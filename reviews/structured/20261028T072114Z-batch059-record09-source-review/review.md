# Scientific review: CARBOXYDOTHERMUS SIDEROPHILUS MEDIUM

- Review: 20261028T072114Z-batch059-record09-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T06:51:20.826468Z
- Finished UTC: 2026-10-28T07:21:14.364325Z
- Reviewer: Codex tsb_source_check (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact507a formulation and preparation are distinguishable from507. Correct the unsupported duplicate graph, stock flattening and nickel form; preserve unresolved variant formulas, source ambiguities and historical version boundaries.

## Scope And Provenance

Whole exact target/owner with explicit scoped dependencies, current sources and historical claims.

Selection: Authoritative batch059 index 09
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:001640 | data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml | generated | carboxydothermus_siderophilus_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:001640 | Actual exit 0; full original streams retained. |
| Canonical strict | passed | True | CultureMech:001640 | Actual exit 0; full original streams retained. |
| Canonical terms | passed | True | CultureMech:001640 | Actual exit 0; full original streams retained. |
| Canonical references | passed | True | CultureMech:001640 | Actual exit 0; full original streams retained. |

## Scientific And Domain Assessments

### Canonical identity and conflicting owner family

identity: concern. Targets: CultureMech:001640.

The target identity and retained preparation match exact DSM507a. Its nine-owner merge and duplicate graph improperly collapse materially distinct 507 and 507a sources; seven named KOMODO child formulations remain independently unresolved. All eight current KOMODO requests failed 403 and remain bounded failed access, not evidence of source absence.

### Classification and existing preparation credit

representation: supported. Targets: CultureMech:001640.

Complex undefined liquid classification is compatible with yeast extract and the source formulation. Existing507a main preparation, pH and 1 bar overpressure are retained and credited; stock preparation must move with its own stage. The name is not evidence of strain growth.

### Complete amounts, units and preparation stages

quantity: concern. Targets: CultureMech:001640.

270 current concentration fields are covered by 67 decisions, including unchanged support and explicit source-only conditions.

{"schema": "fresh-b059-quantity-inventory-v1", "target": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "quantity_field_count": 270, "decisions": [{"quantity_id": "q1", "label": "KCl", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "stored": {"value": "0.326409", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[0].concentration", "stored": {"value": "0.326409", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[0].concentration", "stored": {"value": "0.326409", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[0].concentration", "stored": {"value": "0.326409", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[0].concentration", "stored": {"value": "0.326409", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[0].concentration", "stored": {"value": "0.326409", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[0].concentration", "stored": {"value": "0.326409", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[0].concentration", "stored": {"value": "0.326409", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[0].concentration", "stored": {"value": "0.326409", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[0].concentration", "stored": {"value": "0.326409", "unit": "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner support, separate507 base conflict and unavailable KOMODO variants are distinguished in the layer decisions; no blanket transfer or approval of the ten encoded copies.", "source_stage": "main solutions with distinct source identities", "sources": [{"evidence_id": "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79", "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d", "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 3-3", "quote": "KCl                                                   0.33            g", "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a", "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[0].recipe[0]", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.33,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.326409,\n                        \"mmol_l\": 4.3784,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}, {"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4", "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7", "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 3-3", "quote": "KCl                                                      0.33         g", "quote_basis": "derivative text"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507", "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[0].recipe[0]", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.33,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.322896,\n                        \"mmol_l\": 4.33127,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}], "layer_decisions": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "decision": "evidence_only", "rationale": "The exact 507a API explicitly reports the encoded g_l on declared 1011 mL normalization; the PDF supports its batch mass. Attach evidence without claiming measured final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[0].concentration", "decision": "conflict", "rationale": "The local507a-derived quantity conflicts with or is absent from the separately identified 507 base table. Resolve that source identity before correcting this maintained owner; do not transfer507a amounts."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[0].concentration", "decision": "evidence_only", "rationale": "The exact 507a API explicitly reports the encoded g_l on declared 1011 mL normalization; the PDF supports its batch mass. Attach evidence without claiming measured final volume."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[0].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[0].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[0].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[0].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[0].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[0].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[0].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id": "q2", "label": "MgCl2 x 6 H2O", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "stored": {"value": "0.514342", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[1].concentration", "stored": {"value": "0.514342", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[1].concentration", "stored": {"value": "0.514342", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[1].concentration", "stored": {"value": "0.514342", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[1].concentration", "stored": {"value": "0.514342", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[1].concentration", "stored": {"value": "0.514342", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[1].concentration", "stored": {"value": "0.514342", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[1].concentration", "stored": {"value": "0.514342", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[1].concentration", "stored": {"value": "0.514342", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[1].concentration", "stored": {"value": "0.514342", "unit": "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner support, separate507 base conflict and unavailable KOMODO variants are distinguished in the layer decisions; no blanket transfer or approval of the ten encoded copies.", "source_stage": "main solutions with distinct source identities", "sources": [{"evidence_id": "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79", "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d", "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 4-4", "quote": "MgCl2 x 6 H2O                                         0.52            g", "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a", "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[0].recipe[1]", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 0.52,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.514342,\n                        \"mmol_l\": 2.52993,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}, {"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4", "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7", "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 4-4", "quote": "MgCl2 x 6 H2O                                            0.52         g", "quote_basis": "derivative text"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507", "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[0].recipe[1]", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 0.52,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.508806,\n                        \"mmol_l\": 2.5027,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}], "layer_decisions": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "decision": "evidence_only", "rationale": "The exact 507a API explicitly reports the encoded g_l on declared 1011 mL normalization; the PDF supports its batch mass. Attach evidence without claiming measured final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[1].concentration", "decision": "conflict", "rationale": "The local507a-derived quantity conflicts with or is absent from the separately identified 507 base table. Resolve that source identity before correcting this maintained owner; do not transfer507a amounts."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[1].concentration", "decision": "evidence_only", "rationale": "The exact 507a API explicitly reports the encoded g_l on declared 1011 mL normalization; the PDF supports its batch mass. Attach evidence without claiming measured final volume."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[1].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[1].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[1].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[1].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[1].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[1].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[1].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id": "q3", "label": "CaCl2 x 2 H2O", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "stored": {"value": "0.286845", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[2].concentration", "stored": {"value": "0.286845", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[2].concentration", "stored": {"value": "0.286845", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[2].concentration", "stored": {"value": "0.286845", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[2].concentration", "stored": {"value": "0.286845", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[2].concentration", "stored": {"value": "0.286845", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[2].concentration", "stored": {"value": "0.286845", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[2].concentration", "stored": {"value": "0.286845", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[2].concentration", "stored": {"value": "0.286845", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[2].concentration", "stored": {"value": "0.286845", "unit": "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner support, separate507 base conflict and unavailable KOMODO variants are distinguished in the layer decisions; no blanket transfer or approval of the ten encoded copies.", "source_stage": "main solutions with distinct source identities", "sources": [{"evidence_id": "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79", "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d", "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 5-5", "quote": "CaCl2 x 2 H2O                                         0.29            g", "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a", "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[0].recipe[2]", "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.29,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.286845,\n                        \"mmol_l\": 1.95113,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}, {"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4", "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7", "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 5-5", "quote": "CaCl2 x 2 H2O                                            0.29         g", "quote_basis": "derivative text"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507", "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[0].recipe[2]", "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.29,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.283757,\n                        \"mmol_l\": 1.93013,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}], "layer_decisions": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "decision": "evidence_only", "rationale": "The exact 507a API explicitly reports the encoded g_l on declared 1011 mL normalization; the PDF supports its batch mass. Attach evidence without claiming measured final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[2].concentration", "decision": "conflict", "rationale": "The local507a-derived quantity conflicts with or is absent from the separately identified 507 base table. Resolve that source identity before correcting this maintained owner; do not transfer507a amounts."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[2].concentration", "decision": "evidence_only", "rationale": "The exact 507a API explicitly reports the encoded g_l on declared 1011 mL normalization; the PDF supports its batch mass. Attach evidence without claiming measured final volume."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[2].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[2].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[2].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[2].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[2].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[2].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[2].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id": "q4", "label": "NH4Cl", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "stored": {"value": "0.326409", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[3].concentration", "stored": {"value": "0.326409", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[3].concentration", "stored": {"value": "0.326409", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[3].concentration", "stored": {"value": "0.326409", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[3].concentration", "stored": {"value": "0.326409", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[3].concentration", "stored": {"value": "0.326409", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[3].concentration", "stored": {"value": "0.326409", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[3].concentration", "stored": {"value": "0.326409", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[3].concentration", "stored": {"value": "0.326409", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[3].concentration", "stored": {"value": "0.326409", "unit": "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner support, separate507 base conflict and unavailable KOMODO variants are distinguished in the layer decisions; no blanket transfer or approval of the ten encoded copies.", "source_stage": "main solutions with distinct source identities", "sources": [{"evidence_id": "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79", "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d", "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 6-6", "quote": "NH4Cl                                                 0.33            g", "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a", "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[0].recipe[3]", "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 0.33,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.326409,\n                        \"mmol_l\": 6.10225,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}, {"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4", "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7", "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 6-6", "quote": "NH4Cl                                                    0.33         g", "quote_basis": "derivative text"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507", "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[0].recipe[3]", "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 0.33,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.322896,\n                        \"mmol_l\": 6.03657,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}], "layer_decisions": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "decision": "evidence_only", "rationale": "The exact 507a API explicitly reports the encoded g_l on declared 1011 mL normalization; the PDF supports its batch mass. Attach evidence without claiming measured final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[3].concentration", "decision": "conflict", "rationale": "The local507a-derived quantity conflicts with or is absent from the separately identified 507 base table. Resolve that source identity before correcting this maintained owner; do not transfer507a amounts."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[3].concentration", "decision": "evidence_only", "rationale": "The exact 507a API explicitly reports the encoded g_l on declared 1011 mL normalization; the PDF supports its batch mass. Attach evidence without claiming measured final volume."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[3].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[3].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[3].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[3].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[3].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[3].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[3].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id": "q5", "label": "KH2PO4", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "stored": {"value": "0.326409", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[4].concentration", "stored": {"value": "0.326409", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[4].concentration", "stored": {"value": "0.326409", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[4].concentration", "stored": {"value": "0.326409", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[4].concentration", "stored": {"value": "0.326409", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[4].concentration", "stored": {"value": "0.326409", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[4].concentration", "stored": {"value": "0.326409", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[4].concentration", "stored": {"value": "0.326409", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[4].concentration", "stored": {"value": "0.326409", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[4].concentration", "stored": {"value": "0.326409", "unit": "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner support, separate507 base conflict and unavailable KOMODO variants are distinguished in the layer decisions; no blanket transfer or approval of the ten encoded copies.", "source_stage": "main solutions with distinct source identities", "sources": [{"evidence_id": "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79", "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d", "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 7-7", "quote": "KH2PO4                                                0.33            g", "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a", "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[0].recipe[4]", "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.33,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.326409,\n                        \"mmol_l\": 2.39857,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}, {"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4", "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7", "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 7-7", "quote": "KH2PO4                                                   0.33         g", "quote_basis": "derivative text"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507", "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[0].recipe[4]", "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.33,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.322896,\n                        \"mmol_l\": 2.37275,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}], "layer_decisions": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "decision": "evidence_only", "rationale": "The exact 507a API explicitly reports the encoded g_l on declared 1011 mL normalization; the PDF supports its batch mass. Attach evidence without claiming measured final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[4].concentration", "decision": "conflict", "rationale": "The local507a-derived quantity conflicts with or is absent from the separately identified 507 base table. Resolve that source identity before correcting this maintained owner; do not transfer507a amounts."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[4].concentration", "decision": "evidence_only", "rationale": "The exact 507a API explicitly reports the encoded g_l on declared 1011 mL normalization; the PDF supports its batch mass. Attach evidence without claiming measured final volume."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[4].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[4].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[4].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[4].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[4].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[4].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[4].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id": "q6", "label": "Na2-9,10-anthraquinone-2,6-disulfonate", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[5].concentration", "stored": {"value": "8.16024", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[5].concentration", "stored": {"value": "8.16024", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[5].concentration", "stored": {"value": "8.16024", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[5].concentration", "stored": {"value": "8.16024", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[5].concentration", "stored": {"value": "8.16024", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[5].concentration", "stored": {"value": "8.16024", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[5].concentration", "stored": {"value": "8.16024", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[5].concentration", "stored": {"value": "8.16024", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[5].concentration", "stored": {"value": "8.16024", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[5].concentration", "stored": {"value": "8.16024", "unit": "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner support, separate507 base conflict and unavailable KOMODO variants are distinguished in the layer decisions; no blanket transfer or approval of the ten encoded copies.", "source_stage": "main solutions with distinct source identities", "sources": [{"evidence_id": "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79", "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d", "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 8-8", "quote": "Na2-9,10-anthraquinone-2,6-disulfonate (TCI A0308)    8.25            g", "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a", "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[0].recipe[5]", "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Na2-9,10-anthraquinone-2,6-disulfonate\",\n                        \"compound_id\": 521,\n                        \"attribute\": \"TCI A0308\",\n                        \"amount\": 8.25,\n                        \"unit\": \"g\",\n                        \"g_l\": 8.16024,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}, {"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4", "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7", "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 3-14", "quote": "KCl                                                      0.33         g\n   MgCl2 x 6 H2O                                            0.52         g\n   CaCl2 x 2 H2O                                            0.29         g\n   NH4Cl                                                    0.33         g\n   KH2PO4                                                   0.33         g\n   Trace element solution SL-11                             1.00        ml\n   Sodium resazurin (0.1% w/v)                              0.50        ml\n   NaHCO3                                                   1.00         g\n   Yeast extract                                            0.05         g\n   Wolin's vitamin solution (10x)                           1.00        ml\n   Neutralized sulfide solution 3% (w/v)                   20.00        ml\n   Distilled water                                       1000.00        ml", "quote_basis": "derivative text"}], "layer_decisions": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[5].concentration", "decision": "evidence_only", "rationale": "The exact 507a API explicitly reports the encoded g_l on declared 1011 mL normalization; the PDF supports its batch mass. Attach evidence without claiming measured final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[5].concentration", "decision": "conflict", "rationale": "The local507a-derived quantity conflicts with or is absent from the separately identified 507 base table. Resolve that source identity before correcting this maintained owner; do not transfer507a amounts."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[5].concentration", "decision": "evidence_only", "rationale": "The exact 507a API explicitly reports the encoded g_l on declared 1011 mL normalization; the PDF supports its batch mass. Attach evidence without claiming measured final volume."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[5].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[5].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[5].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[5].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[5].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[5].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[5].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id": "q7", "label": "NaHCO3", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[6].concentration", "stored": {"value": "0.98912", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[6].concentration", "stored": {"value": "0.98912", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[6].concentration", "stored": {"value": "0.98912", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[6].concentration", "stored": {"value": "0.98912", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[6].concentration", "stored": {"value": "0.98912", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[6].concentration", "stored": {"value": "0.98912", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[6].concentration", "stored": {"value": "0.98912", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[6].concentration", "stored": {"value": "0.98912", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[6].concentration", "stored": {"value": "0.98912", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[6].concentration", "stored": {"value": "0.98912", "unit": "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner support, separate507 base conflict and unavailable KOMODO variants are distinguished in the layer decisions; no blanket transfer or approval of the ten encoded copies.", "source_stage": "main solutions with distinct source identities", "sources": [{"evidence_id": "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79", "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d", "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 10-10", "quote": "NaHCO3                                                1.00            g", "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a", "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[0].recipe[7]", "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.98912,\n                        \"mmol_l\": 11.7743,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}, {"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4", "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7", "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 10-10", "quote": "NaHCO3                                                   1.00         g", "quote_basis": "derivative text"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507", "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[0].recipe[7]", "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.978474,\n                        \"mmol_l\": 11.6475,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}], "layer_decisions": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[6].concentration", "decision": "evidence_only", "rationale": "The exact 507a API explicitly reports the encoded g_l on declared 1011 mL normalization; the PDF supports its batch mass. Attach evidence without claiming measured final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[6].concentration", "decision": "conflict", "rationale": "The local507a-derived quantity conflicts with or is absent from the separately identified 507 base table. Resolve that source identity before correcting this maintained owner; do not transfer507a amounts."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[6].concentration", "decision": "evidence_only", "rationale": "The exact 507a API explicitly reports the encoded g_l on declared 1011 mL normalization; the PDF supports its batch mass. Attach evidence without claiming measured final volume."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[6].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[6].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[6].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[6].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[6].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[6].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[6].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id": "q8", "label": "Yeast extract", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[7].concentration", "stored": {"value": "0.197824", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[7].concentration", "stored": {"value": "0.197824", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[7].concentration", "stored": {"value": "0.197824", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[7].concentration", "stored": {"value": "0.197824", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[7].concentration", "stored": {"value": "0.197824", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[7].concentration", "stored": {"value": "0.197824", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[7].concentration", "stored": {"value": "0.197824", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[7].concentration", "stored": {"value": "0.197824", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[7].concentration", "stored": {"value": "0.197824", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[7].concentration", "stored": {"value": "0.197824", "unit": "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner support, separate507 base conflict and unavailable KOMODO variants are distinguished in the layer decisions; no blanket transfer or approval of the ten encoded copies.", "source_stage": "main solutions with distinct source identities", "sources": [{"evidence_id": "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79", "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d", "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 11-11", "quote": "Yeast extract                                         0.20            g", "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a", "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[0].recipe[8]", "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.197824,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}, {"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4", "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7", "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 11-11", "quote": "Yeast extract                                            0.05         g", "quote_basis": "derivative text"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507", "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[0].recipe[8]", "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 0.05,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0489237,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}], "layer_decisions": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[7].concentration", "decision": "evidence_only", "rationale": "The exact 507a API explicitly reports the encoded g_l on declared 1011 mL normalization; the PDF supports its batch mass. Attach evidence without claiming measured final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[7].concentration", "decision": "conflict", "rationale": "The local507a-derived quantity conflicts with or is absent from the separately identified 507 base table. Resolve that source identity before correcting this maintained owner; do not transfer507a amounts."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[7].concentration", "decision": "evidence_only", "rationale": "The exact 507a API explicitly reports the encoded g_l on declared 1011 mL normalization; the PDF supports its batch mass. Attach evidence without claiming measured final volume."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[7].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[7].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[7].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[7].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[7].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[7].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[7].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id": "q9", "label": "Na2-EDTA", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[8].concentration", "stored": {"value": "0.5", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[8].concentration", "stored": {"value": "0.5", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[8].concentration", "stored": {"value": "0.5", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[8].concentration", "stored": {"value": "0.5", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[8].concentration", "stored": {"value": "0.5", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[8].concentration", "stored": {"value": "0.5", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[8].concentration", "stored": {"value": "0.5", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[8].concentration", "stored": {"value": "0.5", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[8].concentration", "stored": {"value": "0.5", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[8].concentration", "stored": {"value": "0.5", "unit": "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner support, separate507 base conflict and unavailable KOMODO variants are distinguished in the layer decisions; no blanket transfer or approval of the ten encoded copies.", "source_stage": "distinct SL-4 and SL-11 stocks", "sources": [{"evidence_id": "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79", "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d", "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 29-29", "quote": "Na2-EDTA                                                 0.50         g", "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a", "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[1].recipe[0]", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2-EDTA\",\n                        \"compound_id\": 34,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 1.48718,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}, {"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4", "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7", "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 44-44", "quote": "Na2-EDTA x 2 H2O                                          5.20        g", "quote_basis": "derivative text"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507", "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[1].recipe[0]", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2-EDTA x 2 H2O\",\n                        \"compound_id\": 676,\n                        \"amount\": 5.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 5.2,\n                        \"mmol_l\": 15.4667,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}], "layer_decisions": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[8].concentration", "decision": "correct", "rationale": "This is a declared SL-4 stock quantity flattened into main ingredients. Restore the source stock and 10 mL batch addition; water input alone does not establish measured stock or receiving final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[8].concentration", "decision": "conflict", "rationale": "The local SL-4-like item cannot substitute for the differently composed SL-11 embedded in507. Its source stock must be resolved separately, retaining exact salt form and batch/final-makeup scope."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[8].concentration", "decision": "correct", "rationale": "This is a declared SL-4 stock quantity flattened into main ingredients. Restore the source stock and 10 mL batch addition; water input alone does not establish measured stock or receiving final volume."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[8].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[8].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[8].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[8].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[8].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[8].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[8].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id": "q10", "label": "FeSO4 x 7 H2O", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[9].concentration", "stored": {"value": "0.2", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[9].concentration", "stored": {"value": "0.2", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[9].concentration", "stored": {"value": "0.2", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[9].concentration", "stored": {"value": "0.2", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[9].concentration", "stored": {"value": "0.2", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[9].concentration", "stored": {"value": "0.2", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[9].concentration", "stored": {"value": "0.2", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[9].concentration", "stored": {"value": "0.2", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[9].concentration", "stored": {"value": "0.2", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[9].concentration", "stored": {"value": "0.2", "unit": "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner support, separate507 base conflict and unavailable KOMODO variants are distinguished in the layer decisions; no blanket transfer or approval of the ten encoded copies.", "source_stage": "distinct SL-4 and SL-11 stocks", "sources": [{"evidence_id": "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79", "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d", "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 30-30", "quote": "FeSO4 x 7 H2O                                            0.20         g", "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a", "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[1].recipe[1]", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 0.719386,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}, {"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4", "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7", "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 45-45", "quote": "FeCl2 x 4 H2O                                             1.50        g", "quote_basis": "derivative text"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507", "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[1].recipe[1]", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\": 260,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.54482,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}], "layer_decisions": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[9].concentration", "decision": "correct", "rationale": "This is a declared SL-4 stock quantity flattened into main ingredients. Restore the source stock and 10 mL batch addition; water input alone does not establish measured stock or receiving final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[9].concentration", "decision": "conflict", "rationale": "The local SL-4-like item cannot substitute for the differently composed SL-11 embedded in507. Its source stock must be resolved separately, retaining exact salt form and batch/final-makeup scope."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[9].concentration", "decision": "correct", "rationale": "This is a declared SL-4 stock quantity flattened into main ingredients. Restore the source stock and 10 mL batch addition; water input alone does not establish measured stock or receiving final volume."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[9].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[9].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[9].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[9].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[9].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[9].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[9].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id": "q11", "label": "ZnSO4 x 7 H2O", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[10].concentration", "stored": {"value": "0.1", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[10].concentration", "stored": {"value": "0.1", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[10].concentration", "stored": {"value": "0.1", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[10].concentration", "stored": {"value": "0.1", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[10].concentration", "stored": {"value": "0.1", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[10].concentration", "stored": {"value": "0.1", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[10].concentration", "stored": {"value": "0.1", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[10].concentration", "stored": {"value": "0.1", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[10].concentration", "stored": {"value": "0.1", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[10].concentration", "stored": {"value": "0.1", "unit": "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner support, separate507 base conflict and unavailable KOMODO variants are distinguished in the layer decisions; no blanket transfer or approval of the ten encoded copies.", "source_stage": "distinct SL-4 and SL-11 stocks", "sources": [{"evidence_id": "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79", "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d", "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 31-31", "quote": "ZnSO4 x 7 H2O                                            0.10         g", "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a", "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[1].recipe[2]", "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.347752,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}, {"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4", "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7", "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 54-54", "quote": "ZnCl2                                                   70.00      mg", "quote_basis": "derivative text"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507", "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[1].recipe[2]", "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\": 64,\n                        \"amount\": 70,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\": 0.513573,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}], "layer_decisions": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[10].concentration", "decision": "correct", "rationale": "This is a declared SL-4 stock quantity flattened into main ingredients. Restore the source stock and 10 mL batch addition; water input alone does not establish measured stock or receiving final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[10].concentration", "decision": "conflict", "rationale": "The local SL-4-like item cannot substitute for the differently composed SL-11 embedded in507. Its source stock must be resolved separately, retaining exact salt form and batch/final-makeup scope."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[10].concentration", "decision": "correct", "rationale": "This is a declared SL-4 stock quantity flattened into main ingredients. Restore the source stock and 10 mL batch addition; water input alone does not establish measured stock or receiving final volume."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[10].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[10].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[10].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[10].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[10].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[10].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[10].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id": "q12", "label": "MnCl2 x 4 H2O", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[11].concentration", "stored": {"value": "0.03", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[11].concentration", "stored": {"value": "0.03", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[11].concentration", "stored": {"value": "0.03", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[11].concentration", "stored": {"value": "0.03", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[11].concentration", "stored": {"value": "0.03", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[11].concentration", "stored": {"value": "0.03", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[11].concentration", "stored": {"value": "0.03", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[11].concentration", "stored": {"value": "0.03", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[11].concentration", "stored": {"value": "0.03", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[11].concentration", "stored": {"value": "0.03", "unit": "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner support, separate507 base conflict and unavailable KOMODO variants are distinguished in the layer decisions; no blanket transfer or approval of the ten encoded copies.", "source_stage": "distinct SL-4 and SL-11 stocks", "sources": [{"evidence_id": "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79", "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d", "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 32-32", "quote": "MnCl2 x 4 H2O                                            0.03         g", "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a", "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[1].recipe[3]", "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 0.03,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\": 0.151588,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}, {"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4", "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7", "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 55-55", "quote": "MnCl2 x 4 H2O                                          100.00      mg", "quote_basis": "derivative text"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507", "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[1].recipe[3]", "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.505293,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}], "layer_decisions": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[11].concentration", "decision": "correct", "rationale": "This is a declared SL-4 stock quantity flattened into main ingredients. Restore the source stock and 10 mL batch addition; water input alone does not establish measured stock or receiving final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[11].concentration", "decision": "conflict", "rationale": "The local SL-4-like item cannot substitute for the differently composed SL-11 embedded in507. Its source stock must be resolved separately, retaining exact salt form and batch/final-makeup scope."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[11].concentration", "decision": "correct", "rationale": "This is a declared SL-4 stock quantity flattened into main ingredients. Restore the source stock and 10 mL batch addition; water input alone does not establish measured stock or receiving final volume."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[11].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[11].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[11].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[11].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[11].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[11].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[11].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id": "q13", "label": "H3BO3", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[12].concentration", "stored": {"value": "0.3", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[12].concentration", "stored": {"value": "0.3", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[12].concentration", "stored": {"value": "0.3", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[12].concentration", "stored": {"value": "0.3", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[12].concentration", "stored": {"value": "0.3", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[12].concentration", "stored": {"value": "0.3", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[12].concentration", "stored": {"value": "0.3", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[12].concentration", "stored": {"value": "0.3", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[12].concentration", "stored": {"value": "0.3", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[12].concentration", "stored": {"value": "0.3", "unit": "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner support, separate507 base conflict and unavailable KOMODO variants are distinguished in the layer decisions; no blanket transfer or approval of the ten encoded copies.", "source_stage": "distinct SL-4 and SL-11 stocks", "sources": [{"evidence_id": "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79", "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d", "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 33-33", "quote": "H3BO3                                                    0.30         g", "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a", "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[1].recipe[4]", "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\": 4.85123,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}, {"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4", "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7", "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 56-56", "quote": "H3BO3                                                    6.00      mg", "quote_basis": "derivative text"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507", "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[1].recipe[4]", "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 6,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\": 0.0970246,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}], "layer_decisions": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[12].concentration", "decision": "correct", "rationale": "This is a declared SL-4 stock quantity flattened into main ingredients. Restore the source stock and 10 mL batch addition; water input alone does not establish measured stock or receiving final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[12].concentration", "decision": "conflict", "rationale": "The local SL-4-like item cannot substitute for the differently composed SL-11 embedded in507. Its source stock must be resolved separately, retaining exact salt form and batch/final-makeup scope."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[12].concentration", "decision": "correct", "rationale": "This is a declared SL-4 stock quantity flattened into main ingredients. Restore the source stock and 10 mL batch addition; water input alone does not establish measured stock or receiving final volume."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[12].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[12].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[12].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[12].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[12].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[12].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[12].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id": "q14", "label": "CoCl2 x 6 H2O", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[13].concentration", "stored": {"value": "0.2", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[13].concentration", "stored": {"value": "0.2", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[13].concentration", "stored": {"value": "0.2", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[13].concentration", "stored": {"value": "0.2", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[13].concentration", "stored": {"value": "0.2", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[13].concentration", "stored": {"value": "0.2", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[13].concentration", "stored": {"value": "0.2", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[13].concentration", "stored": {"value": "0.2", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[13].concentration", "stored": {"value": "0.2", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[13].concentration", "stored": {"value": "0.2", "unit": "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner support, separate507 base conflict and unavailable KOMODO variants are distinguished in the layer decisions; no blanket transfer or approval of the ten encoded copies.", "source_stage": "distinct SL-4 and SL-11 stocks", "sources": [{"evidence_id": "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79", "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d", "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 34-34", "quote": "CoCl2 x 6 H2O                                            0.20         g", "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a", "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[1].recipe[5]", "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.54037,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}, {"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4", "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7", "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 57-57", "quote": "CoCl2 x 6 H2O                                          190.00      mg", "quote_basis": "derivative text"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507", "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[1].recipe[5]", "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 190,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\": 1.46335,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}], "layer_decisions": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[13].concentration", "decision": "correct", "rationale": "This is a declared SL-4 stock quantity flattened into main ingredients. Restore the source stock and 10 mL batch addition; water input alone does not establish measured stock or receiving final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[13].concentration", "decision": "conflict", "rationale": "The local SL-4-like item cannot substitute for the differently composed SL-11 embedded in507. Its source stock must be resolved separately, retaining exact salt form and batch/final-makeup scope."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[13].concentration", "decision": "correct", "rationale": "This is a declared SL-4 stock quantity flattened into main ingredients. Restore the source stock and 10 mL batch addition; water input alone does not establish measured stock or receiving final volume."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[13].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[13].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[13].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[13].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[13].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[13].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[13].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id": "q15", "label": "CuCl2 x 2 H2O", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[14].concentration", "stored": {"value": "0.01", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[14].concentration", "stored": {"value": "0.01", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[14].concentration", "stored": {"value": "0.01", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[14].concentration", "stored": {"value": "0.01", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[14].concentration", "stored": {"value": "0.01", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[14].concentration", "stored": {"value": "0.01", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[14].concentration", "stored": {"value": "0.01", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[14].concentration", "stored": {"value": "0.01", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[14].concentration", "stored": {"value": "0.01", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[14].concentration", "stored": {"value": "0.01", "unit": "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner support, separate507 base conflict and unavailable KOMODO variants are distinguished in the layer decisions; no blanket transfer or approval of the ten encoded copies.", "source_stage": "distinct SL-4 and SL-11 stocks", "sources": [{"evidence_id": "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79", "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d", "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 35-35", "quote": "CuCl2 x 2 H2O                                            0.01         g", "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a", "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[1].recipe[6]", "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0586569,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}, {"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4", "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7", "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 58-58", "quote": "CuCl2 x 2 H2O                                            2.00      mg", "quote_basis": "derivative text"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507", "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[1].recipe[6]", "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.0117314,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}], "layer_decisions": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[14].concentration", "decision": "correct", "rationale": "This is a declared SL-4 stock quantity flattened into main ingredients. Restore the source stock and 10 mL batch addition; water input alone does not establish measured stock or receiving final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[14].concentration", "decision": "conflict", "rationale": "The local SL-4-like item cannot substitute for the differently composed SL-11 embedded in507. Its source stock must be resolved separately, retaining exact salt form and batch/final-makeup scope."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[14].concentration", "decision": "correct", "rationale": "This is a declared SL-4 stock quantity flattened into main ingredients. Restore the source stock and 10 mL batch addition; water input alone does not establish measured stock or receiving final volume."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[14].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[14].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[14].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[14].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[14].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[14].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[14].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id": "q16", "label": "NiCl2 x 6 H2O", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[15].concentration", "stored": {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[15].concentration", "stored": {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[15].concentration", "stored": {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[15].concentration", "stored": {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[15].concentration", "stored": {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[15].concentration", "stored": {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[15].concentration", "stored": {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[15].concentration", "stored": {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[15].concentration", "stored": {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[15].concentration", "stored": {"value": "0.02", "unit": "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner support, separate507 base conflict and unavailable KOMODO variants are distinguished in the layer decisions; no blanket transfer or approval of the ten encoded copies.", "source_stage": "distinct SL-4 and SL-11 stocks", "sources": [{"evidence_id": "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79", "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d", "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 36-36", "quote": "NiCl2 x 6 H2O                                            0.02         g", "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a", "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[1].recipe[7]", "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 0.02,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.154322,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}, {"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4", "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7", "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 59-59", "quote": "NiCl2 x 6 H2O                                           24.00      mg", "quote_basis": "derivative text"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507", "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[1].recipe[7]", "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 24,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\": 0.185187,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}], "layer_decisions": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[15].concentration", "decision": "correct", "rationale": "This is a declared SL-4 stock quantity flattened into main ingredients. Restore the source stock and 10 mL batch addition; water input alone does not establish measured stock or receiving final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[15].concentration", "decision": "conflict", "rationale": "The local SL-4-like item cannot substitute for the differently composed SL-11 embedded in507. Its source stock must be resolved separately, retaining exact salt form and batch/final-makeup scope."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[15].concentration", "decision": "correct", "rationale": "This is a declared SL-4 stock quantity flattened into main ingredients. Restore the source stock and 10 mL batch addition; water input alone does not establish measured stock or receiving final volume."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[15].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[15].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[15].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[15].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[15].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[15].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[15].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id": "q17", "label": "Na2MoO4 x 2 H2O", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[16].concentration", "stored": {"value": "0.03", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[16].concentration", "stored": {"value": "0.03", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[16].concentration", "stored": {"value": "0.03", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[16].concentration", "stored": {"value": "0.03", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[16].concentration", "stored": {"value": "0.03", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[16].concentration", "stored": {"value": "0.03", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[16].concentration", "stored": {"value": "0.03", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[16].concentration", "stored": {"value": "0.03", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[16].concentration", "stored": {"value": "0.03", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[16].concentration", "stored": {"value": "0.03", "unit": "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner support, separate507 base conflict and unavailable KOMODO variants are distinguished in the layer decisions; no blanket transfer or approval of the ten encoded copies.", "source_stage": "distinct SL-4 and SL-11 stocks", "sources": [{"evidence_id": "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79", "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d", "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 37-37", "quote": "Na2MoO4 x 2 H2O                                          0.03         g", "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a", "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[1].recipe[8]", "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 0.03,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\": 0.123993,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}, {"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4", "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7", "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 60-60", "quote": "Na2MoO4 x 2 H2O                                         36.00      mg", "quote_basis": "derivative text"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507", "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[1].recipe[8]", "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 36,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\": 0.148791,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}], "layer_decisions": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[16].concentration", "decision": "correct", "rationale": "This is a declared SL-4 stock quantity flattened into main ingredients. Restore the source stock and 10 mL batch addition; water input alone does not establish measured stock or receiving final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[16].concentration", "decision": "conflict", "rationale": "The local SL-4-like item cannot substitute for the differently composed SL-11 embedded in507. Its source stock must be resolved separately, retaining exact salt form and batch/final-makeup scope."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[16].concentration", "decision": "correct", "rationale": "This is a declared SL-4 stock quantity flattened into main ingredients. Restore the source stock and 10 mL batch addition; water input alone does not establish measured stock or receiving final volume."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[16].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[16].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[16].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[16].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[16].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[16].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[16].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id": "q18", "label": "Biotin", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[17].concentration", "stored": {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[17].concentration", "stored": {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[17].concentration", "stored": {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[17].concentration", "stored": {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[17].concentration", "stored": {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[17].concentration", "stored": {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[17].concentration", "stored": {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[17].concentration", "stored": {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[17].concentration", "stored": {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[17].concentration", "stored": {"value": "0.02", "unit": "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner support, separate507 base conflict and unavailable KOMODO variants are distinguished in the layer decisions; no blanket transfer or approval of the ten encoded copies.", "source_stage": "Wolin vitamin stock", "sources": [{"evidence_id": "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79", "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d", "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 46-46", "quote": "Biotin                                                   20.00      mg", "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a", "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[2].recipe[0]", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507", "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[2].recipe[0]", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}], "layer_decisions": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[17].concentration", "decision": "correct", "rationale": "The supported stock concentration is flattened into the main ingredients. Restore the vitamin stock and 1 mL batch addition without inventing a receiving-litre denominator."}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[17].concentration", "decision": "correct", "rationale": "Both primary recipes place this item in the vitamin stock, not directly in the main medium. Matching stock composition does not authenticate the complete medium or any separate KOMODO variant."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[17].concentration", "decision": "correct", "rationale": "The supported stock concentration is flattened into the main ingredients. Restore the vitamin stock and 1 mL batch addition without inventing a receiving-litre denominator."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[17].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[17].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[17].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[17].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[17].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[17].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[17].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id": "q19", "label": "Folic acid", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[18].concentration", "stored": {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[18].concentration", "stored": {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[18].concentration", "stored": {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[18].concentration", "stored": {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[18].concentration", "stored": {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[18].concentration", "stored": {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[18].concentration", "stored": {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[18].concentration", "stored": {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[18].concentration", "stored": {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[18].concentration", "stored": {"value": "0.02", "unit": "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner support, separate507 base conflict and unavailable KOMODO variants are distinguished in the layer decisions; no blanket transfer or approval of the ten encoded copies.", "source_stage": "Wolin vitamin stock", "sources": [{"evidence_id": "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79", "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d", "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 56-56", "quote": "Folic acid                             20.00   mg", "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a", "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[2].recipe[1]", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0453104,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507", "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[2].recipe[1]", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0453104,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}], "layer_decisions": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[18].concentration", "decision": "correct", "rationale": "The supported stock concentration is flattened into the main ingredients. Restore the vitamin stock and 1 mL batch addition without inventing a receiving-litre denominator."}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[18].concentration", "decision": "correct", "rationale": "Both primary recipes place this item in the vitamin stock, not directly in the main medium. Matching stock composition does not authenticate the complete medium or any separate KOMODO variant."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[18].concentration", "decision": "correct", "rationale": "The supported stock concentration is flattened into the main ingredients. Restore the vitamin stock and 1 mL batch addition without inventing a receiving-litre denominator."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[18].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[18].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[18].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[18].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[18].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[18].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[18].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id": "q20", "label": "Pyridoxine hydrochloride", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[19].concentration", "stored": {"value": "0.1", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[19].concentration", "stored": {"value": "0.1", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[19].concentration", "stored": {"value": "0.1", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[19].concentration", "stored": {"value": "0.1", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[19].concentration", "stored": {"value": "0.1", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[19].concentration", "stored": {"value": "0.1", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[19].concentration", "stored": {"value": "0.1", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[19].concentration", "stored": {"value": "0.1", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[19].concentration", "stored": {"value": "0.1", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[19].concentration", "stored": {"value": "0.1", "unit": "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner support, separate507 base conflict and unavailable KOMODO variants are distinguished in the layer decisions; no blanket transfer or approval of the ten encoded copies.", "source_stage": "Wolin vitamin stock", "sources": [{"evidence_id": "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79", "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d", "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 57-57", "quote": "Pyridoxine hydrochloride              100.00   mg", "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a", "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[2].recipe[2]", "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.486287,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507", "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[2].recipe[2]", "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.486287,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}], "layer_decisions": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[19].concentration", "decision": "correct", "rationale": "The supported stock concentration is flattened into the main ingredients. Restore the vitamin stock and 1 mL batch addition without inventing a receiving-litre denominator."}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[19].concentration", "decision": "correct", "rationale": "Both primary recipes place this item in the vitamin stock, not directly in the main medium. Matching stock composition does not authenticate the complete medium or any separate KOMODO variant."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[19].concentration", "decision": "correct", "rationale": "The supported stock concentration is flattened into the main ingredients. Restore the vitamin stock and 1 mL batch addition without inventing a receiving-litre denominator."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[19].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[19].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[19].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[19].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[19].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[19].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[19].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id": "q21", "label": "Thiamine HCl", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[20].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[20].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[20].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[20].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[20].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[20].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[20].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[20].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[20].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[20].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner support, separate507 base conflict and unavailable KOMODO variants are distinguished in the layer decisions; no blanket transfer or approval of the ten encoded copies.", "source_stage": "Wolin vitamin stock", "sources": [{"evidence_id": "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79", "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d", "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 58-58", "quote": "Thiamine HCl                           50.00   mg", "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a", "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[2].recipe[3]", "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.148236,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507", "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[2].recipe[3]", "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.148236,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}], "layer_decisions": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[20].concentration", "decision": "correct", "rationale": "The supported stock concentration is flattened into the main ingredients. Restore the vitamin stock and 1 mL batch addition without inventing a receiving-litre denominator."}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[20].concentration", "decision": "correct", "rationale": "Both primary recipes place this item in the vitamin stock, not directly in the main medium. Matching stock composition does not authenticate the complete medium or any separate KOMODO variant."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[20].concentration", "decision": "correct", "rationale": "The supported stock concentration is flattened into the main ingredients. Restore the vitamin stock and 1 mL batch addition without inventing a receiving-litre denominator."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[20].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[20].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[20].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[20].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[20].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[20].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[20].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id": "q22", "label": "Riboflavin", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[21].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[21].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[21].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[21].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[21].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[21].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[21].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[21].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[21].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[21].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner support, separate507 base conflict and unavailable KOMODO variants are distinguished in the layer decisions; no blanket transfer or approval of the ten encoded copies.", "source_stage": "Wolin vitamin stock", "sources": [{"evidence_id": "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79", "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d", "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 59-59", "quote": "Riboflavin                             50.00   mg", "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a", "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[2].recipe[4]", "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.132837,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507", "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[2].recipe[4]", "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.132837,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}], "layer_decisions": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[21].concentration", "decision": "correct", "rationale": "The supported stock concentration is flattened into the main ingredients. Restore the vitamin stock and 1 mL batch addition without inventing a receiving-litre denominator."}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[21].concentration", "decision": "correct", "rationale": "Both primary recipes place this item in the vitamin stock, not directly in the main medium. Matching stock composition does not authenticate the complete medium or any separate KOMODO variant."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[21].concentration", "decision": "correct", "rationale": "The supported stock concentration is flattened into the main ingredients. Restore the vitamin stock and 1 mL batch addition without inventing a receiving-litre denominator."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[21].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[21].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[21].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[21].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[21].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[21].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[21].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id": "q23", "label": "Nicotinic acid", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[22].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[22].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[22].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[22].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[22].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[22].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[22].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[22].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[22].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[22].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner support, separate507 base conflict and unavailable KOMODO variants are distinguished in the layer decisions; no blanket transfer or approval of the ten encoded copies.", "source_stage": "Wolin vitamin stock", "sources": [{"evidence_id": "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79", "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d", "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 60-60", "quote": "Nicotinic acid                         50.00   mg", "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a", "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[2].recipe[5]", "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.406141,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507", "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[2].recipe[5]", "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.406141,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}], "layer_decisions": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[22].concentration", "decision": "correct", "rationale": "The supported stock concentration is flattened into the main ingredients. Restore the vitamin stock and 1 mL batch addition without inventing a receiving-litre denominator."}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[22].concentration", "decision": "correct", "rationale": "Both primary recipes place this item in the vitamin stock, not directly in the main medium. Matching stock composition does not authenticate the complete medium or any separate KOMODO variant."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[22].concentration", "decision": "correct", "rationale": "The supported stock concentration is flattened into the main ingredients. Restore the vitamin stock and 1 mL batch addition without inventing a receiving-litre denominator."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[22].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[22].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[22].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[22].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[22].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[22].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[22].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id": "q24", "label": "Calcium D-(+)-pantothenate", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[23].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[23].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[23].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[23].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[23].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[23].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[23].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[23].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[23].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[23].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner support, separate507 base conflict and unavailable KOMODO variants are distinguished in the layer decisions; no blanket transfer or approval of the ten encoded copies.", "source_stage": "Wolin vitamin stock", "sources": [{"evidence_id": "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79", "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d", "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 61-61", "quote": "Calcium D-(+)-pantothenate             50.00   mg", "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a", "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[2].recipe[6]", "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\": 1512,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.209846,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507", "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[2].recipe[6]", "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\": 1512,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.209846,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}], "layer_decisions": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[23].concentration", "decision": "correct", "rationale": "The supported stock concentration is flattened into the main ingredients. Restore the vitamin stock and 1 mL batch addition without inventing a receiving-litre denominator."}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[23].concentration", "decision": "correct", "rationale": "Both primary recipes place this item in the vitamin stock, not directly in the main medium. Matching stock composition does not authenticate the complete medium or any separate KOMODO variant."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[23].concentration", "decision": "correct", "rationale": "The supported stock concentration is flattened into the main ingredients. Restore the vitamin stock and 1 mL batch addition without inventing a receiving-litre denominator."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[23].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[23].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[23].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[23].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[23].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[23].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[23].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id": "q25", "label": "Vitamin B12", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[24].concentration", "stored": {"value": "0.001", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[24].concentration", "stored": {"value": "0.001", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[24].concentration", "stored": {"value": "0.001", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[24].concentration", "stored": {"value": "0.001", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[24].concentration", "stored": {"value": "0.001", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[24].concentration", "stored": {"value": "0.001", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[24].concentration", "stored": {"value": "0.001", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[24].concentration", "stored": {"value": "0.001", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[24].concentration", "stored": {"value": "0.001", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[24].concentration", "stored": {"value": "0.001", "unit": "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner support, separate507 base conflict and unavailable KOMODO variants are distinguished in the layer decisions; no blanket transfer or approval of the ten encoded copies.", "source_stage": "Wolin vitamin stock", "sources": [{"evidence_id": "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79", "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d", "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 62-62", "quote": "Vitamin B12                             1.00   mg", "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a", "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[2].recipe[7]", "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\": 0.00073779,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507", "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[2].recipe[7]", "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\": 0.00073779,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}], "layer_decisions": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[24].concentration", "decision": "correct", "rationale": "The supported stock concentration is flattened into the main ingredients. Restore the vitamin stock and 1 mL batch addition without inventing a receiving-litre denominator."}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[24].concentration", "decision": "correct", "rationale": "Both primary recipes place this item in the vitamin stock, not directly in the main medium. Matching stock composition does not authenticate the complete medium or any separate KOMODO variant."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[24].concentration", "decision": "correct", "rationale": "The supported stock concentration is flattened into the main ingredients. Restore the vitamin stock and 1 mL batch addition without inventing a receiving-litre denominator."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[24].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[24].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[24].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[24].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[24].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[24].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[24].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id": "q26", "label": "p-Aminobenzoic acid", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[25].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[25].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[25].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[25].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[25].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[25].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[25].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[25].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[25].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[25].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner support, separate507 base conflict and unavailable KOMODO variants are distinguished in the layer decisions; no blanket transfer or approval of the ten encoded copies.", "source_stage": "Wolin vitamin stock", "sources": [{"evidence_id": "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79", "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d", "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 63-63", "quote": "p-Aminobenzoic acid                    50.00   mg", "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a", "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[2].recipe[8]", "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.364591,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507", "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[2].recipe[8]", "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.364591,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}], "layer_decisions": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[25].concentration", "decision": "correct", "rationale": "The supported stock concentration is flattened into the main ingredients. Restore the vitamin stock and 1 mL batch addition without inventing a receiving-litre denominator."}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[25].concentration", "decision": "correct", "rationale": "Both primary recipes place this item in the vitamin stock, not directly in the main medium. Matching stock composition does not authenticate the complete medium or any separate KOMODO variant."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[25].concentration", "decision": "correct", "rationale": "The supported stock concentration is flattened into the main ingredients. Restore the vitamin stock and 1 mL batch addition without inventing a receiving-litre denominator."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[25].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[25].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[25].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[25].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[25].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[25].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[25].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id": "q27", "label": "(DL)-alpha-Lipoic acid", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[26].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[26].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[26].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[26].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[26].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[26].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[26].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[26].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[26].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[26].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner support, separate507 base conflict and unavailable KOMODO variants are distinguished in the layer decisions; no blanket transfer or approval of the ten encoded copies.", "source_stage": "Wolin vitamin stock", "sources": [{"evidence_id": "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79", "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d", "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 64-64", "quote": "(DL)-alpha-Lipoic acid                 50.00   mg", "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a", "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[2].recipe[9]", "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\": 252,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.24233,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507", "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[2].recipe[9]", "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\": 252,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.24233,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}], "layer_decisions": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ingredients[26].concentration", "decision": "correct", "rationale": "The supported stock concentration is flattened into the main ingredients. Restore the vitamin stock and 1 mL batch addition without inventing a receiving-litre denominator."}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ingredients[26].concentration", "decision": "correct", "rationale": "Both primary recipes place this item in the vitamin stock, not directly in the main medium. Matching stock composition does not authenticate the complete medium or any separate KOMODO variant."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ingredients[26].concentration", "decision": "correct", "rationale": "The supported stock concentration is flattened into the main ingredients. Restore the vitamin stock and 1 mL batch addition without inventing a receiving-litre denominator."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ingredients[26].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[26].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[26].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[26].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[26].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ingredients[26].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ingredients[26].concentration", "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned 403. Its local copied signature and base-source link do not authenticate this amount. Preserve unresolved variant provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id": "q28", "label": "Existing pH: carboxydothermus_siderophilus_medium", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "ph_value", "stored": 6.9}], "decision": "evidence_only", "rationale": "The declared507a pH 6.9 lies within the printed 6.8–7.0 final range; preserve this supported value and source distinction.", "source_stage": "source-specific pH", "sources": [{"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a", "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.medium", "quote": "{\n            \"id\": \"507a\",\n            \"name\": \"CARBOXYDOTHERMUS SIDEROPHILUS MEDIUM\",\n            \"complex_medium\": \"yes\",\n            \"min_pH\": 6.9,\n            \"max_pH\": 6.9,\n            \"source\": \"DSMZ\",\n            \"link\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf\"\n        }", "quote_basis": "raw UTF-8"}, {"evidence_id": "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79", "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d", "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 21-21", "quote": "After completing the medium adjust pH to 6.8 - 7.0.", "quote_basis": "derivative text"}]}, {"quantity_id": "q29", "label": "Existing pH: carboxydothermus_medium", "local_fields": [{"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ph_value", "stored": 6.9}], "decision": "evidence_only", "rationale": "The value agrees with the exact printed base range or named DSM override. This does not certify the complete KOMODO formulation or transfer that override to 507a.", "source_stage": "source-specific pH", "sources": [{"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4", "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7", "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 23-23", "quote": "medium adjust pH to 6.8-7.0.", "quote_basis": "derivative text"}]}, {"quantity_id": "q30", "label": "Existing pH range: carboxydothermus_medium", "local_fields": [{"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ph_range.min", "stored": 6.8}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml", "field_path": "ph_range.max", "stored": 7.0}], "decision": "evidence_only", "rationale": "The base507 source prints 6.8–7.0; its transfer to separately named variants remains unverified when exact variant evidence is unavailable.", "source_stage": "base range or unresolved variant assertion", "sources": [{"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4", "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7", "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 23-23", "quote": "medium adjust pH to 6.8-7.0.", "quote_basis": "derivative text"}]}, {"quantity_id": "q31", "label": "Existing pH: carboxydothermus_siderophilus_medium", "local_fields": [{"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "ph_value", "stored": 6.9}], "decision": "evidence_only", "rationale": "The declared507a pH 6.9 lies within the printed 6.8–7.0 final range; preserve this supported value and source distinction.", "source_stage": "source-specific pH", "sources": [{"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a", "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.medium", "quote": "{\n            \"id\": \"507a\",\n            \"name\": \"CARBOXYDOTHERMUS SIDEROPHILUS MEDIUM\",\n            \"complex_medium\": \"yes\",\n            \"min_pH\": 6.9,\n            \"max_pH\": 6.9,\n            \"source\": \"DSMZ\",\n            \"link\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf\"\n        }", "quote_basis": "raw UTF-8"}, {"evidence_id": "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79", "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d", "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 21-21", "quote": "After completing the medium adjust pH to 6.8 - 7.0.", "quote_basis": "derivative text"}]}, {"quantity_id": "q32", "label": "Existing pH: for_dsm_12326", "local_fields": [{"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ph_value", "stored": 6.9}], "decision": "unsupported", "rationale": "This local variant pH is not independently established by the available exact primary and the current KOMODO request failed. Preserve it as an unresolved assertion, not a validated growth optimum.", "source_stage": "source-specific pH", "sources": [{"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4", "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7", "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 23-23", "quote": "medium adjust pH to 6.8-7.0.", "quote_basis": "derivative text"}]}, {"quantity_id": "q33", "label": "Existing pH range: for_dsm_12326", "local_fields": [{"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ph_range.min", "stored": 6.8}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ph_range.max", "stored": 7.0}], "decision": "unsupported", "rationale": "The base507 source prints 6.8–7.0; its transfer to separately named variants remains unverified when exact variant evidence is unavailable.", "source_stage": "base range or unresolved variant assertion", "sources": [{"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4", "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7", "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 23-23", "quote": "medium adjust pH to 6.8-7.0.", "quote_basis": "derivative text"}]}, {"quantity_id": "q34", "label": "Existing pH: for_dsm_18923", "local_fields": [{"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ph_value", "stored": 6.9}], "decision": "unsupported", "rationale": "This local variant pH is not independently established by the available exact primary and the current KOMODO request failed. Preserve it as an unresolved assertion, not a validated growth optimum.", "source_stage": "source-specific pH", "sources": [{"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4", "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7", "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 23-23", "quote": "medium adjust pH to 6.8-7.0.", "quote_basis": "derivative text"}]}, {"quantity_id": "q35", "label": "Existing pH range: for_dsm_18923", "local_fields": [{"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ph_range.min", "stored": 6.8}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ph_range.max", "stored": 7.0}], "decision": "unsupported", "rationale": "The base507 source prints 6.8–7.0; its transfer to separately named variants remains unverified when exact variant evidence is unavailable.", "source_stage": "base range or unresolved variant assertion", "sources": [{"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4", "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7", "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 23-23", "quote": "medium adjust pH to 6.8-7.0.", "quote_basis": "derivative text"}]}, {"quantity_id": "q36", "label": "Existing pH: for_dsm_21278", "local_fields": [{"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ph_value", "stored": 6.9}], "decision": "unsupported", "rationale": "This local variant pH is not independently established by the available exact primary and the current KOMODO request failed. Preserve it as an unresolved assertion, not a validated growth optimum.", "source_stage": "source-specific pH", "sources": [{"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4", "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7", "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 23-23", "quote": "medium adjust pH to 6.8-7.0.", "quote_basis": "derivative text"}]}, {"quantity_id": "q37", "label": "Existing pH range: for_dsm_21278", "local_fields": [{"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ph_range.min", "stored": 6.8}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ph_range.max", "stored": 7.0}], "decision": "unsupported", "rationale": "The base507 source prints 6.8–7.0; its transfer to separately named variants remains unverified when exact variant evidence is unavailable.", "source_stage": "base range or unresolved variant assertion", "sources": [{"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4", "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7", "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 23-23", "quote": "medium adjust pH to 6.8-7.0.", "quote_basis": "derivative text"}]}, {"quantity_id": "q38", "label": "Existing pH: for_dsm_21830", "local_fields": [{"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ph_value", "stored": 6.0}], "decision": "evidence_only", "rationale": "The value agrees with the exact printed base range or named DSM override. This does not certify the complete KOMODO formulation or transfer that override to 507a.", "source_stage": "source-specific pH", "sources": [{"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4", "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7", "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 32-32", "quote": "For DSM 21830: Adjust pH of complete medium to 6.0.", "quote_basis": "derivative text"}]}, {"quantity_id": "q39", "label": "Existing pH: for_dsm_23698", "local_fields": [{"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ph_value", "stored": 6.2}], "decision": "evidence_only", "rationale": "The value agrees with the exact printed base range or named DSM override. This does not certify the complete KOMODO formulation or transfer that override to 507a.", "source_stage": "source-specific pH", "sources": [{"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4", "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7", "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 36-38", "quote": "For DSM 23698: Supplement medium with 2.00 g/l Na-pyruvate and omit sulfide. Adjust\nfinal pH of medium to 6.2. Change gas phase to 100% carbon monoxide prior to\ninoculation, but do not use excess pressure.", "quote_basis": "derivative text"}]}, {"quantity_id": "q40", "label": "Existing pH: medium_507_modified_for_dsm_7242", "local_fields": [{"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path": "ph_value", "stored": 7.0}], "decision": "unsupported", "rationale": "This local variant pH is not independently established by the available exact primary and the current KOMODO request failed. Preserve it as an unresolved assertion, not a validated growth optimum.", "source_stage": "source-specific pH", "sources": [{"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4", "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7", "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 23-23", "quote": "medium adjust pH to 6.8-7.0.", "quote_basis": "derivative text"}]}, {"quantity_id": "q41", "label": "Existing pH: pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521", "local_fields": [{"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml", "field_path": "ph_value", "stored": 7.0}], "decision": "unsupported", "rationale": "This local variant pH is not independently established by the available exact primary and the current KOMODO request failed. Preserve it as an unresolved assertion, not a validated growth optimum.", "source_stage": "source-specific pH", "sources": [{"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4", "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7", "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 23-23", "quote": "medium adjust pH to 6.8-7.0.", "quote_basis": "derivative text"}]}, {"quantity_id": "q42", "label": "Retained507a preparation 1", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "preparation_steps[0].description", "stored": "Dissolve ingredients except bicarbonate, yeast extract, vitamins and sulfide, then sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials to 30% of their volume and autoclave. Add yeast extract, vitamins (sterilized by filtration) and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas atmosphere and bicarbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture. After completing the medium adjust pH to 6.8 - 7.0."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "preparation_steps[0].description", "stored": "Dissolve ingredients except bicarbonate, yeast extract, vitamins and sulfide, then sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials to 30% of their volume and autoclave. Add yeast extract, vitamins (sterilized by filtration) and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas atmosphere and bicarbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture. After completing the medium adjust pH to 6.8 - 7.0."}], "decision": "evidence_only", "rationale": "Credit the complete retained literal source instructions. The third step belongs to SL-4 and must move with the stock. Sulfide is mentioned in preparation without a quantified507a table dose; retain that ambiguity and never borrow the 20 mL dose from 507. The 1 bar instruction is overpressure, not absolute pressure.", "source_stage": "507a main preparation", "sources": [{"evidence_id": "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79", "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d", "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 15-21", "quote": "1. Dissolve ingredients except bicarbonate, yeast extract, vitamins and sulfide, then\nsparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Dispense medium\nunder same gas atmosphere into anoxic Hungate-type tubes or serum vials to 30% of their\nvolume and autoclave. Add yeast extract, vitamins (sterilized by filtration) and sulfide from\nsterile anoxic stock solutions prepared under 100% N2 gas atmosphere and bicarbonate\nfrom a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture.\nAfter completing the medium adjust pH to 6.8 - 7.0.", "quote_basis": "derivative text"}]}, {"quantity_id": "q43", "label": "Retained507a preparation 2", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "preparation_steps[1].description", "stored": "Inoculated vessels are pressurized with sterile carbon monoxide gas to 1 bar overpressure."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "preparation_steps[1].description", "stored": "Inoculated vessels are pressurized with sterile carbon monoxide gas to 1 bar overpressure."}], "decision": "evidence_only", "rationale": "Credit the complete retained literal source instructions. The third step belongs to SL-4 and must move with the stock. Sulfide is mentioned in preparation without a quantified507a table dose; retain that ambiguity and never borrow the 20 mL dose from 507. The 1 bar instruction is overpressure, not absolute pressure.", "source_stage": "507a main preparation", "sources": [{"evidence_id": "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79", "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d", "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 22-23", "quote": "2. Inoculated vessels are pressurized with sterile carbon monoxide gas to 1 bar\noverpressure.", "quote_basis": "derivative text"}]}, {"quantity_id": "q44", "label": "Retained507a preparation 3", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path": "preparation_steps[2].description", "stored": "First dissolve EDTA in distilled water and adjust pH to 7.0 using 2 N NaOH; then add other compounds."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path": "preparation_steps[2].description", "stored": "First dissolve EDTA in distilled water and adjust pH to 7.0 using 2 N NaOH; then add other compounds."}], "decision": "correct", "rationale": "Credit the complete retained literal source instructions. The third step belongs to SL-4 and must move with the stock. Sulfide is mentioned in preparation without a quantified507a table dose; retain that ambiguity and never borrow the 20 mL dose from 507. The 1 bar instruction is overpressure, not absolute pressure.", "source_stage": "SL-4 stock preparation", "sources": [{"evidence_id": "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79", "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d", "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 40-41", "quote": "First dissolve EDTA in distilled water and adjust pH to 7.0 using 2 N NaOH; then add other\ncompounds.", "quote_basis": "derivative text"}]}, {"quantity_id": "q45", "label": "507a SL-4 addition", "local_fields": [], "decision": "evidence_only", "rationale": "The printed source batch volume is missing structurally. Restore its exact stage and unit without deriving a measured final volume or per-litre dose.", "source_stage": "507a receiving batch", "sources": [{"evidence_id": "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79", "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d", "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 9-9", "quote": "Trace element solution SL-4                          10.00           ml", "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a", "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[0].recipe[6]", "quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Trace element solution SL-4\",\n                        \"solution_id\": 20,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}]}, {"quantity_id": "q46", "label": "507a Vitamin addition", "local_fields": [], "decision": "evidence_only", "rationale": "The printed source batch volume is missing structurally. Restore its exact stage and unit without deriving a measured final volume or per-litre dose.", "source_stage": "507a receiving batch", "sources": [{"evidence_id": "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79", "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d", "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 12-12", "quote": "Wolin's vitamin solution (10x)                        1.00           ml", "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a", "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[0].recipe[9]", "quote": "{\n                        \"recipe_order\": 10,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}]}, {"quantity_id": "q47", "label": "507a Main water input", "local_fields": [], "decision": "evidence_only", "rationale": "The printed source batch volume is missing structurally. Restore its exact stage and unit without deriving a measured final volume or per-litre dose.", "source_stage": "507a receiving batch", "sources": [{"evidence_id": "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79", "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d", "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 13-13", "quote": "Distilled water                                    1000.00           ml", "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a", "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[0].recipe[10]", "quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}]}, {"quantity_id": "q48", "label": "507a stock water 1", "local_fields": [], "decision": "evidence_only", "rationale": "The source states 1000 mL water input for this stock; its provider-declared rate is distinct from a measured final volume. SL-4 has a pH adjustment but no explicit final-makeup sentence.", "source_stage": "507a stock solvent", "sources": [{"evidence_id": "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79", "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d", "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 38-38", "quote": "Distilled water                                       1000.00        ml", "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a", "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[1].recipe[9]", "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}]}, {"quantity_id": "q49", "label": "507a stock water 2", "local_fields": [], "decision": "evidence_only", "rationale": "The source states 1000 mL water input for this stock; its provider-declared rate is distinct from a measured final volume. SL-4 has a pH adjustment but no explicit final-makeup sentence.", "source_stage": "507a stock solvent", "sources": [{"evidence_id": "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79", "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d", "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 65-65", "quote": "Distilled water                      1000.00   ml", "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a", "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[2].recipe[10]", "quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}]}, {"quantity_id": "q50", "label": "507 comparator SL-11 addition", "local_fields": [], "decision": "evidence_only", "rationale": "This belongs only to the separately identified 507 base source and is retained for identity/representation reconciliation. It is not a missing507a quantity and does not establish a complete unavailable KOMODO variant.", "source_stage": "507-only source comparison", "sources": [{"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4", "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7", "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 8-8", "quote": "Trace element solution SL-11                             1.00        ml", "quote_basis": "derivative text"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507", "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[0].recipe[5]", "quote": "{\n                        \"recipe_order\": 6,\n                        \"solution\": \"Trace element solution SL-11\",\n                        \"solution_id\": 1474,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}]}, {"quantity_id": "q51", "label": "507 comparator Resazurin stock addition", "local_fields": [], "decision": "evidence_only", "rationale": "This belongs only to the separately identified 507 base source and is retained for identity/representation reconciliation. It is not a missing507a quantity and does not establish a complete unavailable KOMODO variant.", "source_stage": "507-only source comparison", "sources": [{"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4", "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7", "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 9-9", "quote": "Sodium resazurin (0.1% w/v)                              0.50        ml", "quote_basis": "derivative text"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507", "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[0].recipe[6]", "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.000489237,\n                        \"mmol_l\": 0.00194783,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}]}, {"quantity_id": "q52", "label": "507 comparator Vitamin addition", "local_fields": [], "decision": "evidence_only", "rationale": "This belongs only to the separately identified 507 base source and is retained for identity/representation reconciliation. It is not a missing507a quantity and does not establish a complete unavailable KOMODO variant.", "source_stage": "507-only source comparison", "sources": [{"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4", "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7", "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 12-12", "quote": "Wolin's vitamin solution (10x)                           1.00        ml", "quote_basis": "derivative text"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507", "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[0].recipe[9]", "quote": "{\n                        \"recipe_order\": 10,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}]}, {"quantity_id": "q53", "label": "507 comparator Sulfide addition", "local_fields": [], "decision": "evidence_only", "rationale": "This belongs only to the separately identified 507 base source and is retained for identity/representation reconciliation. It is not a missing507a quantity and does not establish a complete unavailable KOMODO variant.", "source_stage": "507-only source comparison", "sources": [{"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4", "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7", "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 13-13", "quote": "Neutralized sulfide solution 3% (w/v)                   20.00        ml", "quote_basis": "derivative text"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507", "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[0].recipe[10]", "quote": "{\n                        \"recipe_order\": 11,\n                        \"solution\": \"Neutralized sulfide solution 3% (w/v)\",\n                        \"solution_id\": 34,\n                        \"amount\": 20,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}]}, {"quantity_id": "q54", "label": "507 comparator Main water", "local_fields": [], "decision": "evidence_only", "rationale": "This belongs only to the separately identified 507 base source and is retained for identity/representation reconciliation. It is not a missing507a quantity and does not establish a complete unavailable KOMODO variant.", "source_stage": "507-only source comparison", "sources": [{"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4", "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7", "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 14-14", "quote": "Distilled water                                       1000.00        ml", "quote_basis": "derivative text"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507", "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[0].recipe[11]", "quote": "{\n                        \"recipe_order\": 13,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}]}, {"quantity_id": "q55", "label": "507 comparator SL-11 water", "local_fields": [], "decision": "evidence_only", "rationale": "Retain this exact stock amount and source stage only. The sulfide 3% w/v strength is explicit; its preparation-water input is not measured receiving volume. No transfer into 507a is justified.", "source_stage": "507-only stock comparison", "sources": [{"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4", "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7", "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 61-61", "quote": "Distilled water                                       1000.00      ml", "quote_basis": "derivative text"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507", "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[1].recipe[9]", "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}]}, {"quantity_id": "q56", "label": "507 comparator Vitamin water", "local_fields": [], "decision": "evidence_only", "rationale": "Retain this exact stock amount and source stage only. The sulfide 3% w/v strength is explicit; its preparation-water input is not measured receiving volume. No transfer into 507a is justified.", "source_stage": "507-only stock comparison", "sources": [{"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4", "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7", "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 80-80", "quote": "Distilled water                                       1000.00      ml", "quote_basis": "derivative text"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507", "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[2].recipe[10]", "quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}]}, {"quantity_id": "q57", "label": "507 comparator Sulfide solute", "local_fields": [], "decision": "evidence_only", "rationale": "Retain this exact stock amount and source stage only. The sulfide 3% w/v strength is explicit; its preparation-water input is not measured receiving volume. No transfer into 507a is justified.", "source_stage": "507-only stock comparison", "sources": [{"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4", "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7", "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 85-85", "quote": "Na2S x 9 H2O                                             3.00        g", "quote_basis": "derivative text"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507", "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[3].recipe[0]", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 30,\n                        \"mmol_l\": 124.905,\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}]}, {"quantity_id": "q58", "label": "507 comparator Sulfide water", "local_fields": [], "decision": "evidence_only", "rationale": "Retain this exact stock amount and source stage only. The sulfide 3% w/v strength is explicit; its preparation-water input is not measured receiving volume. No transfer into 507a is justified.", "source_stage": "507-only stock comparison", "sources": [{"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4", "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7", "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 86-86", "quote": "Distilled water                                        100.00       ml", "quote_basis": "derivative text"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507", "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[3].recipe[1]", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 100,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_basis": "raw UTF-8"}]}, {"quantity_id": "q59", "label": "507 main preparation", "local_fields": [], "decision": "evidence_only", "rationale": "This source-only process or named override remains tied to 507. Preserve explicit strengths, amounts, gas composition, vessel fraction, time, temperature and overpressure separately; unquantified titrant doses remain unknown. An identity lead is not a verified complete formulation for the unavailable KOMODO variants.", "source_stage": "507-specific preparation/variant", "sources": [{"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4", "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7", "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 16-25", "quote": "1. Dissolve ingredients except bicarbonate, yeast extract, vitamins and sulfide, then\nsparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Dispense medium\nunder same gas atmosphere into anoxic Hungate-type tubes or serum vials to 30% of their\nvolume and autoclave. Add yeast extract, vitamins (sterilized by filtration) and sulfide from\nsterile anoxic stock solutions prepared under 100% N2 gas atmosphere and bicarbonate\nfrom a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture.\nNeutralize the sodium sulfide with sterile H2SO4 (see medium 29). After completing the\nmedium adjust pH to 6.8-7.0.\n2. Inoculated vessels are pressurized with sterile carbon monoxide gas to 2 bar\noverpressure.", "quote_basis": "derivative text"}]}, {"quantity_id": "q60", "label": "507 SL-11 makeup", "local_fields": [], "decision": "evidence_only", "rationale": "This source-only process or named override remains tied to 507. Preserve explicit strengths, amounts, gas composition, vessel fraction, time, temperature and overpressure separately; unquantified titrant doses remain unknown. An identity lead is not a verified complete formulation for the unavailable KOMODO variants.", "source_stage": "507-specific preparation/variant", "sources": [{"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4", "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7", "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 63-65", "quote": "Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.", "quote_basis": "derivative text"}]}, {"quantity_id": "q61", "label": "507 sulfide preparation", "local_fields": [], "decision": "evidence_only", "rationale": "This source-only process or named override remains tied to 507. Preserve explicit strengths, amounts, gas composition, vessel fraction, time, temperature and overpressure separately; unquantified titrant doses remain unknown. An identity lead is not a verified complete formulation for the unavailable KOMODO variants.", "source_stage": "507-specific preparation/variant", "sources": [{"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4", "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7", "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 88-92", "quote": "The sulfide solution is prepared in a 250 ml screw-capped bottle with a butyl rubber\nseptum and a magnetic stirrer. The solution is bubbled with nitrogen gas, closed and\nautoclaved for 15 min. at 121°C. After cooling to room temperature the pH is adjusted to\nabout 7.0 by adding of sterile 2 M H2SO4 drop-wise with a syringe without opening the\nbottle.", "quote_basis": "derivative text"}]}, {"quantity_id": "q62", "label": "DSM12326 supplement", "local_fields": [], "decision": "evidence_only", "rationale": "This source-only process or named override remains tied to 507. Preserve explicit strengths, amounts, gas composition, vessel fraction, time, temperature and overpressure separately; unquantified titrant doses remain unknown. An identity lead is not a verified complete formulation for the unavailable KOMODO variants.", "source_stage": "507-specific preparation/variant", "sources": [{"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4", "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7", "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 28-29", "quote": "For DSM 12326: Supplement medium with 1.00 ml/l selenite-tungstate solution (see\nmedium 385).", "quote_basis": "derivative text"}]}, {"quantity_id": "q63", "label": "DSM19011 override", "local_fields": [], "decision": "evidence_only", "rationale": "This source-only process or named override remains tied to 507. Preserve explicit strengths, amounts, gas composition, vessel fraction, time, temperature and overpressure separately; unquantified titrant doses remain unknown. An identity lead is not a verified complete formulation for the unavailable KOMODO variants.", "source_stage": "507-specific preparation/variant", "sources": [{"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4", "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7", "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 30-31", "quote": "For DSM 19011: Supplement medium with 0.20 g/l Na-lactate. Change gas phase to 100%\ncarbon monoxide prior to inoculation, but do not use excess pressure.", "quote_basis": "derivative text"}]}, {"quantity_id": "q64", "label": "DSM21830 pH override", "local_fields": [], "decision": "evidence_only", "rationale": "This source-only process or named override remains tied to 507. Preserve explicit strengths, amounts, gas composition, vessel fraction, time, temperature and overpressure separately; unquantified titrant doses remain unknown. An identity lead is not a verified complete formulation for the unavailable KOMODO variants.", "source_stage": "507-specific preparation/variant", "sources": [{"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4", "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7", "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 32-32", "quote": "For DSM 21830: Adjust pH of complete medium to 6.0.", "quote_basis": "derivative text"}]}, {"quantity_id": "q65", "label": "DSM22663 override", "local_fields": [], "decision": "evidence_only", "rationale": "This source-only process or named override remains tied to 507. Preserve explicit strengths, amounts, gas composition, vessel fraction, time, temperature and overpressure separately; unquantified titrant doses remain unknown. An identity lead is not a verified complete formulation for the unavailable KOMODO variants.", "source_stage": "507-specific preparation/variant", "sources": [{"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4", "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7", "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 33-35", "quote": "For DSM 22663: Supplement medium with 10.00 g/l sulfur and increase amount of yeast\nextract to 1.00 g/l. Sulfur is sterilized separately by steaming for 3 h on each of three\nsuccessive days.", "quote_basis": "derivative text"}]}, {"quantity_id": "q66", "label": "DSM23698 override", "local_fields": [], "decision": "evidence_only", "rationale": "This source-only process or named override remains tied to 507. Preserve explicit strengths, amounts, gas composition, vessel fraction, time, temperature and overpressure separately; unquantified titrant doses remain unknown. An identity lead is not a verified complete formulation for the unavailable KOMODO variants.", "source_stage": "507-specific preparation/variant", "sources": [{"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf", "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4", "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7", "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 36-38", "quote": "For DSM 23698: Supplement medium with 2.00 g/l Na-pyruvate and omit sulfide. Adjust\nfinal pH of medium to 6.2. Change gas phase to 100% carbon monoxide prior to\ninoculation, but do not use excess pressure.", "quote_basis": "derivative text"}]}, {"quantity_id": "q67", "label": "Provider volumes", "local_fields": [], "decision": "evidence_only", "rationale": "The providers declare 1011 mL for507a and 1022 mL for507. These explain their rate normalizations; they are not measured final volumes and cannot justify exchanging formulations.", "source_stage": "provider normalization", "sources": [{"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a", "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7", "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "$.data.solutions[0].volume", "quote": "\"volume\": 1011", "quote_basis": "raw UTF-8"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507", "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48", "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "$.data.solutions[0].volume", "quote": "\"volume\": 1022", "quote_basis": "raw UTF-8"}]}], "document_scopes": {"data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml": null, "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml": null, "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml": null, "data/normalized_yaml/bacterial/for_dsm_12326.yaml": null, "data/normalized_yaml/bacterial/for_dsm_18923.yaml": null, "data/normalized_yaml/bacterial/for_dsm_21278.yaml": null, "data/normalized_yaml/bacterial/for_dsm_21830.yaml": null, "data/normalized_yaml/bacterial/for_dsm_23698.yaml": null, "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml": null, "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml": null}, "scope": "Every selected target/owner concentration plus explicit dependency fields; source-only rows/conditions and unchanged claims distinguished. Excluded parent quantities are not transferred."}

### Supplied forms and current ontology/MIM scope

grounding: concern. Targets: CultureMech:001640.

Every actual asserted CHEBI primary and secondary slot is joined to a fresh exact non-obsolete OLS object and current packaged MIM rows. Nickel has a confirmed hydrate mismatch. Source Na2-EDTA in SL-4 has no hydrate qualifier, so anhydrous specificity remains unproven. Generic biotin does not by itself establish stereochemistry; DL lipoic acid is compatible with the non-stereospecific object. Calcium D-pantothenate agrees with the D-configured 31345 object but lacks the secondary slot. The absent anthraquinone slot is not counted as a validated ontology object, and historical candidate 85112 is not newly certified.

### Existing repair credit and writer limits

provenance: concern. Targets: CultureMech:001640.

All twenty exact historical reports and all current target/owner histories were read using lossless duplicate-cell pooling. Of347 literal historical source objects, 339 equal current responses; eight old 507 sulfide rows omit the now-present g_l/mmol_l fields. Current 507a raw bytes exactly match the old declared digest, while the current 507 raw digest differs; equal decoded objects do not authenticate the original507 raw event. No current owner has attached concentration evidence. The September report correctly raised source distinctions but incorrectly treats1011 as measured final volume and states507a has no sulfide despite its preparation mention; those claims and automatic dilution/variant repair suggestions are not adopted. Current repair code is inspected as current implementation, not independent historical execution proof.

## Findings

### f1: Distinct 507 and 507a sources are asserted as duplicates

major / open / confirmed; issue key: culturemech-001640-source-duplicate.

The generated target combines nine owners and publishes reciprocal SOURCE_DUPLICATE assertions. Fresh primary sources distinguish507a anthraquinone/SL-4 from 507 SL-11/resazurin/sulfide, different yeast input and different CO overpressure. The local 27-row signature cannot establish source equivalence. Separate these source identities and recover each exact variant before regenerating; retain current conservative merger safeguards, which already compare scientific fields and reject incompatible formulations.

### f2: Nineteen stock ingredients remain flattened into the main recipe

major / open / confirmed; issue key: culturemech-001640-stock-topology.

For the exact 507a target/owner, nine SL-4 and ten vitamin components are encoded at stock strengths in main ingredients. Restore the two stock identities and printed batch additions, their separate water inputs and literal amount evidence. Preserve the supported main API rates on their declared basis. The copied KOMODO amounts require their own source reconciliation and are not repaired by applying507a to every owner.

### f3: Variant-specific quantities and atmosphere metadata are not represented reliably

major / open / confirmed; issue key: culturemech-001640-variant-controls.

The exact base507 source specifies a DSM12326 supplement and distinct DSM21830/23698 overrides, while the corresponding local wrappers retain the copied507a matrix. Other variant formulations remain unavailable behind 403 responses. Aerobic:Yes notes conflict with the linked base source anoxic preparation and require source-specific correction; do not infer new organism-growth claims. Credit existing pH values that match named source overrides without endorsing entire variants. Preserve507a preparation and its unquantified sulfide ambiguity.

### f4: The supplied nickel hexahydrate has an anhydrous ontology identity

major / open / confirmed; issue key: culturemech-001640-nickel-form.

All ten copies assert CHEBI:34887 in primary and secondary nickel slots despite supplied NiCl2·6H2O. The fresh 53542 object identifies nickel dichloride hexahydrate. Correct actual supplied-form assertions while keeping unresolved variant formulation identity separate. Canonical label agreement and current MIM membership do not certify hydration.

### f5: The topology repair writer preserves the unsupported duplicate assumption

major / open / confirmed; issue key: culturemech-001640-repair-writer.

Current repair_komodo_507_carboxydothermus_score10.py hardcodes the shared 27-row signature and SOURCE_DUPLICATE graph. Its matching-event replacement uses a fixed historical timestamp. Correct the maintained evidence and writer assumptions with a genuinely new append-only event; do not blindly rerun it or rewrite old history as though this new review occurred then. An ingredients_curated flag is not source authentication.

### f6: Two existing descriptors need bounded grounding follow-up

minor / open / confirmed; issue key: culturemech-001640-missing-grounding.

Anthraquinone disulfonate has no primary or secondary ontology slot, and calcium D-pantothenate lacks its secondary linkage. The exact source compound identity is present, but the old report candidate 85112 is not freshly authenticated in this review; resolve the exact disodium form before adopting it. Existing 31345 agrees with the source D-configured pantothenate and current index.

## Recommended Actions And Acceptance Checks

### a1

The generated target combines nine owners and publishes reciprocal SOURCE_DUPLICATE assertions. Fresh primary sources distinguish507a anthraquinone/SL-4 from 507 SL-11/resazurin/sulfide, different yeast input and different CO overpressure. The local 27-row signature cannot establish source equivalence. Separate these source identities and recover each exact variant before regenerating; retain current conservative merger safeguards, which already compare scientific fields and reject incompatible formulations.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a2

For the exact 507a target/owner, nine SL-4 and ten vitamin components are encoded at stock strengths in main ingredients. Restore the two stock identities and printed batch additions, their separate water inputs and literal amount evidence. Preserve the supported main API rates on their declared basis. The copied KOMODO amounts require their own source reconciliation and are not repaired by applying507a to every owner.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a3

The exact base507 source specifies a DSM12326 supplement and distinct DSM21830/23698 overrides, while the corresponding local wrappers retain the copied507a matrix. Other variant formulations remain unavailable behind 403 responses. Aerobic:Yes notes conflict with the linked base source anoxic preparation and require source-specific correction; do not infer new organism-growth claims. Credit existing pH values that match named source overrides without endorsing entire variants. Preserve507a preparation and its unquantified sulfide ambiguity.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a4

All ten copies assert CHEBI:34887 in primary and secondary nickel slots despite supplied NiCl2·6H2O. The fresh 53542 object identifies nickel dichloride hexahydrate. Correct actual supplied-form assertions while keeping unresolved variant formulation identity separate. Canonical label agreement and current MIM membership do not certify hydration.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a5

Current repair_komodo_507_carboxydothermus_score10.py hardcodes the shared 27-row signature and SOURCE_DUPLICATE graph. Its matching-event replacement uses a fixed historical timestamp. Correct the maintained evidence and writer assumptions with a genuinely new append-only event; do not blindly rerun it or rewrite old history as though this new review occurred then. An ingredients_curated flag is not source authentication.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a6

Anthraquinone disulfonate has no primary or secondary ontology slot, and calcium D-pantothenate lacks its secondary linkage. The exact source compound identity is present, but the old report candidate 85112 is not freshly authenticated in this review; resolve the exact disodium form before adopting it. Existing 31345 agrees with the source D-configured pantothenate and current index.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| dsm507a | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf; REVIEW_WORK/batch059/source07-09/dsm507a.json; exact original raw/text/hash/time metadata | context_only | Exact primary medium and its printed stock/preparation subsections; named strain variations remain separate and do not establish generic growth. |
| api507a | https://mediadive.dsmz.de/rest/medium/507a; REVIEW_WORK/batch059/source07-09/api507a.json; exact original raw/text/hash/time metadata | context_only | Exact current provider identity and declared amounts/basis; provider volume is not independently measured final volume. |
| dsm507 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf; REVIEW_WORK/batch059/source07-09/dsm507.json; exact original raw/text/hash/time metadata | context_only | Exact primary medium and its printed stock/preparation subsections; named strain variations remain separate and do not establish generic growth. |
| api507 | https://mediadive.dsmz.de/rest/medium/507; REVIEW_WORK/batch059/source07-09/api507.json; exact original raw/text/hash/time metadata | context_only | Exact current provider identity and declared amounts/basis; provider volume is not independently measured final volume. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:34887; REVIEW_WORK/batch059/source07-09/chebi34887.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi53542 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53542; REVIEW_WORK/batch059/source07-09/chebi53542.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi64734 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:64734; REVIEW_WORK/batch059/source07-09/chebi64734.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15956; REVIEW_WORK/batch059/source07-09/chebi15956.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31345; REVIEW_WORK/batch059/source07-09/chebi31345.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:16494; REVIEW_WORK/batch059/source07-09/chebi16494.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| komodo507 | https://komodo.modelseed.org/servlet/Komodo?getRecipe=507; REVIEW_WORK/batch059/source07-09/komodo507.json; exact original raw/text/hash/time metadata | context_only | Earlier guessed KOMODO getRecipe route returned HTTP 403. This is an unsuccessful discovery lead, not authentication of the exact historical source route; subsequent exact MediaInfo attempts are separately retained. |
| komodo507.1 | https://komodo.modelseed.org/servlet/Komodo?getRecipe=507.1; REVIEW_WORK/batch059/source07-09/komodo507.1.json; exact original raw/text/hash/time metadata | context_only | Earlier guessed KOMODO getRecipe route returned HTTP 403. This is an unsuccessful discovery lead, not authentication of the exact historical source route; subsequent exact MediaInfo attempts are separately retained. |
| komodo507.2 | https://komodo.modelseed.org/servlet/Komodo?getRecipe=507.2; REVIEW_WORK/batch059/source07-09/komodo507.2.json; exact original raw/text/hash/time metadata | context_only | Earlier guessed KOMODO getRecipe route returned HTTP 403. This is an unsuccessful discovery lead, not authentication of the exact historical source route; subsequent exact MediaInfo attempts are separately retained. |
| komodo507.3 | https://komodo.modelseed.org/servlet/Komodo?getRecipe=507.3; REVIEW_WORK/batch059/source07-09/komodo507.3.json; exact original raw/text/hash/time metadata | context_only | Earlier guessed KOMODO getRecipe route returned HTTP 403. This is an unsuccessful discovery lead, not authentication of the exact historical source route; subsequent exact MediaInfo attempts are separately retained. |
| komodo507.4 | https://komodo.modelseed.org/servlet/Komodo?getRecipe=507.4; REVIEW_WORK/batch059/source07-09/komodo507.4.json; exact original raw/text/hash/time metadata | context_only | Earlier guessed KOMODO getRecipe route returned HTTP 403. This is an unsuccessful discovery lead, not authentication of the exact historical source route; subsequent exact MediaInfo attempts are separately retained. |
| komodo507.5 | https://komodo.modelseed.org/servlet/Komodo?getRecipe=507.5; REVIEW_WORK/batch059/source07-09/komodo507.5.json; exact original raw/text/hash/time metadata | context_only | Earlier guessed KOMODO getRecipe route returned HTTP 403. This is an unsuccessful discovery lead, not authentication of the exact historical source route; subsequent exact MediaInfo attempts are separately retained. |
| komodo507.7 | https://komodo.modelseed.org/servlet/Komodo?getRecipe=507.7; REVIEW_WORK/batch059/source07-09/komodo507.7.json; exact original raw/text/hash/time metadata | context_only | Earlier guessed KOMODO getRecipe route returned HTTP 403. This is an unsuccessful discovery lead, not authentication of the exact historical source route; subsequent exact MediaInfo attempts are separately retained. |
| komodo507_7242 | https://komodo.modelseed.org/servlet/Komodo?getRecipe=507_7242; REVIEW_WORK/batch059/source07-09/komodo507_7242.json; exact original raw/text/hash/time metadata | context_only | Earlier guessed KOMODO getRecipe route returned HTTP 403. This is an unsuccessful discovery lead, not authentication of the exact historical source route; subsequent exact MediaInfo attempts are separately retained. |
| target | data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml; Complete file | context_only | Complete generated target. |
| owner | data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml; Complete file | context_only | Complete exact maintained owner. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete file | context_only | Exact packaged current identifier/ontology_id and preferred-term rows. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Complete file | context_only | Exact packaged snapshot version and checksum. |
| writer-formulation | src/culturemech/merge/formulation.py; Full formulation comparison | context_only | Current scientific-field equality includes quantities, stocks and notes; no chemical equivalence is inferred. |
| writer-merger | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | Current merge_group copies singletons and rejects incompatible multiple formulations. Generated staleness is not evidence that current code permits ingredient-only merging. |
| owner-2 | data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml; Complete file | context_only | Complete exact additional maintained owner. |
| owner-3 | data/normalized_yaml/bacterial/for_dsm_12326.yaml; Complete file | context_only | Complete exact additional maintained owner. |
| owner-4 | data/normalized_yaml/bacterial/for_dsm_18923.yaml; Complete file | context_only | Complete exact additional maintained owner. |
| owner-5 | data/normalized_yaml/bacterial/for_dsm_21278.yaml; Complete file | context_only | Complete exact additional maintained owner. |
| owner-6 | data/normalized_yaml/bacterial/for_dsm_21830.yaml; Complete file | context_only | Complete exact additional maintained owner. |
| owner-7 | data/normalized_yaml/bacterial/for_dsm_23698.yaml; Complete file | context_only | Complete exact additional maintained owner. |
| owner-8 | data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml; Complete file | context_only | Complete exact additional maintained owner. |
| owner-9 | data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml; Complete file | context_only | Complete exact additional maintained owner. |
| report-24 | reports/ingredient_concentration_curation/20261007-komodo-media-1500-2000/inspected-candidate-context.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-25 | reports/ingredient_concentration_curation/20261007-komodo-media-1500-2000/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-26 | reports/ingredient_concentration_curation/20261007-komodo-media-1500-2000/records/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-27 | reports/ingredient_concentration_curation/20261007-komodo-media-1500-2000/records/bacterial/for_dsm_12326.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-28 | reports/ingredient_concentration_curation/20261007-komodo-media-1500-2000/records/bacterial/for_dsm_18923.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-29 | reports/ingredient_concentration_curation/20261007-komodo-media-1500-2000/records/bacterial/for_dsm_21278.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-30 | reports/ingredient_concentration_curation/20261007-komodo-media-1500-2000/records/bacterial/for_dsm_21830.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-31 | reports/ingredient_concentration_curation/20261007-komodo-media-1500-2000/records/bacterial/for_dsm_23698.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-32 | reports/ingredient_concentration_curation/20261007-komodo-media-1500-2000/records/bacterial/medium_507_modified_for_dsm_7242.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-33 | reports/ingredient_concentration_curation/20261007-komodo-media-1500-2000/records/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-34 | reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-35 | reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/carboxydothermus_siderophilus_medium.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-36 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-37 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-38 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-39 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_12326.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-40 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_18923.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-41 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_21278.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-42 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_21830.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-43 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_23698.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-44 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-45 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-46 | reports/yaml_record_review/20260922T041153Z-CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition, _is_api_stock_addition, _parse_api_solutions, _normalize_unit | context_only | Current parser reads only the primary recipe, separates referenced solutions and percentage/ml additions, and preserves their source attributes. It prefers explicit g_l but otherwise maps bare mass/volume units to per-litre schema units. This credits existing stage handling without certifying a source final volume or historical execution. |
| writer-cleanup | scripts/cleanup_media_quality.py; _merge_ingredient_group | context_only | Current duplicate cleanup collapses identical values but flags conflicting values without summing. Earlier sums require source-stage curation; do not rerun cleanup as a substitute for scientific reconciliation. |
| historical-reading | REVIEW_WORK/batch059/record09/historical-reading.json; Complete report cell pool and exact current-source object joins | context_only | Complete report text read through exact duplicate pooling; old conclusions separately assessed. |
| writer-507 | scripts/repair_komodo_507_carboxydothermus_score10.py; Complete file, ingredient_signature, variant constants and _upsert_event | context_only | Current code hardcodes the27-row507a-like ingredient signature, SOURCE_DUPLICATE classification and variant graph. Its _upsert_event replaces a matching curator/action event with a fixed historical timestamp. These current assumptions need correction; do not blindly rerun this writer as append-only curation. Current code does not prove a past execution. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32588; REVIEW_WORK/batch059/source07-09/chebi32588.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86345; REVIEW_WORK/batch059/source07-09/chebi86345.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86158; REVIEW_WORK/batch059/source07-09/chebi86158.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31206; REVIEW_WORK/batch059/source07-09/chebi31206.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63036; REVIEW_WORK/batch059/source07-09/chebi63036.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32139; REVIEW_WORK/batch059/source07-09/chebi32139.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75836; REVIEW_WORK/batch059/source07-09/chebi75836.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32312; REVIEW_WORK/batch059/source07-09/chebi32312.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86368; REVIEW_WORK/batch059/source07-09/chebi86368.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:33118; REVIEW_WORK/batch059/source07-09/chebi33118.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53503; REVIEW_WORK/batch059/source07-09/chebi53503.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86318; REVIEW_WORK/batch059/source07-09/chebi86318.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75213; REVIEW_WORK/batch059/source07-09/chebi75213.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:27470; REVIEW_WORK/batch059/source07-09/chebi27470.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30961; REVIEW_WORK/batch059/source07-09/chebi30961.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49105; REVIEW_WORK/batch059/source07-09/chebi49105.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17015; REVIEW_WORK/batch059/source07-09/chebi17015.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15940; REVIEW_WORK/batch059/source07-09/chebi15940.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:176843; REVIEW_WORK/batch059/source07-09/chebi176843.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30753; REVIEW_WORK/batch059/source07-09/chebi30753.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| quantities | REVIEW_WORK/batch059/record09/quantity-inventory.json; Complete sidecar | supports | Complete source-stage quantity decisions. |
| groundings | REVIEW_WORK/batch059/record09/grounding-inventory.json; Complete sidecar | supports | Exact slots, raw OLS scientific objects and current MIM rows. |
| census | REVIEW_WORK/batch059/record09/field-census.json; Complete sidecar | supports | Complete scalar census with explicit dependency exclusions. |
| numeric-census | REVIEW_WORK/batch059/record09/numeric-field-census.json; Complete sidecar | supports | Numeric/text assertions and quantity joins. |
| history | REVIEW_WORK/batch059/record09/history-inventory.json; Complete sidecar | supports | Current exact histories, without replay. |
| old-reports | REVIEW_WORK/batch059/record09/history-report-inventory.json; Complete sidecar | supports | Exact historical report scopes. |
| old-claims | REVIEW_WORK/batch059/record09/existing-claim-authentication.json; Complete sidecar | supports | Existing literal and raw-digest matches; current content authentication is separate from original retrieval provenance. |
| check-schema | REVIEW_WORK/batch059/record09/schema-result.json | supports | Original once-only canonical schema with complete argv/time/streams; reference count zero does not verify sources. |
| check-strict | REVIEW_WORK/batch059/record09/strict-result.json | supports | Original once-only canonical strict with complete argv/time/streams; reference count zero does not verify sources. |
| check-terms | REVIEW_WORK/batch059/record09/terms-result.json | supports | Original once-only canonical terms with complete argv/time/streams; reference count zero does not verify sources. |
| check-references | REVIEW_WORK/batch059/record09/references-result.json | supports | Original once-only canonical references with complete argv/time/streams; reference count zero does not verify sources. |
| komodo-exact-1 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=507; REVIEW_WORK/batch059/record09-peer-exact-routes-20261028T071852Z/result.json $.outcomes[0]; historical discovery $.unique_cells[263] | context_only | Exact historical MediaInfo hyperlink attempted once; HTTP 403 challenge. No current formulation or historical access-time authentication follows. |
| komodo-exact-2 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=507.2; REVIEW_WORK/batch059/record09-peer-exact-routes-20261028T071852Z/result.json $.outcomes[1]; historical discovery $.unique_cells[282] | context_only | Exact historical MediaInfo hyperlink attempted once; HTTP 403 challenge. No current formulation or historical access-time authentication follows. |
| komodo-exact-3 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=507.3; REVIEW_WORK/batch059/record09-peer-exact-routes-20261028T071852Z/result.json $.outcomes[2]; historical discovery $.unique_cells[291] | context_only | Exact historical MediaInfo hyperlink attempted once; HTTP 403 challenge. No current formulation or historical access-time authentication follows. |
| komodo-exact-4 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=507.4; REVIEW_WORK/batch059/record09-peer-exact-routes-20261028T071852Z/result.json $.outcomes[3]; historical discovery $.unique_cells[300] | context_only | Exact historical MediaInfo hyperlink attempted once; HTTP 403 challenge. No current formulation or historical access-time authentication follows. |
| komodo-exact-5 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=507.5; REVIEW_WORK/batch059/record09-peer-exact-routes-20261028T071852Z/result.json $.outcomes[4]; historical discovery $.unique_cells[309] | context_only | Exact historical MediaInfo hyperlink attempted once; HTTP 403 challenge. No current formulation or historical access-time authentication follows. |
| komodo-exact-6 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=507.7; REVIEW_WORK/batch059/record09-peer-exact-routes-20261028T071852Z/result.json $.outcomes[5]; historical discovery $.unique_cells[319] | context_only | Exact historical MediaInfo hyperlink attempted once; HTTP 403 challenge. No current formulation or historical access-time authentication follows. |
| komodo-exact-7 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=507_7242; REVIEW_WORK/batch059/record09-peer-exact-routes-20261028T071852Z/result.json $.outcomes[6]; historical discovery $.unique_cells[329] | context_only | Exact historical MediaInfo hyperlink attempted once; HTTP 403 challenge. No current formulation or historical access-time authentication follows. |
| komodo-exact-8 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=507.1; REVIEW_WORK/batch059/record09-peer-exact-routes-20261028T071852Z/result.json $.outcomes[7]; historical discovery $.unique_cells[339] | context_only | Exact historical MediaInfo hyperlink attempted once; HTTP 403 challenge. No current formulation or historical access-time authentication follows. |
| komodo-exact-catalog | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; REVIEW_WORK/batch059/record01-root-exact-routes/komodo964-list.json; reused exact current failed capture with original access time | context_only | Exact historical MediaList route returned HTTP 403. Current failure is distinct from old catalog excerpts. |

## Limits And Additional Notes

- Current canonical checks validate encoded structure/labels; zero reference checks do not verify external source claims.
- All primary PDF pages were read visually as well as in their complete extracted text. Current source status, retrieval times and complete raw/text bytes remain in the capture catalog.
- Completion is partial because the eight exact historical KOMODO MediaInfo hyperlinks and exact MediaList route returned HTTP 403. Earlier getRecipe failures were guessed discovery leads and are retained separately. Full current-field coverage does not mean all variants are scientifically verified.
- The parent graph includes a separate DSM23132 child outside the selected nine owners. Its relationship assertion is read in the parent, but that separate YAML and its quantities are not assessed or modified.
- The older report mentions standalone main/SL-4/Wolin records outside this selected input scope. No new current defect is asserted for those uninspected standalone records.
- 507a preparation mentions sulfide but supplies no stock dose in its table or API. This remains unresolved; the 20 mL addition and 3% stock from 507 are not transferred.
- Historical imported timestamps with malformed .fZ or absent time zones are retained provenance, not used as new review access times. Native diagnostics passing do not certify every old timestamp or historical scientific assertion.
- No strain-growth claim, optimization or experimental recommendation is inferred from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed only on their declared normalization basis; unspecified percent bases and hydrate numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T072114Z-batch059-record09-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Scientific review: CARBOXYDOTHERMUS SIDEROPHILUS MEDIUM'
started_at: '2026-10-28T06:51:20.826468Z'
finished_at: '2026-10-28T07:21:14.364325Z'
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
summary: The exact507a formulation and preparation are distinguishable from507. Correct
  the unsupported duplicate graph, stock flattening and nickel form; preserve unresolved
  variant formulas, source ambiguities and historical version boundaries.
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
  - path: data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml
    sha256: cd8c09e29dbb71a965afd4c18114e124dfe8025d83bb0690423f4777fb627211
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml
    sha256: 8bc1c4982db978a9dc25662937e53a24665d2c60302b80bb58fabd37ab3b4a5a
    role: context
  - path: data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml
    sha256: f003bb781f43232ba7cdf9ae5c2477be7860913a93f84c44b38e4f97e9b59da9
    role: context
  - path: data/normalized_yaml/bacterial/for_dsm_12326.yaml
    sha256: 75e15e8ef624d170acd18d85d2fbba8409611e241e61bb431895b661f901310a
    role: context
  - path: data/normalized_yaml/bacterial/for_dsm_18923.yaml
    sha256: b14bbf6df3e3e316cb6ae65c211a68929f6be80de42c158f7d2e2597bfd02526
    role: context
  - path: data/normalized_yaml/bacterial/for_dsm_21278.yaml
    sha256: a862a1226bea719aab2a952bdc2d96d6cbbaff051df7dc0368198d9d9f5d8881
    role: context
  - path: data/normalized_yaml/bacterial/for_dsm_21830.yaml
    sha256: 3e24cacb3865c1c3f6f174bac026eafcf5a936512749fd6614d6e131ccebae34
    role: context
  - path: data/normalized_yaml/bacterial/for_dsm_23698.yaml
    sha256: a810f79c39b25b73642c867b70cd5fc93d4b1cf68b0091ee67eb0fe2612d660b
    role: context
  - path: data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml
    sha256: cbed41f17007c7cf46338f50380d5ed4860074bbaa63053879d45c6ac11279d9
    role: context
  - path: data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml
    sha256: ae3a128915194898b4ad4986d1ff597439bcc0083ba7f3def873d3cb74419044
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
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-1500-2000/inspected-candidate-context.json
    sha256: 20c95f15dfdb08b3e7019d784339ef66641789e40579c7c51f9396092b007fba
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-1500-2000/plan.json
    sha256: 56e72694e73e28cee3666277d0f215973f770da991b4b42930105ec89d0ab6e3
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-1500-2000/records/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml.md
    sha256: 8000569bc2dde9595e866728637805559c124b4d3dc9cd67e2f08a39601969dd
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-1500-2000/records/bacterial/for_dsm_12326.yaml.md
    sha256: 647da9a31dedacdee4fc472314ef2349ac299f7e25dd9d197fd9f1dce89615f6
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-1500-2000/records/bacterial/for_dsm_18923.yaml.md
    sha256: b1b918dda4ffe61054b7beee22c2e08ec3eb9b97bc892b90f820d64c26bf1bf9
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-1500-2000/records/bacterial/for_dsm_21278.yaml.md
    sha256: 73e14d47bb12b7075e8cc8164ba7c8925080873911c67e2cf231ee9a03b257f4
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-1500-2000/records/bacterial/for_dsm_21830.yaml.md
    sha256: b04b8053efae35f64dd3762f2eda942a9f17c9df4826f4955352ddc7a69f2c9a
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-1500-2000/records/bacterial/for_dsm_23698.yaml.md
    sha256: 2b416b47dbc9f757598e34e7f39a7f1735ddba3577db4aed0f472571e467175d
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-1500-2000/records/bacterial/medium_507_modified_for_dsm_7242.yaml.md
    sha256: 5586daae5f3dc4ee9c93018afa606746d4ff3ef8c280f4933c47b3d54ae76283
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-1500-2000/records/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml.md
    sha256: 164d431dd11e2e25c0db211860c7a7fd604043c9890558ff5ecf24da7c6b0315
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/plan.json
    sha256: bc8c96d09770525e6b6ba6dc0c7680354cf9bc6baa5249e79e82b65328203147
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/carboxydothermus_siderophilus_medium.yaml.md
    sha256: eae5c21979264b496d93686f241806f3b67dbad811f8d5e8a3da8125bd92c92a
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.md
    sha256: f5fa9de661c4938a2548906fbc5c74e581cee77ef744846c6511aff5ec796572
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.md
    sha256: d76f54aea4a16f7b1741737df7f64588d336bc499fd2c0c73cfbb00d2c321396
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.md
    sha256: dea5e8f503f1d1c9b958e57b51096d7649e23e1873b8889944dcc9bb44ee51d1
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_12326.md
    sha256: 92d2d5079dff869ecf34424390f397e685d6302d74411babc8df0776f23bd7d0
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_18923.md
    sha256: 794af8c36f8ad212d39ff61f90c05fe4515ab8f827a0e1260cab42f1ff330f5d
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_21278.md
    sha256: 5bf8544f23ed749aa7fcf29827e866159fba7fcdb9aa21d40584060633c12464
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_21830.md
    sha256: 1c5f0a642b11c70c661e6eca3fa2a9a6df1473e5d777eeb0cecaab0647f104b8
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_23698.md
    sha256: a417735c51bd73b6e8177c4cc6022a1067cea875b5bd4fddd880b1cc055c1f3f
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.md
    sha256: 453010b6bf11ec5651e59352a315a04671a9799916658229db4335386200a8a4
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.md
    sha256: c07dc55e92ef67cf776da34ef31840a5d6cdcda589401f2159fee065e5d173fc
    role: context
  - path: reports/yaml_record_review/20260922T041153Z-CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.md
    sha256: b7a8481b6a767f31ea8b75dc169c87f1e561f31c9df9a1bd41e46471071c3ae1
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
  - path: scripts/promote_komodo_volume_candidates.py
    sha256: 2423b7e2e04011b31d21eac939714a2db4380f033a69094325dc567e44929cd2
    role: context
  - path: scripts/refill_term_labels.py
    sha256: 8eee4532e4a71d120532db511733bde974ab1b179e50cb1ea51d66c3870f3cb9
    role: context
  - path: scripts/remove_invalid_chebi_ids.py
    sha256: a6c2f7577812081230fd5fe008182c09eace4ef7818857f8026ec8d5e0b760e0
    role: context
  - path: scripts/repair_komodo_507_carboxydothermus_score10.py
    sha256: d33ce935e5f4621b68f2e8c3e351b4d0ec7e63caccc73918d5e43a38d7161582
    role: context
  - path: scripts/repair_mediadive_jcm_structure.py
    sha256: 5bff4c2d1900051bdea1b8e0f655049147c85cc9c61da4c348a6d60a8d0fd509
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
  selection: Authoritative batch059 index 09
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:001640
targets:
- target_id: CultureMech:001640
  path: data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml
  label: carboxydothermus_siderophilus_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_12326.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_18923.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_21278.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_21830.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_23698.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml
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
  - CultureMech:001640
  command: just validate-schema data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml
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
  - CultureMech:001640
  command: just validate-strict data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml
    --out REVIEW_WORK/batch059/record09/strict.tsv --workers 1 --quiet
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
  - CultureMech:001640
  command: just validate-terms data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml
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
  - CultureMech:001640
  command: just validate-references data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: dsm507a
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf
  accessed_at: '2026-10-28T06:51:39.622388Z'
  locator: REVIEW_WORK/batch059/source07-09/dsm507a.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact primary medium and its printed stock/preparation subsections; named
    strain variations remain separate and do not establish generic growth.
  snapshot_sha256: c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79
- evidence_id: api507a
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/507a
  accessed_at: '2026-10-28T06:51:39.281663Z'
  locator: REVIEW_WORK/batch059/source07-09/api507a.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current provider identity and declared amounts/basis; provider volume
    is not independently measured final volume.
  snapshot_sha256: a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7
- evidence_id: dsm507
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf
  accessed_at: '2026-10-28T06:51:39.624958Z'
  locator: REVIEW_WORK/batch059/source07-09/dsm507.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact primary medium and its printed stock/preparation subsections; named
    strain variations remain separate and do not establish generic growth.
  snapshot_sha256: 47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4
- evidence_id: api507
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/507
  accessed_at: '2026-10-28T06:51:39.443123Z'
  locator: REVIEW_WORK/batch059/source07-09/api507.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current provider identity and declared amounts/basis; provider volume
    is not independently measured final volume.
  snapshot_sha256: 14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:34887
  accessed_at: '2026-10-28T06:51:42.869820Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi34887.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 3a37ef35991d24faf578286a7d7557ee1b0646c286dd3f8a555d833e6bf82a57
- evidence_id: chebi53542
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53542
  accessed_at: '2026-10-28T06:51:43.468678Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi53542.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 1e44a068cfe6b98d7bb3b0240ffdc0611e1be59f2d3dab9f04e4162ed94e4444
- evidence_id: chebi64734
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:64734
  accessed_at: '2026-10-28T06:51:43.579559Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi64734.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 4afcce140f81023fe7e21d1081a51e76eb83b0d89e158079ef5be695df2388ec
- evidence_id: chebi15956
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15956
  accessed_at: '2026-10-28T06:51:41.086967Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi15956.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 5135a39e8b52c878896db22443f00507125db80e5ce4bb1dcc97914b9bdd7316
- evidence_id: chebi31345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31345
  accessed_at: '2026-10-28T06:51:42.245938Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi31345.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: c3341e7cf8a7ea0768d505265376c1514f161c9048b6e878314e204341d702eb
- evidence_id: chebi16494
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:16494
  accessed_at: '2026-10-28T06:51:40.953073Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi16494.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 192c51f672f633c6071a3397d5785fb2bca6eaf8f9b787f7aaaa6c2aeb3b1a2f
- evidence_id: komodo507
  kind: search
  reference: https://komodo.modelseed.org/servlet/Komodo?getRecipe=507
  accessed_at: '2026-10-28T06:51:39.548364Z'
  locator: REVIEW_WORK/batch059/source07-09/komodo507.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Earlier guessed KOMODO getRecipe route returned HTTP 403. This is an unsuccessful
    discovery lead, not authentication of the exact historical source route; subsequent
    exact MediaInfo attempts are separately retained.
  snapshot_sha256: 9d62115f58d6d9e4bd31b3dd08382175035f1f359fa3eb167e216355916784ce
  search_scope: One public GET of the guessed discovery URL https://komodo.modelseed.org/servlet/Komodo?getRecipe=507;
    retained status 403. No exhaustive repository or literature absence claim.
- evidence_id: komodo507.1
  kind: search
  reference: https://komodo.modelseed.org/servlet/Komodo?getRecipe=507.1
  accessed_at: '2026-10-28T06:51:39.607590Z'
  locator: REVIEW_WORK/batch059/source07-09/komodo507.1.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Earlier guessed KOMODO getRecipe route returned HTTP 403. This is an unsuccessful
    discovery lead, not authentication of the exact historical source route; subsequent
    exact MediaInfo attempts are separately retained.
  snapshot_sha256: f11b360a8f08f0cf69c5d7f65f1585765279b93263812842c088f70faef26ffa
  search_scope: One public GET of the guessed discovery URL https://komodo.modelseed.org/servlet/Komodo?getRecipe=507.1;
    retained status 403. No exhaustive repository or literature absence claim.
- evidence_id: komodo507.2
  kind: search
  reference: https://komodo.modelseed.org/servlet/Komodo?getRecipe=507.2
  accessed_at: '2026-10-28T06:51:39.720539Z'
  locator: REVIEW_WORK/batch059/source07-09/komodo507.2.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Earlier guessed KOMODO getRecipe route returned HTTP 403. This is an unsuccessful
    discovery lead, not authentication of the exact historical source route; subsequent
    exact MediaInfo attempts are separately retained.
  snapshot_sha256: fc8955254714ea0ea305f4f3f5f66219ab531c5d3399a970e5e8259d2a38c19c
  search_scope: One public GET of the guessed discovery URL https://komodo.modelseed.org/servlet/Komodo?getRecipe=507.2;
    retained status 403. No exhaustive repository or literature absence claim.
- evidence_id: komodo507.3
  kind: search
  reference: https://komodo.modelseed.org/servlet/Komodo?getRecipe=507.3
  accessed_at: '2026-10-28T06:51:39.757079Z'
  locator: REVIEW_WORK/batch059/source07-09/komodo507.3.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Earlier guessed KOMODO getRecipe route returned HTTP 403. This is an unsuccessful
    discovery lead, not authentication of the exact historical source route; subsequent
    exact MediaInfo attempts are separately retained.
  snapshot_sha256: 1039ad96140901526c8ed589b75946fadc65e02596b6cada95618a0e18880aea
  search_scope: One public GET of the guessed discovery URL https://komodo.modelseed.org/servlet/Komodo?getRecipe=507.3;
    retained status 403. No exhaustive repository or literature absence claim.
- evidence_id: komodo507.4
  kind: search
  reference: https://komodo.modelseed.org/servlet/Komodo?getRecipe=507.4
  accessed_at: '2026-10-28T06:51:39.714015Z'
  locator: REVIEW_WORK/batch059/source07-09/komodo507.4.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Earlier guessed KOMODO getRecipe route returned HTTP 403. This is an unsuccessful
    discovery lead, not authentication of the exact historical source route; subsequent
    exact MediaInfo attempts are separately retained.
  snapshot_sha256: 213f8f0883b35f5d6cb7856be5041308053362a121f7cb95ca91b09093bc03b3
  search_scope: One public GET of the guessed discovery URL https://komodo.modelseed.org/servlet/Komodo?getRecipe=507.4;
    retained status 403. No exhaustive repository or literature absence claim.
- evidence_id: komodo507.5
  kind: search
  reference: https://komodo.modelseed.org/servlet/Komodo?getRecipe=507.5
  accessed_at: '2026-10-28T06:51:39.713929Z'
  locator: REVIEW_WORK/batch059/source07-09/komodo507.5.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Earlier guessed KOMODO getRecipe route returned HTTP 403. This is an unsuccessful
    discovery lead, not authentication of the exact historical source route; subsequent
    exact MediaInfo attempts are separately retained.
  snapshot_sha256: f746822e5cb462473f9fd7467600346b4ae6056cc2debd97e6c0fc9198f77a85
  search_scope: One public GET of the guessed discovery URL https://komodo.modelseed.org/servlet/Komodo?getRecipe=507.5;
    retained status 403. No exhaustive repository or literature absence claim.
- evidence_id: komodo507.7
  kind: search
  reference: https://komodo.modelseed.org/servlet/Komodo?getRecipe=507.7
  accessed_at: '2026-10-28T06:51:39.761171Z'
  locator: REVIEW_WORK/batch059/source07-09/komodo507.7.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Earlier guessed KOMODO getRecipe route returned HTTP 403. This is an unsuccessful
    discovery lead, not authentication of the exact historical source route; subsequent
    exact MediaInfo attempts are separately retained.
  snapshot_sha256: f07d8f65281e8c1c5bbd4b3ff69cab55cd03b0322a34092ca7b687c05b6358ae
  search_scope: One public GET of the guessed discovery URL https://komodo.modelseed.org/servlet/Komodo?getRecipe=507.7;
    retained status 403. No exhaustive repository or literature absence claim.
- evidence_id: komodo507_7242
  kind: search
  reference: https://komodo.modelseed.org/servlet/Komodo?getRecipe=507_7242
  accessed_at: '2026-10-28T06:51:39.769249Z'
  locator: REVIEW_WORK/batch059/source07-09/komodo507_7242.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Earlier guessed KOMODO getRecipe route returned HTTP 403. This is an unsuccessful
    discovery lead, not authentication of the exact historical source route; subsequent
    exact MediaInfo attempts are separately retained.
  snapshot_sha256: 144daf9856d205c11c6b8e2ee006c35443bdd0c77662317bdb7009e2eca406ec
  search_scope: One public GET of the guessed discovery URL https://komodo.modelseed.org/servlet/Komodo?getRecipe=507_7242;
    retained status 403. No exhaustive repository or literature absence claim.
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml
  locator: Complete file
  accessed_at: '2026-10-28T07:08:50.034259Z'
  support: context_only
  summary: Complete generated target.
  snapshot_sha256: cd8c09e29dbb71a965afd4c18114e124dfe8025d83bb0690423f4777fb627211
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml
  locator: Complete file
  accessed_at: '2026-10-28T07:08:50.034423Z'
  support: context_only
  summary: Complete exact maintained owner.
  snapshot_sha256: 8bc1c4982db978a9dc25662937e53a24665d2c60302b80bb58fabd37ab3b4a5a
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete file
  accessed_at: '2026-10-28T07:08:50.034448Z'
  support: context_only
  summary: Exact packaged current identifier/ontology_id and preferred-term rows.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Complete file
  accessed_at: '2026-10-28T07:08:50.034764Z'
  support: context_only
  summary: Exact packaged snapshot version and checksum.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Full formulation comparison
  accessed_at: '2026-10-28T07:08:50.034786Z'
  support: context_only
  summary: Current scientific-field equality includes quantities, stocks and notes;
    no chemical equivalence is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-28T07:08:50.034805Z'
  support: context_only
  summary: Current merge_group copies singletons and rejects incompatible multiple
    formulations. Generated staleness is not evidence that current code permits ingredient-only
    merging.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: owner-2
  kind: record_content
  reference: data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml
  locator: Complete file
  accessed_at: '2026-10-28T07:08:50.034827Z'
  support: context_only
  summary: Complete exact additional maintained owner.
  snapshot_sha256: f003bb781f43232ba7cdf9ae5c2477be7860913a93f84c44b38e4f97e9b59da9
- evidence_id: owner-3
  kind: record_content
  reference: data/normalized_yaml/bacterial/for_dsm_12326.yaml
  locator: Complete file
  accessed_at: '2026-10-28T07:08:50.034846Z'
  support: context_only
  summary: Complete exact additional maintained owner.
  snapshot_sha256: 75e15e8ef624d170acd18d85d2fbba8409611e241e61bb431895b661f901310a
- evidence_id: owner-4
  kind: record_content
  reference: data/normalized_yaml/bacterial/for_dsm_18923.yaml
  locator: Complete file
  accessed_at: '2026-10-28T07:08:50.034865Z'
  support: context_only
  summary: Complete exact additional maintained owner.
  snapshot_sha256: b14bbf6df3e3e316cb6ae65c211a68929f6be80de42c158f7d2e2597bfd02526
- evidence_id: owner-5
  kind: record_content
  reference: data/normalized_yaml/bacterial/for_dsm_21278.yaml
  locator: Complete file
  accessed_at: '2026-10-28T07:08:50.034883Z'
  support: context_only
  summary: Complete exact additional maintained owner.
  snapshot_sha256: a862a1226bea719aab2a952bdc2d96d6cbbaff051df7dc0368198d9d9f5d8881
- evidence_id: owner-6
  kind: record_content
  reference: data/normalized_yaml/bacterial/for_dsm_21830.yaml
  locator: Complete file
  accessed_at: '2026-10-28T07:08:50.034904Z'
  support: context_only
  summary: Complete exact additional maintained owner.
  snapshot_sha256: 3e24cacb3865c1c3f6f174bac026eafcf5a936512749fd6614d6e131ccebae34
- evidence_id: owner-7
  kind: record_content
  reference: data/normalized_yaml/bacterial/for_dsm_23698.yaml
  locator: Complete file
  accessed_at: '2026-10-28T07:08:50.034921Z'
  support: context_only
  summary: Complete exact additional maintained owner.
  snapshot_sha256: a810f79c39b25b73642c867b70cd5fc93d4b1cf68b0091ee67eb0fe2612d660b
- evidence_id: owner-8
  kind: record_content
  reference: data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml
  locator: Complete file
  accessed_at: '2026-10-28T07:08:50.034939Z'
  support: context_only
  summary: Complete exact additional maintained owner.
  snapshot_sha256: cbed41f17007c7cf46338f50380d5ed4860074bbaa63053879d45c6ac11279d9
- evidence_id: owner-9
  kind: record_content
  reference: data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml
  locator: Complete file
  accessed_at: '2026-10-28T07:08:50.034957Z'
  support: context_only
  summary: Complete exact additional maintained owner.
  snapshot_sha256: ae3a128915194898b4ad4986d1ff597439bcc0083ba7f3def873d3cb74419044
- evidence_id: report-24
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-1500-2000/inspected-candidate-context.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T07:08:50.034978Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 20c95f15dfdb08b3e7019d784339ef66641789e40579c7c51f9396092b007fba
- evidence_id: report-25
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-1500-2000/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T07:08:50.035056Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 56e72694e73e28cee3666277d0f215973f770da991b4b42930105ec89d0ab6e3
- evidence_id: report-26
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-1500-2000/records/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T07:08:50.043683Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 8000569bc2dde9595e866728637805559c124b4d3dc9cd67e2f08a39601969dd
- evidence_id: report-27
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-1500-2000/records/bacterial/for_dsm_12326.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T07:08:50.043747Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 647da9a31dedacdee4fc472314ef2349ac299f7e25dd9d197fd9f1dce89615f6
- evidence_id: report-28
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-1500-2000/records/bacterial/for_dsm_18923.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T07:08:50.043782Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: b1b918dda4ffe61054b7beee22c2e08ec3eb9b97bc892b90f820d64c26bf1bf9
- evidence_id: report-29
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-1500-2000/records/bacterial/for_dsm_21278.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T07:08:50.043814Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 73e14d47bb12b7075e8cc8164ba7c8925080873911c67e2cf231ee9a03b257f4
- evidence_id: report-30
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-1500-2000/records/bacterial/for_dsm_21830.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T07:08:50.043846Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: b04b8053efae35f64dd3762f2eda942a9f17c9df4826f4955352ddc7a69f2c9a
- evidence_id: report-31
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-1500-2000/records/bacterial/for_dsm_23698.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T07:08:50.043878Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 2b416b47dbc9f757598e34e7f39a7f1735ddba3577db4aed0f472571e467175d
- evidence_id: report-32
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-1500-2000/records/bacterial/medium_507_modified_for_dsm_7242.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T07:08:50.043911Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 5586daae5f3dc4ee9c93018afa606746d4ff3ef8c280f4933c47b3d54ae76283
- evidence_id: report-33
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-1500-2000/records/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T07:08:50.043944Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 164d431dd11e2e25c0db211860c7a7fd604043c9890558ff5ecf24da7c6b0315
- evidence_id: report-34
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T07:08:50.043977Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: bc8c96d09770525e6b6ba6dc0c7680354cf9bc6baa5249e79e82b65328203147
- evidence_id: report-35
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/carboxydothermus_siderophilus_medium.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T07:08:50.050229Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: eae5c21979264b496d93686f241806f3b67dbad811f8d5e8a3da8125bd92c92a
- evidence_id: report-36
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T07:08:50.050303Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: f5fa9de661c4938a2548906fbc5c74e581cee77ef744846c6511aff5ec796572
- evidence_id: report-37
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.md
  locator: Complete report
  accessed_at: '2026-10-28T07:08:50.050331Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: d76f54aea4a16f7b1741737df7f64588d336bc499fd2c0c73cfbb00d2c321396
- evidence_id: report-38
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.md
  locator: Complete report
  accessed_at: '2026-10-28T07:08:50.050364Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: dea5e8f503f1d1c9b958e57b51096d7649e23e1873b8889944dcc9bb44ee51d1
- evidence_id: report-39
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_12326.md
  locator: Complete report
  accessed_at: '2026-10-28T07:08:50.050387Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 92d2d5079dff869ecf34424390f397e685d6302d74411babc8df0776f23bd7d0
- evidence_id: report-40
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_18923.md
  locator: Complete report
  accessed_at: '2026-10-28T07:08:50.050412Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 794af8c36f8ad212d39ff61f90c05fe4515ab8f827a0e1260cab42f1ff330f5d
- evidence_id: report-41
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_21278.md
  locator: Complete report
  accessed_at: '2026-10-28T07:08:50.050433Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 5bf8544f23ed749aa7fcf29827e866159fba7fcdb9aa21d40584060633c12464
- evidence_id: report-42
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_21830.md
  locator: Complete report
  accessed_at: '2026-10-28T07:08:50.050455Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 1c5f0a642b11c70c661e6eca3fa2a9a6df1473e5d777eeb0cecaab0647f104b8
- evidence_id: report-43
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_23698.md
  locator: Complete report
  accessed_at: '2026-10-28T07:08:50.050480Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: a417735c51bd73b6e8177c4cc6022a1067cea875b5bd4fddd880b1cc055c1f3f
- evidence_id: report-44
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.md
  locator: Complete report
  accessed_at: '2026-10-28T07:08:50.050506Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 453010b6bf11ec5651e59352a315a04671a9799916658229db4335386200a8a4
- evidence_id: report-45
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.md
  locator: Complete report
  accessed_at: '2026-10-28T07:08:50.050528Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: c07dc55e92ef67cf776da34ef31840a5d6cdcda589401f2159fee065e5d173fc
- evidence_id: report-46
  kind: prior_review
  reference: reports/yaml_record_review/20260922T041153Z-CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T07:08:50.050550Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: b7a8481b6a767f31ea8b75dc169c87f1e561f31c9df9a1bd41e46471071c3ae1
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition, _is_api_stock_addition, _parse_api_solutions, _normalize_unit
  accessed_at: '2026-10-28T07:08:50.050574Z'
  support: context_only
  summary: Current parser reads only the primary recipe, separates referenced solutions
    and percentage/ml additions, and preserves their source attributes. It prefers
    explicit g_l but otherwise maps bare mass/volume units to per-litre schema units.
    This credits existing stage handling without certifying a source final volume
    or historical execution.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-cleanup
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: _merge_ingredient_group
  accessed_at: '2026-10-28T07:08:50.050610Z'
  support: context_only
  summary: Current duplicate cleanup collapses identical values but flags conflicting
    values without summing. Earlier sums require source-stage curation; do not rerun
    cleanup as a substitute for scientific reconciliation.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: historical-reading
  kind: prior_review
  reference: REVIEW_WORK/batch059/record09/historical-reading.json
  locator: Complete report cell pool and exact current-source object joins
  accessed_at: '2026-10-28T07:08:50.278673Z'
  support: context_only
  summary: Complete report text read through exact duplicate pooling; old conclusions
    separately assessed.
  snapshot_sha256: 292beb1c1fc0d238c2ad2f78fe19ff8ea5dcb88858200de9c343d046d551dc03
- evidence_id: writer-507
  kind: record_content
  reference: scripts/repair_komodo_507_carboxydothermus_score10.py
  locator: Complete file, ingredient_signature, variant constants and _upsert_event
  accessed_at: '2026-10-28T07:08:50.280999Z'
  support: context_only
  summary: Current code hardcodes the27-row507a-like ingredient signature, SOURCE_DUPLICATE
    classification and variant graph. Its _upsert_event replaces a matching curator/action
    event with a fixed historical timestamp. These current assumptions need correction;
    do not blindly rerun this writer as append-only curation. Current code does not
    prove a past execution.
  snapshot_sha256: d33ce935e5f4621b68f2e8c3e351b4d0ec7e63caccc73918d5e43a38d7161582
- evidence_id: chebi32588
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32588
  accessed_at: '2026-10-28T06:51:42.616651Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi32588.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 9494b26ad5d3ce43942c3e859cdefe4114e111b1d45328c0cd5faf3b75faec00
- evidence_id: chebi86345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86345
  accessed_at: '2026-10-28T06:51:44.702578Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi86345.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 94b600ced6e98743e2d1b02c73e1756f8f81b639407a8fdd080c96d8fa563c70
- evidence_id: chebi86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86158
  accessed_at: '2026-10-28T06:51:44.192971Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi86158.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: eacf58308fa876cb17661b82d08a64d9be24814fde8014ac82da7696b3684841
- evidence_id: chebi31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31206
  accessed_at: '2026-10-28T06:51:42.216507Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi31206.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 645112dbfa7f1c565489070586f5d4018429259ff0400500ca10dfe6e43a5449
- evidence_id: chebi63036
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63036
  accessed_at: '2026-10-28T06:51:43.517218Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi63036.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 07dec38373731d2125348c574d0f9f2df977e458974100383d3f69c8849a84e0
- evidence_id: chebi32139
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32139
  accessed_at: '2026-10-28T06:51:42.273272Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi32139.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 51709e2510736d0b63369147b10ec6ffe80d5d5c3a40605381de9b3ed78634c3
- evidence_id: chebi75836
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75836
  accessed_at: '2026-10-28T06:51:44.192791Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi75836.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: ab9922083bab0fb07df977855094d11fe3a5ca1f14bc6bddd10dc80ad9055569
- evidence_id: chebi32312
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32312
  accessed_at: '2026-10-28T06:51:42.325517Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi32312.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 19bbc18dfc582e76457c6f08d51bb777a2f7a2cbd2f810cb3b58bdb0004b4d60
- evidence_id: chebi86368
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86368
  accessed_at: '2026-10-28T06:51:44.859904Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi86368.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 2d5685a4a03c5d730876514b4a7664fb477f63682a60cc7e13d7776a250f68e3
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:33118
  accessed_at: '2026-10-28T06:51:42.837479Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi33118.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: eef160dcdcd93f231064bc7b59da1e05a2efe1f96089b9cd2fdbdf68a9a4e5fc
- evidence_id: chebi53503
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53503
  accessed_at: '2026-10-28T06:51:43.468865Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi53503.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: a626d2aa210aafd9572221d4893cd206310d5df507e474e1528997048f522250
- evidence_id: chebi86318
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86318
  accessed_at: '2026-10-28T06:51:44.725430Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi86318.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: bd88e1499f370a9f474b29fa7a9a83aa5c42c69d0b6772ece8c89d646dfda8d8
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75213
  accessed_at: '2026-10-28T06:51:44.103080Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi75213.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: f99a2d8b28ac44913a666745dd70098c5d5f21c9513fee921a35f0fd18f2c445
- evidence_id: chebi27470
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:27470
  accessed_at: '2026-10-28T06:51:41.647007Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi27470.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: e1820a7a704794fa20995eea5037e03c2b22b847817c28bb2f45f80762c275d1
- evidence_id: chebi30961
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30961
  accessed_at: '2026-10-28T06:51:42.015654Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi30961.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 855ea2cf0e89d25ab4a560ab1c2dab6ac861d215bc5473cb4d3a0a2d4cdff438
- evidence_id: chebi49105
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49105
  accessed_at: '2026-10-28T06:51:42.911648Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi49105.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: f9dbae8cd2dcbd38d914abb99730e341ff280d3a44f20f95b2663e47664780cf
- evidence_id: chebi17015
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17015
  accessed_at: '2026-10-28T06:51:41.015362Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi17015.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 17f7ac7c03d75b85a96f951321902906266f3ce8fa44faea4814fac46560e3e6
- evidence_id: chebi15940
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15940
  accessed_at: '2026-10-28T06:51:40.977277Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi15940.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: c291a1c1bb0d6af05ac4005af0957534f430db47e7df9cec874f8a94d961dba1
- evidence_id: chebi176843
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:176843
  accessed_at: '2026-10-28T06:51:41.413603Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi176843.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 9c73ea31864abce6b9ed6328e9ed491bc1cad2ba27f40adb5c00f0f192838e63
- evidence_id: chebi30753
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30753
  accessed_at: '2026-10-28T06:51:41.732561Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi30753.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 1340e054634ce960494b9388f6e3fd231d9e7d66969c3c11932ee2058171fd2c
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch059/record09/quantity-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T07:21:14.364307Z'
  support: supports
  summary: Complete source-stage quantity decisions.
  snapshot_sha256: f90399f0340ce0fa1e082e125090accabf0777ff1f157a88ad3ad972e5a32216
- evidence_id: groundings
  kind: record_content
  reference: REVIEW_WORK/batch059/record09/grounding-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T07:08:50.655018Z'
  support: supports
  summary: Exact slots, raw OLS scientific objects and current MIM rows.
  snapshot_sha256: 2d220c5f40743cf9c489e8e5db2cbb6ffcf3448bb12ac573c21cbea429408b98
- evidence_id: census
  kind: record_content
  reference: REVIEW_WORK/batch059/record09/field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T07:08:50.655273Z'
  support: supports
  summary: Complete scalar census with explicit dependency exclusions.
  snapshot_sha256: 5fd5d1b482d018244f8192d34ddd8d1caba4884ef73c4399ca0548d7bb9a79a2
- evidence_id: numeric-census
  kind: record_content
  reference: REVIEW_WORK/batch059/record09/numeric-field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T07:08:50.655500Z'
  support: supports
  summary: Numeric/text assertions and quantity joins.
  snapshot_sha256: fb83e7fbda88d91febc3908eb7c7e599eb5b37a68943545fe0ba66c3edf2a0c6
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch059/record09/history-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T07:08:50.655696Z'
  support: supports
  summary: Current exact histories, without replay.
  snapshot_sha256: ecaf266b1c1abd6ffc3ca4cb1f722c4b5db7b25dcabf959c6257b078e5e7efda
- evidence_id: old-reports
  kind: record_content
  reference: REVIEW_WORK/batch059/record09/history-report-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T07:08:50.655740Z'
  support: supports
  summary: Exact historical report scopes.
  snapshot_sha256: daeb5c4e4c6d5590260e512999094a8de34fc51b435823565e801e45b52659f0
- evidence_id: old-claims
  kind: record_content
  reference: REVIEW_WORK/batch059/record09/existing-claim-authentication.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T07:08:50.655769Z'
  support: supports
  summary: Existing literal and raw-digest matches; current content authentication
    is separate from original retrieval provenance.
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch059/record09/schema-result.json
  accessed_at: '2026-10-28T06:51:21.886114Z'
  support: supports
  summary: Original once-only canonical schema with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 1a5c5999b0565b847621196afcc45676878d464be6ab74093906578ea7ca04d8
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch059/record09/strict-result.json
  accessed_at: '2026-10-28T06:51:22.807349Z'
  support: supports
  summary: Original once-only canonical strict with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: e04be5d678f21290c7b1715ac3d808fb7575ef04fea4d49521f4fc96f3ac724c
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch059/record09/terms-result.json
  accessed_at: '2026-10-28T06:51:23.818860Z'
  support: supports
  summary: Original once-only canonical terms with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 5e480b6e529e9c95b7954a004908b66752bf9110ad4ff93ab58f093bed0d1a6d
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch059/record09/references-result.json
  accessed_at: '2026-10-28T06:51:24.548380Z'
  support: supports
  summary: Original once-only canonical references with complete argv/time/streams;
    reference count zero does not verify sources.
  snapshot_sha256: ee186baa87e20982f1f6a036614b29dc91507d3b02e49ebf031fb52e9019756a
- evidence_id: komodo-exact-1
  kind: search
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=507
  locator: REVIEW_WORK/batch059/record09-peer-exact-routes-20261028T071852Z/result.json
    $.outcomes[0]; historical discovery $.unique_cells[263]
  accessed_at: '2026-10-28T07:18:52.880356Z'
  support: context_only
  summary: Exact historical MediaInfo hyperlink attempted once; HTTP 403 challenge.
    No current formulation or historical access-time authentication follows.
  snapshot_sha256: 1f5e3a5058cab4458e973ca126a96d121a730be7aea5eeef9aa8e90da65859a9
  search_scope: One GET of the exact historical hyperlink https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=507;
    no automatic retries or broader absence claim.
- evidence_id: komodo-exact-2
  kind: search
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=507.2
  locator: REVIEW_WORK/batch059/record09-peer-exact-routes-20261028T071852Z/result.json
    $.outcomes[1]; historical discovery $.unique_cells[282]
  accessed_at: '2026-10-28T07:18:53.108676Z'
  support: context_only
  summary: Exact historical MediaInfo hyperlink attempted once; HTTP 403 challenge.
    No current formulation or historical access-time authentication follows.
  snapshot_sha256: c9f553b14c69a200408c7c6df11403af8dba4d95dbf26772b334385fae7bd2ab
  search_scope: One GET of the exact historical hyperlink https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=507.2;
    no automatic retries or broader absence claim.
- evidence_id: komodo-exact-3
  kind: search
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=507.3
  locator: REVIEW_WORK/batch059/record09-peer-exact-routes-20261028T071852Z/result.json
    $.outcomes[2]; historical discovery $.unique_cells[291]
  accessed_at: '2026-10-28T07:18:52.882486Z'
  support: context_only
  summary: Exact historical MediaInfo hyperlink attempted once; HTTP 403 challenge.
    No current formulation or historical access-time authentication follows.
  snapshot_sha256: e2d7ad8e7a09fe8e8fe64759cd724496b6905e13d3118fc16d126466b24e6b30
  search_scope: One GET of the exact historical hyperlink https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=507.3;
    no automatic retries or broader absence claim.
- evidence_id: komodo-exact-4
  kind: search
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=507.4
  locator: REVIEW_WORK/batch059/record09-peer-exact-routes-20261028T071852Z/result.json
    $.outcomes[3]; historical discovery $.unique_cells[300]
  accessed_at: '2026-10-28T07:18:52.889109Z'
  support: context_only
  summary: Exact historical MediaInfo hyperlink attempted once; HTTP 403 challenge.
    No current formulation or historical access-time authentication follows.
  snapshot_sha256: b9ca3bf3c0163d9ba28d1f0b79d78effb0566a3130ae27da4a913c200d68bc9c
  search_scope: One GET of the exact historical hyperlink https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=507.4;
    no automatic retries or broader absence claim.
- evidence_id: komodo-exact-5
  kind: search
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=507.5
  locator: REVIEW_WORK/batch059/record09-peer-exact-routes-20261028T071852Z/result.json
    $.outcomes[4]; historical discovery $.unique_cells[309]
  accessed_at: '2026-10-28T07:18:52.977806Z'
  support: context_only
  summary: Exact historical MediaInfo hyperlink attempted once; HTTP 403 challenge.
    No current formulation or historical access-time authentication follows.
  snapshot_sha256: 9d13fd9f148660ff4891e44ff01bc97a6b0859f1d4222e48886e24f4fc9887e4
  search_scope: One GET of the exact historical hyperlink https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=507.5;
    no automatic retries or broader absence claim.
- evidence_id: komodo-exact-6
  kind: search
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=507.7
  locator: REVIEW_WORK/batch059/record09-peer-exact-routes-20261028T071852Z/result.json
    $.outcomes[5]; historical discovery $.unique_cells[319]
  accessed_at: '2026-10-28T07:18:52.977877Z'
  support: context_only
  summary: Exact historical MediaInfo hyperlink attempted once; HTTP 403 challenge.
    No current formulation or historical access-time authentication follows.
  snapshot_sha256: f7c9bc293c8001454cc1ee52807598231dd9e960f6dd26273a1a30e3606c7728
  search_scope: One GET of the exact historical hyperlink https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=507.7;
    no automatic retries or broader absence claim.
- evidence_id: komodo-exact-7
  kind: search
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=507_7242
  locator: REVIEW_WORK/batch059/record09-peer-exact-routes-20261028T071852Z/result.json
    $.outcomes[6]; historical discovery $.unique_cells[329]
  accessed_at: '2026-10-28T07:18:52.960209Z'
  support: context_only
  summary: Exact historical MediaInfo hyperlink attempted once; HTTP 403 challenge.
    No current formulation or historical access-time authentication follows.
  snapshot_sha256: 5060ba0df8a3385feb659f5d7e63b6751daa2aa8117b8a025ff373ae9ff55731
  search_scope: One GET of the exact historical hyperlink https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=507_7242;
    no automatic retries or broader absence claim.
- evidence_id: komodo-exact-8
  kind: search
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=507.1
  locator: REVIEW_WORK/batch059/record09-peer-exact-routes-20261028T071852Z/result.json
    $.outcomes[7]; historical discovery $.unique_cells[339]
  accessed_at: '2026-10-28T07:18:53.094004Z'
  support: context_only
  summary: Exact historical MediaInfo hyperlink attempted once; HTTP 403 challenge.
    No current formulation or historical access-time authentication follows.
  snapshot_sha256: fdeb012aabc7cff58a75a644fc4e96a7565a0ebb15935911e389b77a4a230875
  search_scope: One GET of the exact historical hyperlink https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=507.1;
    no automatic retries or broader absence claim.
- evidence_id: komodo-exact-catalog
  kind: search
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: REVIEW_WORK/batch059/record01-root-exact-routes/komodo964-list.json; reused
    exact current failed capture with original access time
  accessed_at: '2026-10-28T07:08:35.693802Z'
  support: context_only
  summary: Exact historical MediaList route returned HTTP 403. Current failure is
    distinct from old catalog excerpts.
  snapshot_sha256: dad86ae019c5da0a88b63143ffde0fbfc65248b341be6c798aa9d0d3c25e6bd5
  search_scope: Reuse of one exact public GET of https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList;
    no new request, retries or catalogue-content assertion.
assessments:
- assessment_id: identity
  area: identity
  topic: Canonical identity and conflicting owner family
  outcome: concern
  summary: The target identity and retained preparation match exact DSM507a. Its nine-owner
    merge and duplicate graph improperly collapse materially distinct 507 and 507a
    sources; seven named KOMODO child formulations remain independently unresolved.
    All eight current KOMODO requests failed 403 and remain bounded failed access,
    not evidence of source absence.
  target_ids:
  - CultureMech:001640
  evidence_ids:
  - target
  - owner-2
  - dsm507a
  - api507a
  - dsm507
  - api507
  - komodo-exact-1
  - komodo-exact-2
  - komodo-exact-3
  - komodo-exact-4
  - komodo-exact-5
  - komodo-exact-6
  - komodo-exact-7
  - komodo-exact-8
  - komodo-exact-catalog
- assessment_id: classification
  area: representation
  topic: Classification and existing preparation credit
  outcome: supported
  summary: Complex undefined liquid classification is compatible with yeast extract
    and the source formulation. Existing507a main preparation, pH and 1 bar overpressure
    are retained and credited; stock preparation must move with its own stage. The
    name is not evidence of strain growth.
  target_ids:
  - CultureMech:001640
  evidence_ids:
  - dsm507a
  - api507a
  - target
  - owner-2
- assessment_id: quantities
  area: quantity
  topic: Complete amounts, units and preparation stages
  outcome: concern
  summary: 270 current concentration fields are covered by 67 decisions, including
    unchanged support and explicit source-only conditions.
  target_ids:
  - CultureMech:001640
  evidence_ids:
  - quantities
  - numeric-census
  details: '{"schema": "fresh-b059-quantity-inventory-v1", "target": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml",
    "quantity_field_count": 270, "decisions": [{"quantity_id": "q1", "label": "KCl",
    "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml",
    "field_path": "ingredients[0].concentration", "stored": {"value": "0.326409",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[0].concentration", "stored": {"value": "0.326409",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[0].concentration", "stored": {"value": "0.326409",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml",
    "field_path": "ingredients[0].concentration", "stored": {"value": "0.326409",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml",
    "field_path": "ingredients[0].concentration", "stored": {"value": "0.326409",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml",
    "field_path": "ingredients[0].concentration", "stored": {"value": "0.326409",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml",
    "field_path": "ingredients[0].concentration", "stored": {"value": "0.326409",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml",
    "field_path": "ingredients[0].concentration", "stored": {"value": "0.326409",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml",
    "field_path": "ingredients[0].concentration", "stored": {"value": "0.326409",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[0].concentration", "stored": {"value": "0.326409",
    "unit": "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner
    support, separate507 base conflict and unavailable KOMODO variants are distinguished
    in the layer decisions; no blanket transfer or approval of the ten encoded copies.",
    "source_stage": "main solutions with distinct source identities", "sources": [{"evidence_id":
    "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79",
    "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d",
    "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 3-3",
    "quote": "KCl                                                   0.33            g",
    "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[0].recipe[0]",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\":
    0.33,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.326409,\n                        \"mmol_l\": 4.3784,\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}, {"evidence_id": "dsm507",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4",
    "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7",
    "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 3-3",
    "quote": "KCl                                                      0.33         g",
    "quote_basis": "derivative text"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[0].recipe[0]",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\":
    0.33,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.322896,\n                        \"mmol_l\": 4.33127,\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}], "layer_decisions": [{"path":
    "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path":
    "ingredients[0].concentration", "decision": "evidence_only", "rationale": "The
    exact 507a API explicitly reports the encoded g_l on declared 1011 mL normalization;
    the PDF supports its batch mass. Attach evidence without claiming measured final
    volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[0].concentration", "decision": "conflict", "rationale":
    "The local507a-derived quantity conflicts with or is absent from the separately
    identified 507 base table. Resolve that source identity before correcting this
    maintained owner; do not transfer507a amounts."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[0].concentration", "decision": "evidence_only", "rationale":
    "The exact 507a API explicitly reports the encoded g_l on declared 1011 mL normalization;
    the PDF supports its batch mass. Attach evidence without claiming measured final
    volume."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path":
    "ingredients[0].concentration", "decision": "unsupported", "rationale": "The exact
    KOMODO variant endpoint returned 403. Its local copied signature and base-source
    link do not authenticate this amount. Preserve unresolved variant provenance pending
    exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml",
    "field_path": "ingredients[0].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[0].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml",
    "field_path": "ingredients[0].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[0].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml",
    "field_path": "ingredients[0].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[0].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id":
    "q2", "label": "MgCl2 x 6 H2O", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml",
    "field_path": "ingredients[1].concentration", "stored": {"value": "0.514342",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[1].concentration", "stored": {"value": "0.514342",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[1].concentration", "stored": {"value": "0.514342",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml",
    "field_path": "ingredients[1].concentration", "stored": {"value": "0.514342",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml",
    "field_path": "ingredients[1].concentration", "stored": {"value": "0.514342",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml",
    "field_path": "ingredients[1].concentration", "stored": {"value": "0.514342",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml",
    "field_path": "ingredients[1].concentration", "stored": {"value": "0.514342",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml",
    "field_path": "ingredients[1].concentration", "stored": {"value": "0.514342",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml",
    "field_path": "ingredients[1].concentration", "stored": {"value": "0.514342",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[1].concentration", "stored": {"value": "0.514342",
    "unit": "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner
    support, separate507 base conflict and unavailable KOMODO variants are distinguished
    in the layer decisions; no blanket transfer or approval of the ten encoded copies.",
    "source_stage": "main solutions with distinct source identities", "sources": [{"evidence_id":
    "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79",
    "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d",
    "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 4-4",
    "quote": "MgCl2 x 6 H2O                                         0.52            g",
    "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[0].recipe[1]",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\":
    0.52,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.514342,\n                        \"mmol_l\": 2.52993,\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}, {"evidence_id": "dsm507",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4",
    "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7",
    "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 4-4",
    "quote": "MgCl2 x 6 H2O                                            0.52         g",
    "quote_basis": "derivative text"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[0].recipe[1]",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\":
    0.52,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.508806,\n                        \"mmol_l\": 2.5027,\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}], "layer_decisions": [{"path":
    "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path":
    "ingredients[1].concentration", "decision": "evidence_only", "rationale": "The
    exact 507a API explicitly reports the encoded g_l on declared 1011 mL normalization;
    the PDF supports its batch mass. Attach evidence without claiming measured final
    volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[1].concentration", "decision": "conflict", "rationale":
    "The local507a-derived quantity conflicts with or is absent from the separately
    identified 507 base table. Resolve that source identity before correcting this
    maintained owner; do not transfer507a amounts."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[1].concentration", "decision": "evidence_only", "rationale":
    "The exact 507a API explicitly reports the encoded g_l on declared 1011 mL normalization;
    the PDF supports its batch mass. Attach evidence without claiming measured final
    volume."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path":
    "ingredients[1].concentration", "decision": "unsupported", "rationale": "The exact
    KOMODO variant endpoint returned 403. Its local copied signature and base-source
    link do not authenticate this amount. Preserve unresolved variant provenance pending
    exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml",
    "field_path": "ingredients[1].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[1].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml",
    "field_path": "ingredients[1].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[1].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml",
    "field_path": "ingredients[1].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[1].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id":
    "q3", "label": "CaCl2 x 2 H2O", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml",
    "field_path": "ingredients[2].concentration", "stored": {"value": "0.286845",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[2].concentration", "stored": {"value": "0.286845",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[2].concentration", "stored": {"value": "0.286845",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml",
    "field_path": "ingredients[2].concentration", "stored": {"value": "0.286845",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml",
    "field_path": "ingredients[2].concentration", "stored": {"value": "0.286845",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml",
    "field_path": "ingredients[2].concentration", "stored": {"value": "0.286845",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml",
    "field_path": "ingredients[2].concentration", "stored": {"value": "0.286845",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml",
    "field_path": "ingredients[2].concentration", "stored": {"value": "0.286845",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml",
    "field_path": "ingredients[2].concentration", "stored": {"value": "0.286845",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[2].concentration", "stored": {"value": "0.286845",
    "unit": "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner
    support, separate507 base conflict and unavailable KOMODO variants are distinguished
    in the layer decisions; no blanket transfer or approval of the ten encoded copies.",
    "source_stage": "main solutions with distinct source identities", "sources": [{"evidence_id":
    "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79",
    "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d",
    "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 5-5",
    "quote": "CaCl2 x 2 H2O                                         0.29            g",
    "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[0].recipe[2]",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\":
    0.29,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.286845,\n                        \"mmol_l\": 1.95113,\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}, {"evidence_id": "dsm507",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4",
    "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7",
    "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 5-5",
    "quote": "CaCl2 x 2 H2O                                            0.29         g",
    "quote_basis": "derivative text"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[0].recipe[2]",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\":
    0.29,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.283757,\n                        \"mmol_l\": 1.93013,\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}], "layer_decisions": [{"path":
    "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path":
    "ingredients[2].concentration", "decision": "evidence_only", "rationale": "The
    exact 507a API explicitly reports the encoded g_l on declared 1011 mL normalization;
    the PDF supports its batch mass. Attach evidence without claiming measured final
    volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[2].concentration", "decision": "conflict", "rationale":
    "The local507a-derived quantity conflicts with or is absent from the separately
    identified 507 base table. Resolve that source identity before correcting this
    maintained owner; do not transfer507a amounts."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[2].concentration", "decision": "evidence_only", "rationale":
    "The exact 507a API explicitly reports the encoded g_l on declared 1011 mL normalization;
    the PDF supports its batch mass. Attach evidence without claiming measured final
    volume."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path":
    "ingredients[2].concentration", "decision": "unsupported", "rationale": "The exact
    KOMODO variant endpoint returned 403. Its local copied signature and base-source
    link do not authenticate this amount. Preserve unresolved variant provenance pending
    exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml",
    "field_path": "ingredients[2].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[2].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml",
    "field_path": "ingredients[2].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[2].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml",
    "field_path": "ingredients[2].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[2].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id":
    "q4", "label": "NH4Cl", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml",
    "field_path": "ingredients[3].concentration", "stored": {"value": "0.326409",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[3].concentration", "stored": {"value": "0.326409",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[3].concentration", "stored": {"value": "0.326409",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml",
    "field_path": "ingredients[3].concentration", "stored": {"value": "0.326409",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml",
    "field_path": "ingredients[3].concentration", "stored": {"value": "0.326409",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml",
    "field_path": "ingredients[3].concentration", "stored": {"value": "0.326409",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml",
    "field_path": "ingredients[3].concentration", "stored": {"value": "0.326409",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml",
    "field_path": "ingredients[3].concentration", "stored": {"value": "0.326409",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml",
    "field_path": "ingredients[3].concentration", "stored": {"value": "0.326409",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[3].concentration", "stored": {"value": "0.326409",
    "unit": "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner
    support, separate507 base conflict and unavailable KOMODO variants are distinguished
    in the layer decisions; no blanket transfer or approval of the ten encoded copies.",
    "source_stage": "main solutions with distinct source identities", "sources": [{"evidence_id":
    "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79",
    "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d",
    "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 6-6",
    "quote": "NH4Cl                                                 0.33            g",
    "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[0].recipe[3]",
    "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\":
    0.33,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.326409,\n                        \"mmol_l\": 6.10225,\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}, {"evidence_id": "dsm507",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4",
    "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7",
    "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 6-6",
    "quote": "NH4Cl                                                    0.33         g",
    "quote_basis": "derivative text"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[0].recipe[3]",
    "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\":
    0.33,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.322896,\n                        \"mmol_l\": 6.03657,\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}], "layer_decisions": [{"path":
    "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path":
    "ingredients[3].concentration", "decision": "evidence_only", "rationale": "The
    exact 507a API explicitly reports the encoded g_l on declared 1011 mL normalization;
    the PDF supports its batch mass. Attach evidence without claiming measured final
    volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[3].concentration", "decision": "conflict", "rationale":
    "The local507a-derived quantity conflicts with or is absent from the separately
    identified 507 base table. Resolve that source identity before correcting this
    maintained owner; do not transfer507a amounts."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[3].concentration", "decision": "evidence_only", "rationale":
    "The exact 507a API explicitly reports the encoded g_l on declared 1011 mL normalization;
    the PDF supports its batch mass. Attach evidence without claiming measured final
    volume."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path":
    "ingredients[3].concentration", "decision": "unsupported", "rationale": "The exact
    KOMODO variant endpoint returned 403. Its local copied signature and base-source
    link do not authenticate this amount. Preserve unresolved variant provenance pending
    exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml",
    "field_path": "ingredients[3].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[3].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml",
    "field_path": "ingredients[3].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[3].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml",
    "field_path": "ingredients[3].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[3].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id":
    "q5", "label": "KH2PO4", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml",
    "field_path": "ingredients[4].concentration", "stored": {"value": "0.326409",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[4].concentration", "stored": {"value": "0.326409",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[4].concentration", "stored": {"value": "0.326409",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml",
    "field_path": "ingredients[4].concentration", "stored": {"value": "0.326409",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml",
    "field_path": "ingredients[4].concentration", "stored": {"value": "0.326409",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml",
    "field_path": "ingredients[4].concentration", "stored": {"value": "0.326409",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml",
    "field_path": "ingredients[4].concentration", "stored": {"value": "0.326409",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml",
    "field_path": "ingredients[4].concentration", "stored": {"value": "0.326409",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml",
    "field_path": "ingredients[4].concentration", "stored": {"value": "0.326409",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[4].concentration", "stored": {"value": "0.326409",
    "unit": "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner
    support, separate507 base conflict and unavailable KOMODO variants are distinguished
    in the layer decisions; no blanket transfer or approval of the ten encoded copies.",
    "source_stage": "main solutions with distinct source identities", "sources": [{"evidence_id":
    "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79",
    "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d",
    "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 7-7",
    "quote": "KH2PO4                                                0.33            g",
    "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[0].recipe[4]",
    "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\":
    0.33,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.326409,\n                        \"mmol_l\": 2.39857,\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}, {"evidence_id": "dsm507",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4",
    "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7",
    "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 7-7",
    "quote": "KH2PO4                                                   0.33         g",
    "quote_basis": "derivative text"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[0].recipe[4]",
    "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\":
    0.33,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.322896,\n                        \"mmol_l\": 2.37275,\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}], "layer_decisions": [{"path":
    "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path":
    "ingredients[4].concentration", "decision": "evidence_only", "rationale": "The
    exact 507a API explicitly reports the encoded g_l on declared 1011 mL normalization;
    the PDF supports its batch mass. Attach evidence without claiming measured final
    volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[4].concentration", "decision": "conflict", "rationale":
    "The local507a-derived quantity conflicts with or is absent from the separately
    identified 507 base table. Resolve that source identity before correcting this
    maintained owner; do not transfer507a amounts."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[4].concentration", "decision": "evidence_only", "rationale":
    "The exact 507a API explicitly reports the encoded g_l on declared 1011 mL normalization;
    the PDF supports its batch mass. Attach evidence without claiming measured final
    volume."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path":
    "ingredients[4].concentration", "decision": "unsupported", "rationale": "The exact
    KOMODO variant endpoint returned 403. Its local copied signature and base-source
    link do not authenticate this amount. Preserve unresolved variant provenance pending
    exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml",
    "field_path": "ingredients[4].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[4].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml",
    "field_path": "ingredients[4].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[4].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml",
    "field_path": "ingredients[4].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[4].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id":
    "q6", "label": "Na2-9,10-anthraquinone-2,6-disulfonate", "local_fields": [{"path":
    "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path":
    "ingredients[5].concentration", "stored": {"value": "8.16024", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[5].concentration", "stored": {"value": "8.16024", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[5].concentration", "stored": {"value": "8.16024", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path":
    "ingredients[5].concentration", "stored": {"value": "8.16024", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[5].concentration",
    "stored": {"value": "8.16024", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml",
    "field_path": "ingredients[5].concentration", "stored": {"value": "8.16024", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path":
    "ingredients[5].concentration", "stored": {"value": "8.16024", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[5].concentration",
    "stored": {"value": "8.16024", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml",
    "field_path": "ingredients[5].concentration", "stored": {"value": "8.16024", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[5].concentration", "stored": {"value": "8.16024", "unit":
    "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner support,
    separate507 base conflict and unavailable KOMODO variants are distinguished in
    the layer decisions; no blanket transfer or approval of the ten encoded copies.",
    "source_stage": "main solutions with distinct source identities", "sources": [{"evidence_id":
    "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79",
    "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d",
    "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 8-8",
    "quote": "Na2-9,10-anthraquinone-2,6-disulfonate (TCI A0308)    8.25            g",
    "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[0].recipe[5]",
    "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\":
    \"Na2-9,10-anthraquinone-2,6-disulfonate\",\n                        \"compound_id\":
    521,\n                        \"attribute\": \"TCI A0308\",\n                        \"amount\":
    8.25,\n                        \"unit\": \"g\",\n                        \"g_l\":
    8.16024,\n                        \"optional\": 0\n                    }", "quote_basis":
    "raw UTF-8"}, {"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4",
    "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7",
    "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 3-14",
    "quote": "KCl                                                      0.33         g\n   MgCl2
    x 6 H2O                                            0.52         g\n   CaCl2 x
    2 H2O                                            0.29         g\n   NH4Cl                                                    0.33         g\n   KH2PO4                                                   0.33         g\n   Trace
    element solution SL-11                             1.00        ml\n   Sodium resazurin
    (0.1% w/v)                              0.50        ml\n   NaHCO3                                                   1.00         g\n   Yeast
    extract                                            0.05         g\n   Wolin''s
    vitamin solution (10x)                           1.00        ml\n   Neutralized
    sulfide solution 3% (w/v)                   20.00        ml\n   Distilled water                                       1000.00        ml",
    "quote_basis": "derivative text"}], "layer_decisions": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml",
    "field_path": "ingredients[5].concentration", "decision": "evidence_only", "rationale":
    "The exact 507a API explicitly reports the encoded g_l on declared 1011 mL normalization;
    the PDF supports its batch mass. Attach evidence without claiming measured final
    volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[5].concentration", "decision": "conflict", "rationale":
    "The local507a-derived quantity conflicts with or is absent from the separately
    identified 507 base table. Resolve that source identity before correcting this
    maintained owner; do not transfer507a amounts."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[5].concentration", "decision": "evidence_only", "rationale":
    "The exact 507a API explicitly reports the encoded g_l on declared 1011 mL normalization;
    the PDF supports its batch mass. Attach evidence without claiming measured final
    volume."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path":
    "ingredients[5].concentration", "decision": "unsupported", "rationale": "The exact
    KOMODO variant endpoint returned 403. Its local copied signature and base-source
    link do not authenticate this amount. Preserve unresolved variant provenance pending
    exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml",
    "field_path": "ingredients[5].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[5].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml",
    "field_path": "ingredients[5].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[5].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml",
    "field_path": "ingredients[5].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[5].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id":
    "q7", "label": "NaHCO3", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml",
    "field_path": "ingredients[6].concentration", "stored": {"value": "0.98912", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[6].concentration", "stored": {"value": "0.98912", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[6].concentration", "stored": {"value": "0.98912", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path":
    "ingredients[6].concentration", "stored": {"value": "0.98912", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[6].concentration",
    "stored": {"value": "0.98912", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml",
    "field_path": "ingredients[6].concentration", "stored": {"value": "0.98912", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path":
    "ingredients[6].concentration", "stored": {"value": "0.98912", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[6].concentration",
    "stored": {"value": "0.98912", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml",
    "field_path": "ingredients[6].concentration", "stored": {"value": "0.98912", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[6].concentration", "stored": {"value": "0.98912", "unit":
    "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner support,
    separate507 base conflict and unavailable KOMODO variants are distinguished in
    the layer decisions; no blanket transfer or approval of the ten encoded copies.",
    "source_stage": "main solutions with distinct source identities", "sources": [{"evidence_id":
    "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79",
    "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d",
    "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 10-10",
    "quote": "NaHCO3                                                1.00            g",
    "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[0].recipe[7]",
    "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\":
    \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"amount\":
    1,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.98912,\n                        \"mmol_l\": 11.7743,\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}, {"evidence_id": "dsm507",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4",
    "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7",
    "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 10-10",
    "quote": "NaHCO3                                                   1.00         g",
    "quote_basis": "derivative text"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[0].recipe[7]",
    "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\":
    \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"amount\":
    1,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.978474,\n                        \"mmol_l\": 11.6475,\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}], "layer_decisions": [{"path":
    "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path":
    "ingredients[6].concentration", "decision": "evidence_only", "rationale": "The
    exact 507a API explicitly reports the encoded g_l on declared 1011 mL normalization;
    the PDF supports its batch mass. Attach evidence without claiming measured final
    volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[6].concentration", "decision": "conflict", "rationale":
    "The local507a-derived quantity conflicts with or is absent from the separately
    identified 507 base table. Resolve that source identity before correcting this
    maintained owner; do not transfer507a amounts."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[6].concentration", "decision": "evidence_only", "rationale":
    "The exact 507a API explicitly reports the encoded g_l on declared 1011 mL normalization;
    the PDF supports its batch mass. Attach evidence without claiming measured final
    volume."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path":
    "ingredients[6].concentration", "decision": "unsupported", "rationale": "The exact
    KOMODO variant endpoint returned 403. Its local copied signature and base-source
    link do not authenticate this amount. Preserve unresolved variant provenance pending
    exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml",
    "field_path": "ingredients[6].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[6].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml",
    "field_path": "ingredients[6].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[6].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml",
    "field_path": "ingredients[6].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[6].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id":
    "q8", "label": "Yeast extract", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml",
    "field_path": "ingredients[7].concentration", "stored": {"value": "0.197824",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[7].concentration", "stored": {"value": "0.197824",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[7].concentration", "stored": {"value": "0.197824",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml",
    "field_path": "ingredients[7].concentration", "stored": {"value": "0.197824",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml",
    "field_path": "ingredients[7].concentration", "stored": {"value": "0.197824",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml",
    "field_path": "ingredients[7].concentration", "stored": {"value": "0.197824",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml",
    "field_path": "ingredients[7].concentration", "stored": {"value": "0.197824",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml",
    "field_path": "ingredients[7].concentration", "stored": {"value": "0.197824",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml",
    "field_path": "ingredients[7].concentration", "stored": {"value": "0.197824",
    "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[7].concentration", "stored": {"value": "0.197824",
    "unit": "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner
    support, separate507 base conflict and unavailable KOMODO variants are distinguished
    in the layer decisions; no blanket transfer or approval of the ten encoded copies.",
    "source_stage": "main solutions with distinct source identities", "sources": [{"evidence_id":
    "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79",
    "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d",
    "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 11-11",
    "quote": "Yeast extract                                         0.20            g",
    "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[0].recipe[8]",
    "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\":
    \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\":
    0.2,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.197824,\n                        \"optional\": 0\n                    }", "quote_basis":
    "raw UTF-8"}, {"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4",
    "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7",
    "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 11-11",
    "quote": "Yeast extract                                            0.05         g",
    "quote_basis": "derivative text"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[0].recipe[8]",
    "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\":
    \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\":
    0.05,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.0489237,\n                        \"optional\": 0\n                    }", "quote_basis":
    "raw UTF-8"}], "layer_decisions": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml",
    "field_path": "ingredients[7].concentration", "decision": "evidence_only", "rationale":
    "The exact 507a API explicitly reports the encoded g_l on declared 1011 mL normalization;
    the PDF supports its batch mass. Attach evidence without claiming measured final
    volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[7].concentration", "decision": "conflict", "rationale":
    "The local507a-derived quantity conflicts with or is absent from the separately
    identified 507 base table. Resolve that source identity before correcting this
    maintained owner; do not transfer507a amounts."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[7].concentration", "decision": "evidence_only", "rationale":
    "The exact 507a API explicitly reports the encoded g_l on declared 1011 mL normalization;
    the PDF supports its batch mass. Attach evidence without claiming measured final
    volume."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path":
    "ingredients[7].concentration", "decision": "unsupported", "rationale": "The exact
    KOMODO variant endpoint returned 403. Its local copied signature and base-source
    link do not authenticate this amount. Preserve unresolved variant provenance pending
    exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml",
    "field_path": "ingredients[7].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ingredients[7].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml",
    "field_path": "ingredients[7].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[7].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml",
    "field_path": "ingredients[7].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[7].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id":
    "q9", "label": "Na2-EDTA", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml",
    "field_path": "ingredients[8].concentration", "stored": {"value": "0.5", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[8].concentration", "stored": {"value": "0.5", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[8].concentration", "stored": {"value": "0.5", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path":
    "ingredients[8].concentration", "stored": {"value": "0.5", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[8].concentration",
    "stored": {"value": "0.5", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml",
    "field_path": "ingredients[8].concentration", "stored": {"value": "0.5", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path":
    "ingredients[8].concentration", "stored": {"value": "0.5", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[8].concentration",
    "stored": {"value": "0.5", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml",
    "field_path": "ingredients[8].concentration", "stored": {"value": "0.5", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[8].concentration", "stored": {"value": "0.5", "unit":
    "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner support,
    separate507 base conflict and unavailable KOMODO variants are distinguished in
    the layer decisions; no blanket transfer or approval of the ten encoded copies.",
    "source_stage": "distinct SL-4 and SL-11 stocks", "sources": [{"evidence_id":
    "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79",
    "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d",
    "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 29-29",
    "quote": "Na2-EDTA                                                 0.50         g",
    "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[1].recipe[0]",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"Na2-EDTA\",\n                        \"compound_id\": 34,\n                        \"amount\":
    0.5,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.5,\n                        \"mmol_l\": 1.48718,\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}, {"evidence_id": "dsm507",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4",
    "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7",
    "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 44-44",
    "quote": "Na2-EDTA x 2 H2O                                          5.20        g",
    "quote_basis": "derivative text"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[1].recipe[0]",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"Na2-EDTA x 2 H2O\",\n                        \"compound_id\": 676,\n                        \"amount\":
    5.2,\n                        \"unit\": \"g\",\n                        \"g_l\":
    5.2,\n                        \"mmol_l\": 15.4667,\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}], "layer_decisions": [{"path":
    "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path":
    "ingredients[8].concentration", "decision": "correct", "rationale": "This is a
    declared SL-4 stock quantity flattened into main ingredients. Restore the source
    stock and 10 mL batch addition; water input alone does not establish measured
    stock or receiving final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[8].concentration", "decision": "conflict", "rationale":
    "The local SL-4-like item cannot substitute for the differently composed SL-11
    embedded in507. Its source stock must be resolved separately, retaining exact
    salt form and batch/final-makeup scope."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[8].concentration", "decision": "correct", "rationale":
    "This is a declared SL-4 stock quantity flattened into main ingredients. Restore
    the source stock and 10 mL batch addition; water input alone does not establish
    measured stock or receiving final volume."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml",
    "field_path": "ingredients[8].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[8].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml",
    "field_path": "ingredients[8].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[8].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml",
    "field_path": "ingredients[8].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path":
    "ingredients[8].concentration", "decision": "unsupported", "rationale": "The exact
    KOMODO variant endpoint returned 403. Its local copied signature and base-source
    link do not authenticate this amount. Preserve unresolved variant provenance pending
    exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[8].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id":
    "q10", "label": "FeSO4 x 7 H2O", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml",
    "field_path": "ingredients[9].concentration", "stored": {"value": "0.2", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[9].concentration", "stored": {"value": "0.2", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[9].concentration", "stored": {"value": "0.2", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path":
    "ingredients[9].concentration", "stored": {"value": "0.2", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[9].concentration",
    "stored": {"value": "0.2", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml",
    "field_path": "ingredients[9].concentration", "stored": {"value": "0.2", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path":
    "ingredients[9].concentration", "stored": {"value": "0.2", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[9].concentration",
    "stored": {"value": "0.2", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml",
    "field_path": "ingredients[9].concentration", "stored": {"value": "0.2", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[9].concentration", "stored": {"value": "0.2", "unit":
    "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner support,
    separate507 base conflict and unavailable KOMODO variants are distinguished in
    the layer decisions; no blanket transfer or approval of the ten encoded copies.",
    "source_stage": "distinct SL-4 and SL-11 stocks", "sources": [{"evidence_id":
    "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79",
    "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d",
    "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 30-30",
    "quote": "FeSO4 x 7 H2O                                            0.20         g",
    "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[1].recipe[1]",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\":
    0.2,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.2,\n                        \"mmol_l\": 0.719386,\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}, {"evidence_id": "dsm507",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4",
    "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7",
    "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 45-45",
    "quote": "FeCl2 x 4 H2O                                             1.50        g",
    "quote_basis": "derivative text"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[1].recipe[1]",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"FeCl2 x 4 H2O\",\n                        \"compound_id\": 260,\n                        \"amount\":
    1.5,\n                        \"unit\": \"g\",\n                        \"g_l\":
    1.5,\n                        \"mmol_l\": 7.54482,\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}], "layer_decisions": [{"path":
    "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path":
    "ingredients[9].concentration", "decision": "correct", "rationale": "This is a
    declared SL-4 stock quantity flattened into main ingredients. Restore the source
    stock and 10 mL batch addition; water input alone does not establish measured
    stock or receiving final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[9].concentration", "decision": "conflict", "rationale":
    "The local SL-4-like item cannot substitute for the differently composed SL-11
    embedded in507. Its source stock must be resolved separately, retaining exact
    salt form and batch/final-makeup scope."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[9].concentration", "decision": "correct", "rationale":
    "This is a declared SL-4 stock quantity flattened into main ingredients. Restore
    the source stock and 10 mL batch addition; water input alone does not establish
    measured stock or receiving final volume."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml",
    "field_path": "ingredients[9].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[9].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml",
    "field_path": "ingredients[9].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[9].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml",
    "field_path": "ingredients[9].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path":
    "ingredients[9].concentration", "decision": "unsupported", "rationale": "The exact
    KOMODO variant endpoint returned 403. Its local copied signature and base-source
    link do not authenticate this amount. Preserve unresolved variant provenance pending
    exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[9].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id":
    "q11", "label": "ZnSO4 x 7 H2O", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml",
    "field_path": "ingredients[10].concentration", "stored": {"value": "0.1", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[10].concentration", "stored": {"value": "0.1", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[10].concentration", "stored": {"value": "0.1", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path":
    "ingredients[10].concentration", "stored": {"value": "0.1", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[10].concentration",
    "stored": {"value": "0.1", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml",
    "field_path": "ingredients[10].concentration", "stored": {"value": "0.1", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path":
    "ingredients[10].concentration", "stored": {"value": "0.1", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[10].concentration",
    "stored": {"value": "0.1", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml",
    "field_path": "ingredients[10].concentration", "stored": {"value": "0.1", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[10].concentration", "stored": {"value": "0.1", "unit":
    "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner support,
    separate507 base conflict and unavailable KOMODO variants are distinguished in
    the layer decisions; no blanket transfer or approval of the ten encoded copies.",
    "source_stage": "distinct SL-4 and SL-11 stocks", "sources": [{"evidence_id":
    "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79",
    "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d",
    "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 31-31",
    "quote": "ZnSO4 x 7 H2O                                            0.10         g",
    "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[1].recipe[2]",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\":
    0.1,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.1,\n                        \"mmol_l\": 0.347752,\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}, {"evidence_id": "dsm507",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4",
    "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7",
    "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 54-54",
    "quote": "ZnCl2                                                   70.00      mg",
    "quote_basis": "derivative text"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[1].recipe[2]",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"ZnCl2\",\n                        \"compound_id\": 64,\n                        \"amount\":
    70,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.07,\n                        \"mmol_l\": 0.513573,\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}], "layer_decisions": [{"path":
    "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path":
    "ingredients[10].concentration", "decision": "correct", "rationale": "This is
    a declared SL-4 stock quantity flattened into main ingredients. Restore the source
    stock and 10 mL batch addition; water input alone does not establish measured
    stock or receiving final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[10].concentration", "decision": "conflict", "rationale":
    "The local SL-4-like item cannot substitute for the differently composed SL-11
    embedded in507. Its source stock must be resolved separately, retaining exact
    salt form and batch/final-makeup scope."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[10].concentration", "decision": "correct", "rationale":
    "This is a declared SL-4 stock quantity flattened into main ingredients. Restore
    the source stock and 10 mL batch addition; water input alone does not establish
    measured stock or receiving final volume."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml",
    "field_path": "ingredients[10].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[10].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml",
    "field_path": "ingredients[10].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[10].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml",
    "field_path": "ingredients[10].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path":
    "ingredients[10].concentration", "decision": "unsupported", "rationale": "The
    exact KOMODO variant endpoint returned 403. Its local copied signature and base-source
    link do not authenticate this amount. Preserve unresolved variant provenance pending
    exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[10].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id":
    "q12", "label": "MnCl2 x 4 H2O", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml",
    "field_path": "ingredients[11].concentration", "stored": {"value": "0.03", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[11].concentration", "stored": {"value": "0.03", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[11].concentration", "stored": {"value": "0.03", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path":
    "ingredients[11].concentration", "stored": {"value": "0.03", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[11].concentration",
    "stored": {"value": "0.03", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml",
    "field_path": "ingredients[11].concentration", "stored": {"value": "0.03", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path":
    "ingredients[11].concentration", "stored": {"value": "0.03", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[11].concentration",
    "stored": {"value": "0.03", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml",
    "field_path": "ingredients[11].concentration", "stored": {"value": "0.03", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[11].concentration", "stored": {"value": "0.03", "unit":
    "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner support,
    separate507 base conflict and unavailable KOMODO variants are distinguished in
    the layer decisions; no blanket transfer or approval of the ten encoded copies.",
    "source_stage": "distinct SL-4 and SL-11 stocks", "sources": [{"evidence_id":
    "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79",
    "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d",
    "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 32-32",
    "quote": "MnCl2 x 4 H2O                                            0.03         g",
    "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[1].recipe[3]",
    "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\":
    0.03,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.03,\n                        \"mmol_l\": 0.151588,\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}, {"evidence_id": "dsm507",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4",
    "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7",
    "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 55-55",
    "quote": "MnCl2 x 4 H2O                                          100.00      mg",
    "quote_basis": "derivative text"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[1].recipe[3]",
    "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\":
    100,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.1,\n                        \"mmol_l\": 0.505293,\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}], "layer_decisions": [{"path":
    "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path":
    "ingredients[11].concentration", "decision": "correct", "rationale": "This is
    a declared SL-4 stock quantity flattened into main ingredients. Restore the source
    stock and 10 mL batch addition; water input alone does not establish measured
    stock or receiving final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[11].concentration", "decision": "conflict", "rationale":
    "The local SL-4-like item cannot substitute for the differently composed SL-11
    embedded in507. Its source stock must be resolved separately, retaining exact
    salt form and batch/final-makeup scope."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[11].concentration", "decision": "correct", "rationale":
    "This is a declared SL-4 stock quantity flattened into main ingredients. Restore
    the source stock and 10 mL batch addition; water input alone does not establish
    measured stock or receiving final volume."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml",
    "field_path": "ingredients[11].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[11].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml",
    "field_path": "ingredients[11].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[11].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml",
    "field_path": "ingredients[11].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path":
    "ingredients[11].concentration", "decision": "unsupported", "rationale": "The
    exact KOMODO variant endpoint returned 403. Its local copied signature and base-source
    link do not authenticate this amount. Preserve unresolved variant provenance pending
    exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[11].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id":
    "q13", "label": "H3BO3", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml",
    "field_path": "ingredients[12].concentration", "stored": {"value": "0.3", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[12].concentration", "stored": {"value": "0.3", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[12].concentration", "stored": {"value": "0.3", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path":
    "ingredients[12].concentration", "stored": {"value": "0.3", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[12].concentration",
    "stored": {"value": "0.3", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml",
    "field_path": "ingredients[12].concentration", "stored": {"value": "0.3", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path":
    "ingredients[12].concentration", "stored": {"value": "0.3", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[12].concentration",
    "stored": {"value": "0.3", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml",
    "field_path": "ingredients[12].concentration", "stored": {"value": "0.3", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[12].concentration", "stored": {"value": "0.3", "unit":
    "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner support,
    separate507 base conflict and unavailable KOMODO variants are distinguished in
    the layer decisions; no blanket transfer or approval of the ten encoded copies.",
    "source_stage": "distinct SL-4 and SL-11 stocks", "sources": [{"evidence_id":
    "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79",
    "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d",
    "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 33-33",
    "quote": "H3BO3                                                    0.30         g",
    "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[1].recipe[4]",
    "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\":
    0.3,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.3,\n                        \"mmol_l\": 4.85123,\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}, {"evidence_id": "dsm507",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4",
    "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7",
    "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 56-56",
    "quote": "H3BO3                                                    6.00      mg",
    "quote_basis": "derivative text"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[1].recipe[4]",
    "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\":
    6,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.006,\n                        \"mmol_l\": 0.0970246,\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}], "layer_decisions": [{"path":
    "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path":
    "ingredients[12].concentration", "decision": "correct", "rationale": "This is
    a declared SL-4 stock quantity flattened into main ingredients. Restore the source
    stock and 10 mL batch addition; water input alone does not establish measured
    stock or receiving final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[12].concentration", "decision": "conflict", "rationale":
    "The local SL-4-like item cannot substitute for the differently composed SL-11
    embedded in507. Its source stock must be resolved separately, retaining exact
    salt form and batch/final-makeup scope."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[12].concentration", "decision": "correct", "rationale":
    "This is a declared SL-4 stock quantity flattened into main ingredients. Restore
    the source stock and 10 mL batch addition; water input alone does not establish
    measured stock or receiving final volume."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml",
    "field_path": "ingredients[12].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[12].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml",
    "field_path": "ingredients[12].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[12].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml",
    "field_path": "ingredients[12].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path":
    "ingredients[12].concentration", "decision": "unsupported", "rationale": "The
    exact KOMODO variant endpoint returned 403. Its local copied signature and base-source
    link do not authenticate this amount. Preserve unresolved variant provenance pending
    exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[12].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id":
    "q14", "label": "CoCl2 x 6 H2O", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml",
    "field_path": "ingredients[13].concentration", "stored": {"value": "0.2", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[13].concentration", "stored": {"value": "0.2", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[13].concentration", "stored": {"value": "0.2", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path":
    "ingredients[13].concentration", "stored": {"value": "0.2", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[13].concentration",
    "stored": {"value": "0.2", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml",
    "field_path": "ingredients[13].concentration", "stored": {"value": "0.2", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path":
    "ingredients[13].concentration", "stored": {"value": "0.2", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[13].concentration",
    "stored": {"value": "0.2", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml",
    "field_path": "ingredients[13].concentration", "stored": {"value": "0.2", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[13].concentration", "stored": {"value": "0.2", "unit":
    "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner support,
    separate507 base conflict and unavailable KOMODO variants are distinguished in
    the layer decisions; no blanket transfer or approval of the ten encoded copies.",
    "source_stage": "distinct SL-4 and SL-11 stocks", "sources": [{"evidence_id":
    "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79",
    "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d",
    "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 34-34",
    "quote": "CoCl2 x 6 H2O                                            0.20         g",
    "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[1].recipe[5]",
    "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\":
    \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\":
    0.2,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.2,\n                        \"mmol_l\": 1.54037,\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}, {"evidence_id": "dsm507",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4",
    "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7",
    "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 57-57",
    "quote": "CoCl2 x 6 H2O                                          190.00      mg",
    "quote_basis": "derivative text"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[1].recipe[5]",
    "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\":
    \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\":
    190,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.19,\n                        \"mmol_l\": 1.46335,\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}], "layer_decisions": [{"path":
    "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path":
    "ingredients[13].concentration", "decision": "correct", "rationale": "This is
    a declared SL-4 stock quantity flattened into main ingredients. Restore the source
    stock and 10 mL batch addition; water input alone does not establish measured
    stock or receiving final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[13].concentration", "decision": "conflict", "rationale":
    "The local SL-4-like item cannot substitute for the differently composed SL-11
    embedded in507. Its source stock must be resolved separately, retaining exact
    salt form and batch/final-makeup scope."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[13].concentration", "decision": "correct", "rationale":
    "This is a declared SL-4 stock quantity flattened into main ingredients. Restore
    the source stock and 10 mL batch addition; water input alone does not establish
    measured stock or receiving final volume."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml",
    "field_path": "ingredients[13].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[13].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml",
    "field_path": "ingredients[13].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[13].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml",
    "field_path": "ingredients[13].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path":
    "ingredients[13].concentration", "decision": "unsupported", "rationale": "The
    exact KOMODO variant endpoint returned 403. Its local copied signature and base-source
    link do not authenticate this amount. Preserve unresolved variant provenance pending
    exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[13].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id":
    "q15", "label": "CuCl2 x 2 H2O", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml",
    "field_path": "ingredients[14].concentration", "stored": {"value": "0.01", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[14].concentration", "stored": {"value": "0.01", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[14].concentration", "stored": {"value": "0.01", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path":
    "ingredients[14].concentration", "stored": {"value": "0.01", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[14].concentration",
    "stored": {"value": "0.01", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml",
    "field_path": "ingredients[14].concentration", "stored": {"value": "0.01", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path":
    "ingredients[14].concentration", "stored": {"value": "0.01", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[14].concentration",
    "stored": {"value": "0.01", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml",
    "field_path": "ingredients[14].concentration", "stored": {"value": "0.01", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[14].concentration", "stored": {"value": "0.01", "unit":
    "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner support,
    separate507 base conflict and unavailable KOMODO variants are distinguished in
    the layer decisions; no blanket transfer or approval of the ten encoded copies.",
    "source_stage": "distinct SL-4 and SL-11 stocks", "sources": [{"evidence_id":
    "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79",
    "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d",
    "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 35-35",
    "quote": "CuCl2 x 2 H2O                                            0.01         g",
    "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[1].recipe[6]",
    "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\":
    \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\":
    0.01,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.01,\n                        \"mmol_l\": 0.0586569,\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}, {"evidence_id": "dsm507",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4",
    "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7",
    "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 58-58",
    "quote": "CuCl2 x 2 H2O                                            2.00      mg",
    "quote_basis": "derivative text"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[1].recipe[6]",
    "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\":
    \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\":
    2,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.002,\n                        \"mmol_l\": 0.0117314,\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}], "layer_decisions": [{"path":
    "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path":
    "ingredients[14].concentration", "decision": "correct", "rationale": "This is
    a declared SL-4 stock quantity flattened into main ingredients. Restore the source
    stock and 10 mL batch addition; water input alone does not establish measured
    stock or receiving final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[14].concentration", "decision": "conflict", "rationale":
    "The local SL-4-like item cannot substitute for the differently composed SL-11
    embedded in507. Its source stock must be resolved separately, retaining exact
    salt form and batch/final-makeup scope."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[14].concentration", "decision": "correct", "rationale":
    "This is a declared SL-4 stock quantity flattened into main ingredients. Restore
    the source stock and 10 mL batch addition; water input alone does not establish
    measured stock or receiving final volume."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml",
    "field_path": "ingredients[14].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[14].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml",
    "field_path": "ingredients[14].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[14].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml",
    "field_path": "ingredients[14].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path":
    "ingredients[14].concentration", "decision": "unsupported", "rationale": "The
    exact KOMODO variant endpoint returned 403. Its local copied signature and base-source
    link do not authenticate this amount. Preserve unresolved variant provenance pending
    exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[14].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id":
    "q16", "label": "NiCl2 x 6 H2O", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml",
    "field_path": "ingredients[15].concentration", "stored": {"value": "0.02", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[15].concentration", "stored": {"value": "0.02", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[15].concentration", "stored": {"value": "0.02", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path":
    "ingredients[15].concentration", "stored": {"value": "0.02", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[15].concentration",
    "stored": {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml",
    "field_path": "ingredients[15].concentration", "stored": {"value": "0.02", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path":
    "ingredients[15].concentration", "stored": {"value": "0.02", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[15].concentration",
    "stored": {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml",
    "field_path": "ingredients[15].concentration", "stored": {"value": "0.02", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[15].concentration", "stored": {"value": "0.02", "unit":
    "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner support,
    separate507 base conflict and unavailable KOMODO variants are distinguished in
    the layer decisions; no blanket transfer or approval of the ten encoded copies.",
    "source_stage": "distinct SL-4 and SL-11 stocks", "sources": [{"evidence_id":
    "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79",
    "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d",
    "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 36-36",
    "quote": "NiCl2 x 6 H2O                                            0.02         g",
    "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[1].recipe[7]",
    "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\":
    \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\":
    0.02,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.02,\n                        \"mmol_l\": 0.154322,\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}, {"evidence_id": "dsm507",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4",
    "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7",
    "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 59-59",
    "quote": "NiCl2 x 6 H2O                                           24.00      mg",
    "quote_basis": "derivative text"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[1].recipe[7]",
    "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\":
    \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\":
    24,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.024,\n                        \"mmol_l\": 0.185187,\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}], "layer_decisions": [{"path":
    "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path":
    "ingredients[15].concentration", "decision": "correct", "rationale": "This is
    a declared SL-4 stock quantity flattened into main ingredients. Restore the source
    stock and 10 mL batch addition; water input alone does not establish measured
    stock or receiving final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[15].concentration", "decision": "conflict", "rationale":
    "The local SL-4-like item cannot substitute for the differently composed SL-11
    embedded in507. Its source stock must be resolved separately, retaining exact
    salt form and batch/final-makeup scope."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[15].concentration", "decision": "correct", "rationale":
    "This is a declared SL-4 stock quantity flattened into main ingredients. Restore
    the source stock and 10 mL batch addition; water input alone does not establish
    measured stock or receiving final volume."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml",
    "field_path": "ingredients[15].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[15].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml",
    "field_path": "ingredients[15].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[15].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml",
    "field_path": "ingredients[15].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path":
    "ingredients[15].concentration", "decision": "unsupported", "rationale": "The
    exact KOMODO variant endpoint returned 403. Its local copied signature and base-source
    link do not authenticate this amount. Preserve unresolved variant provenance pending
    exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[15].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id":
    "q17", "label": "Na2MoO4 x 2 H2O", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml",
    "field_path": "ingredients[16].concentration", "stored": {"value": "0.03", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[16].concentration", "stored": {"value": "0.03", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[16].concentration", "stored": {"value": "0.03", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path":
    "ingredients[16].concentration", "stored": {"value": "0.03", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[16].concentration",
    "stored": {"value": "0.03", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml",
    "field_path": "ingredients[16].concentration", "stored": {"value": "0.03", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path":
    "ingredients[16].concentration", "stored": {"value": "0.03", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[16].concentration",
    "stored": {"value": "0.03", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml",
    "field_path": "ingredients[16].concentration", "stored": {"value": "0.03", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[16].concentration", "stored": {"value": "0.03", "unit":
    "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner support,
    separate507 base conflict and unavailable KOMODO variants are distinguished in
    the layer decisions; no blanket transfer or approval of the ten encoded copies.",
    "source_stage": "distinct SL-4 and SL-11 stocks", "sources": [{"evidence_id":
    "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79",
    "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d",
    "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 37-37",
    "quote": "Na2MoO4 x 2 H2O                                          0.03         g",
    "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[1].recipe[8]",
    "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\":
    \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\":
    0.03,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.03,\n                        \"mmol_l\": 0.123993,\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}, {"evidence_id": "dsm507",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4",
    "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7",
    "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 60-60",
    "quote": "Na2MoO4 x 2 H2O                                         36.00      mg",
    "quote_basis": "derivative text"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[1].recipe[8]",
    "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\":
    \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\":
    36,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.036,\n                        \"mmol_l\": 0.148791,\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}], "layer_decisions": [{"path":
    "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path":
    "ingredients[16].concentration", "decision": "correct", "rationale": "This is
    a declared SL-4 stock quantity flattened into main ingredients. Restore the source
    stock and 10 mL batch addition; water input alone does not establish measured
    stock or receiving final volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[16].concentration", "decision": "conflict", "rationale":
    "The local SL-4-like item cannot substitute for the differently composed SL-11
    embedded in507. Its source stock must be resolved separately, retaining exact
    salt form and batch/final-makeup scope."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[16].concentration", "decision": "correct", "rationale":
    "This is a declared SL-4 stock quantity flattened into main ingredients. Restore
    the source stock and 10 mL batch addition; water input alone does not establish
    measured stock or receiving final volume."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml",
    "field_path": "ingredients[16].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[16].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml",
    "field_path": "ingredients[16].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[16].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml",
    "field_path": "ingredients[16].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path":
    "ingredients[16].concentration", "decision": "unsupported", "rationale": "The
    exact KOMODO variant endpoint returned 403. Its local copied signature and base-source
    link do not authenticate this amount. Preserve unresolved variant provenance pending
    exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[16].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id":
    "q18", "label": "Biotin", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml",
    "field_path": "ingredients[17].concentration", "stored": {"value": "0.02", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[17].concentration", "stored": {"value": "0.02", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[17].concentration", "stored": {"value": "0.02", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path":
    "ingredients[17].concentration", "stored": {"value": "0.02", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[17].concentration",
    "stored": {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml",
    "field_path": "ingredients[17].concentration", "stored": {"value": "0.02", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path":
    "ingredients[17].concentration", "stored": {"value": "0.02", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[17].concentration",
    "stored": {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml",
    "field_path": "ingredients[17].concentration", "stored": {"value": "0.02", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[17].concentration", "stored": {"value": "0.02", "unit":
    "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner support,
    separate507 base conflict and unavailable KOMODO variants are distinguished in
    the layer decisions; no blanket transfer or approval of the ten encoded copies.",
    "source_stage": "Wolin vitamin stock", "sources": [{"evidence_id": "dsm507a",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79",
    "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d",
    "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 46-46",
    "quote": "Biotin                                                   20.00      mg",
    "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[2].recipe[0]",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\":
    20,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}, {"evidence_id": "api507",
    "reference": "https://mediadive.dsmz.de/rest/medium/507", "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw",
    "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[2].recipe[0]",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\":
    20,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}], "layer_decisions": [{"path":
    "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path":
    "ingredients[17].concentration", "decision": "correct", "rationale": "The supported
    stock concentration is flattened into the main ingredients. Restore the vitamin
    stock and 1 mL batch addition without inventing a receiving-litre denominator."},
    {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[17].concentration", "decision": "correct", "rationale":
    "Both primary recipes place this item in the vitamin stock, not directly in the
    main medium. Matching stock composition does not authenticate the complete medium
    or any separate KOMODO variant."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[17].concentration", "decision": "correct", "rationale":
    "The supported stock concentration is flattened into the main ingredients. Restore
    the vitamin stock and 1 mL batch addition without inventing a receiving-litre
    denominator."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml",
    "field_path": "ingredients[17].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[17].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml",
    "field_path": "ingredients[17].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[17].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml",
    "field_path": "ingredients[17].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path":
    "ingredients[17].concentration", "decision": "unsupported", "rationale": "The
    exact KOMODO variant endpoint returned 403. Its local copied signature and base-source
    link do not authenticate this amount. Preserve unresolved variant provenance pending
    exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[17].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id":
    "q19", "label": "Folic acid", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml",
    "field_path": "ingredients[18].concentration", "stored": {"value": "0.02", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[18].concentration", "stored": {"value": "0.02", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[18].concentration", "stored": {"value": "0.02", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path":
    "ingredients[18].concentration", "stored": {"value": "0.02", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[18].concentration",
    "stored": {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml",
    "field_path": "ingredients[18].concentration", "stored": {"value": "0.02", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path":
    "ingredients[18].concentration", "stored": {"value": "0.02", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[18].concentration",
    "stored": {"value": "0.02", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml",
    "field_path": "ingredients[18].concentration", "stored": {"value": "0.02", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[18].concentration", "stored": {"value": "0.02", "unit":
    "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner support,
    separate507 base conflict and unavailable KOMODO variants are distinguished in
    the layer decisions; no blanket transfer or approval of the ten encoded copies.",
    "source_stage": "Wolin vitamin stock", "sources": [{"evidence_id": "dsm507a",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79",
    "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d",
    "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 56-56",
    "quote": "Folic acid                             20.00   mg", "quote_basis": "derivative
    text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[2].recipe[1]",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\":
    20,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.02,\n                        \"mmol_l\": 0.0453104,\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}, {"evidence_id": "api507",
    "reference": "https://mediadive.dsmz.de/rest/medium/507", "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw",
    "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[2].recipe[1]",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\":
    20,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.02,\n                        \"mmol_l\": 0.0453104,\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}], "layer_decisions": [{"path":
    "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path":
    "ingredients[18].concentration", "decision": "correct", "rationale": "The supported
    stock concentration is flattened into the main ingredients. Restore the vitamin
    stock and 1 mL batch addition without inventing a receiving-litre denominator."},
    {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[18].concentration", "decision": "correct", "rationale":
    "Both primary recipes place this item in the vitamin stock, not directly in the
    main medium. Matching stock composition does not authenticate the complete medium
    or any separate KOMODO variant."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[18].concentration", "decision": "correct", "rationale":
    "The supported stock concentration is flattened into the main ingredients. Restore
    the vitamin stock and 1 mL batch addition without inventing a receiving-litre
    denominator."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml",
    "field_path": "ingredients[18].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[18].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml",
    "field_path": "ingredients[18].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[18].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml",
    "field_path": "ingredients[18].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path":
    "ingredients[18].concentration", "decision": "unsupported", "rationale": "The
    exact KOMODO variant endpoint returned 403. Its local copied signature and base-source
    link do not authenticate this amount. Preserve unresolved variant provenance pending
    exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[18].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id":
    "q20", "label": "Pyridoxine hydrochloride", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml",
    "field_path": "ingredients[19].concentration", "stored": {"value": "0.1", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[19].concentration", "stored": {"value": "0.1", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[19].concentration", "stored": {"value": "0.1", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path":
    "ingredients[19].concentration", "stored": {"value": "0.1", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[19].concentration",
    "stored": {"value": "0.1", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml",
    "field_path": "ingredients[19].concentration", "stored": {"value": "0.1", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path":
    "ingredients[19].concentration", "stored": {"value": "0.1", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[19].concentration",
    "stored": {"value": "0.1", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml",
    "field_path": "ingredients[19].concentration", "stored": {"value": "0.1", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[19].concentration", "stored": {"value": "0.1", "unit":
    "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner support,
    separate507 base conflict and unavailable KOMODO variants are distinguished in
    the layer decisions; no blanket transfer or approval of the ten encoded copies.",
    "source_stage": "Wolin vitamin stock", "sources": [{"evidence_id": "dsm507a",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79",
    "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d",
    "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 57-57",
    "quote": "Pyridoxine hydrochloride              100.00   mg", "quote_basis": "derivative
    text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[2].recipe[2]",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\":
    100,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.1,\n                        \"mmol_l\": 0.486287,\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}, {"evidence_id": "api507",
    "reference": "https://mediadive.dsmz.de/rest/medium/507", "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw",
    "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[2].recipe[2]",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\":
    100,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.1,\n                        \"mmol_l\": 0.486287,\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}], "layer_decisions": [{"path":
    "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path":
    "ingredients[19].concentration", "decision": "correct", "rationale": "The supported
    stock concentration is flattened into the main ingredients. Restore the vitamin
    stock and 1 mL batch addition without inventing a receiving-litre denominator."},
    {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[19].concentration", "decision": "correct", "rationale":
    "Both primary recipes place this item in the vitamin stock, not directly in the
    main medium. Matching stock composition does not authenticate the complete medium
    or any separate KOMODO variant."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[19].concentration", "decision": "correct", "rationale":
    "The supported stock concentration is flattened into the main ingredients. Restore
    the vitamin stock and 1 mL batch addition without inventing a receiving-litre
    denominator."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml",
    "field_path": "ingredients[19].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[19].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml",
    "field_path": "ingredients[19].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[19].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml",
    "field_path": "ingredients[19].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path":
    "ingredients[19].concentration", "decision": "unsupported", "rationale": "The
    exact KOMODO variant endpoint returned 403. Its local copied signature and base-source
    link do not authenticate this amount. Preserve unresolved variant provenance pending
    exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[19].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id":
    "q21", "label": "Thiamine HCl", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml",
    "field_path": "ingredients[20].concentration", "stored": {"value": "0.05", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[20].concentration", "stored": {"value": "0.05", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[20].concentration", "stored": {"value": "0.05", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path":
    "ingredients[20].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[20].concentration",
    "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml",
    "field_path": "ingredients[20].concentration", "stored": {"value": "0.05", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path":
    "ingredients[20].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[20].concentration",
    "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml",
    "field_path": "ingredients[20].concentration", "stored": {"value": "0.05", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[20].concentration", "stored": {"value": "0.05", "unit":
    "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner support,
    separate507 base conflict and unavailable KOMODO variants are distinguished in
    the layer decisions; no blanket transfer or approval of the ten encoded copies.",
    "source_stage": "Wolin vitamin stock", "sources": [{"evidence_id": "dsm507a",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79",
    "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d",
    "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 58-58",
    "quote": "Thiamine HCl                           50.00   mg", "quote_basis": "derivative
    text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[2].recipe[3]",
    "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\":
    50,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.05,\n                        \"mmol_l\": 0.148236,\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}, {"evidence_id": "api507",
    "reference": "https://mediadive.dsmz.de/rest/medium/507", "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw",
    "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[2].recipe[3]",
    "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\":
    50,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.05,\n                        \"mmol_l\": 0.148236,\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}], "layer_decisions": [{"path":
    "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path":
    "ingredients[20].concentration", "decision": "correct", "rationale": "The supported
    stock concentration is flattened into the main ingredients. Restore the vitamin
    stock and 1 mL batch addition without inventing a receiving-litre denominator."},
    {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[20].concentration", "decision": "correct", "rationale":
    "Both primary recipes place this item in the vitamin stock, not directly in the
    main medium. Matching stock composition does not authenticate the complete medium
    or any separate KOMODO variant."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[20].concentration", "decision": "correct", "rationale":
    "The supported stock concentration is flattened into the main ingredients. Restore
    the vitamin stock and 1 mL batch addition without inventing a receiving-litre
    denominator."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml",
    "field_path": "ingredients[20].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[20].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml",
    "field_path": "ingredients[20].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[20].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml",
    "field_path": "ingredients[20].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path":
    "ingredients[20].concentration", "decision": "unsupported", "rationale": "The
    exact KOMODO variant endpoint returned 403. Its local copied signature and base-source
    link do not authenticate this amount. Preserve unresolved variant provenance pending
    exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[20].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id":
    "q22", "label": "Riboflavin", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml",
    "field_path": "ingredients[21].concentration", "stored": {"value": "0.05", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[21].concentration", "stored": {"value": "0.05", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[21].concentration", "stored": {"value": "0.05", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path":
    "ingredients[21].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[21].concentration",
    "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml",
    "field_path": "ingredients[21].concentration", "stored": {"value": "0.05", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path":
    "ingredients[21].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[21].concentration",
    "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml",
    "field_path": "ingredients[21].concentration", "stored": {"value": "0.05", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[21].concentration", "stored": {"value": "0.05", "unit":
    "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner support,
    separate507 base conflict and unavailable KOMODO variants are distinguished in
    the layer decisions; no blanket transfer or approval of the ten encoded copies.",
    "source_stage": "Wolin vitamin stock", "sources": [{"evidence_id": "dsm507a",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79",
    "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d",
    "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 59-59",
    "quote": "Riboflavin                             50.00   mg", "quote_basis": "derivative
    text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[2].recipe[4]",
    "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\":
    50,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.05,\n                        \"mmol_l\": 0.132837,\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}, {"evidence_id": "api507",
    "reference": "https://mediadive.dsmz.de/rest/medium/507", "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw",
    "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[2].recipe[4]",
    "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\":
    50,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.05,\n                        \"mmol_l\": 0.132837,\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}], "layer_decisions": [{"path":
    "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path":
    "ingredients[21].concentration", "decision": "correct", "rationale": "The supported
    stock concentration is flattened into the main ingredients. Restore the vitamin
    stock and 1 mL batch addition without inventing a receiving-litre denominator."},
    {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[21].concentration", "decision": "correct", "rationale":
    "Both primary recipes place this item in the vitamin stock, not directly in the
    main medium. Matching stock composition does not authenticate the complete medium
    or any separate KOMODO variant."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[21].concentration", "decision": "correct", "rationale":
    "The supported stock concentration is flattened into the main ingredients. Restore
    the vitamin stock and 1 mL batch addition without inventing a receiving-litre
    denominator."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml",
    "field_path": "ingredients[21].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[21].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml",
    "field_path": "ingredients[21].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[21].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml",
    "field_path": "ingredients[21].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path":
    "ingredients[21].concentration", "decision": "unsupported", "rationale": "The
    exact KOMODO variant endpoint returned 403. Its local copied signature and base-source
    link do not authenticate this amount. Preserve unresolved variant provenance pending
    exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[21].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id":
    "q23", "label": "Nicotinic acid", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml",
    "field_path": "ingredients[22].concentration", "stored": {"value": "0.05", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[22].concentration", "stored": {"value": "0.05", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[22].concentration", "stored": {"value": "0.05", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path":
    "ingredients[22].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[22].concentration",
    "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml",
    "field_path": "ingredients[22].concentration", "stored": {"value": "0.05", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path":
    "ingredients[22].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[22].concentration",
    "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml",
    "field_path": "ingredients[22].concentration", "stored": {"value": "0.05", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[22].concentration", "stored": {"value": "0.05", "unit":
    "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner support,
    separate507 base conflict and unavailable KOMODO variants are distinguished in
    the layer decisions; no blanket transfer or approval of the ten encoded copies.",
    "source_stage": "Wolin vitamin stock", "sources": [{"evidence_id": "dsm507a",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79",
    "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d",
    "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 60-60",
    "quote": "Nicotinic acid                         50.00   mg", "quote_basis": "derivative
    text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[2].recipe[5]",
    "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\":
    \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\":
    50,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.05,\n                        \"mmol_l\": 0.406141,\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}, {"evidence_id": "api507",
    "reference": "https://mediadive.dsmz.de/rest/medium/507", "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw",
    "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[2].recipe[5]",
    "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\":
    \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\":
    50,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.05,\n                        \"mmol_l\": 0.406141,\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}], "layer_decisions": [{"path":
    "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path":
    "ingredients[22].concentration", "decision": "correct", "rationale": "The supported
    stock concentration is flattened into the main ingredients. Restore the vitamin
    stock and 1 mL batch addition without inventing a receiving-litre denominator."},
    {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[22].concentration", "decision": "correct", "rationale":
    "Both primary recipes place this item in the vitamin stock, not directly in the
    main medium. Matching stock composition does not authenticate the complete medium
    or any separate KOMODO variant."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[22].concentration", "decision": "correct", "rationale":
    "The supported stock concentration is flattened into the main ingredients. Restore
    the vitamin stock and 1 mL batch addition without inventing a receiving-litre
    denominator."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml",
    "field_path": "ingredients[22].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[22].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml",
    "field_path": "ingredients[22].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[22].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml",
    "field_path": "ingredients[22].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path":
    "ingredients[22].concentration", "decision": "unsupported", "rationale": "The
    exact KOMODO variant endpoint returned 403. Its local copied signature and base-source
    link do not authenticate this amount. Preserve unresolved variant provenance pending
    exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[22].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id":
    "q24", "label": "Calcium D-(+)-pantothenate", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml",
    "field_path": "ingredients[23].concentration", "stored": {"value": "0.05", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[23].concentration", "stored": {"value": "0.05", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[23].concentration", "stored": {"value": "0.05", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path":
    "ingredients[23].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[23].concentration",
    "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml",
    "field_path": "ingredients[23].concentration", "stored": {"value": "0.05", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path":
    "ingredients[23].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[23].concentration",
    "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml",
    "field_path": "ingredients[23].concentration", "stored": {"value": "0.05", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[23].concentration", "stored": {"value": "0.05", "unit":
    "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner support,
    separate507 base conflict and unavailable KOMODO variants are distinguished in
    the layer decisions; no blanket transfer or approval of the ten encoded copies.",
    "source_stage": "Wolin vitamin stock", "sources": [{"evidence_id": "dsm507a",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79",
    "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d",
    "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 61-61",
    "quote": "Calcium D-(+)-pantothenate             50.00   mg", "quote_basis": "derivative
    text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[2].recipe[6]",
    "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\":
    \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\": 1512,\n                        \"amount\":
    50,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.05,\n                        \"mmol_l\": 0.209846,\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}, {"evidence_id": "api507",
    "reference": "https://mediadive.dsmz.de/rest/medium/507", "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw",
    "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[2].recipe[6]",
    "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\":
    \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\": 1512,\n                        \"amount\":
    50,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.05,\n                        \"mmol_l\": 0.209846,\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}], "layer_decisions": [{"path":
    "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path":
    "ingredients[23].concentration", "decision": "correct", "rationale": "The supported
    stock concentration is flattened into the main ingredients. Restore the vitamin
    stock and 1 mL batch addition without inventing a receiving-litre denominator."},
    {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[23].concentration", "decision": "correct", "rationale":
    "Both primary recipes place this item in the vitamin stock, not directly in the
    main medium. Matching stock composition does not authenticate the complete medium
    or any separate KOMODO variant."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[23].concentration", "decision": "correct", "rationale":
    "The supported stock concentration is flattened into the main ingredients. Restore
    the vitamin stock and 1 mL batch addition without inventing a receiving-litre
    denominator."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml",
    "field_path": "ingredients[23].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[23].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml",
    "field_path": "ingredients[23].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[23].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml",
    "field_path": "ingredients[23].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path":
    "ingredients[23].concentration", "decision": "unsupported", "rationale": "The
    exact KOMODO variant endpoint returned 403. Its local copied signature and base-source
    link do not authenticate this amount. Preserve unresolved variant provenance pending
    exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[23].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id":
    "q25", "label": "Vitamin B12", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml",
    "field_path": "ingredients[24].concentration", "stored": {"value": "0.001", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[24].concentration", "stored": {"value": "0.001", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[24].concentration", "stored": {"value": "0.001", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path":
    "ingredients[24].concentration", "stored": {"value": "0.001", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[24].concentration",
    "stored": {"value": "0.001", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml",
    "field_path": "ingredients[24].concentration", "stored": {"value": "0.001", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path":
    "ingredients[24].concentration", "stored": {"value": "0.001", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[24].concentration",
    "stored": {"value": "0.001", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml",
    "field_path": "ingredients[24].concentration", "stored": {"value": "0.001", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[24].concentration", "stored": {"value": "0.001", "unit":
    "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner support,
    separate507 base conflict and unavailable KOMODO variants are distinguished in
    the layer decisions; no blanket transfer or approval of the ten encoded copies.",
    "source_stage": "Wolin vitamin stock", "sources": [{"evidence_id": "dsm507a",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79",
    "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d",
    "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 62-62",
    "quote": "Vitamin B12                             1.00   mg", "quote_basis": "derivative
    text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[2].recipe[7]",
    "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\":
    \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\":
    1,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.001,\n                        \"mmol_l\": 0.00073779,\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}, {"evidence_id": "api507",
    "reference": "https://mediadive.dsmz.de/rest/medium/507", "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw",
    "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[2].recipe[7]",
    "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\":
    \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\":
    1,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.001,\n                        \"mmol_l\": 0.00073779,\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}], "layer_decisions": [{"path":
    "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path":
    "ingredients[24].concentration", "decision": "correct", "rationale": "The supported
    stock concentration is flattened into the main ingredients. Restore the vitamin
    stock and 1 mL batch addition without inventing a receiving-litre denominator."},
    {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[24].concentration", "decision": "correct", "rationale":
    "Both primary recipes place this item in the vitamin stock, not directly in the
    main medium. Matching stock composition does not authenticate the complete medium
    or any separate KOMODO variant."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[24].concentration", "decision": "correct", "rationale":
    "The supported stock concentration is flattened into the main ingredients. Restore
    the vitamin stock and 1 mL batch addition without inventing a receiving-litre
    denominator."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml",
    "field_path": "ingredients[24].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[24].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml",
    "field_path": "ingredients[24].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[24].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml",
    "field_path": "ingredients[24].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path":
    "ingredients[24].concentration", "decision": "unsupported", "rationale": "The
    exact KOMODO variant endpoint returned 403. Its local copied signature and base-source
    link do not authenticate this amount. Preserve unresolved variant provenance pending
    exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[24].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id":
    "q26", "label": "p-Aminobenzoic acid", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml",
    "field_path": "ingredients[25].concentration", "stored": {"value": "0.05", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[25].concentration", "stored": {"value": "0.05", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[25].concentration", "stored": {"value": "0.05", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path":
    "ingredients[25].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[25].concentration",
    "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml",
    "field_path": "ingredients[25].concentration", "stored": {"value": "0.05", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path":
    "ingredients[25].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[25].concentration",
    "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml",
    "field_path": "ingredients[25].concentration", "stored": {"value": "0.05", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[25].concentration", "stored": {"value": "0.05", "unit":
    "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner support,
    separate507 base conflict and unavailable KOMODO variants are distinguished in
    the layer decisions; no blanket transfer or approval of the ten encoded copies.",
    "source_stage": "Wolin vitamin stock", "sources": [{"evidence_id": "dsm507a",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79",
    "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d",
    "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 63-63",
    "quote": "p-Aminobenzoic acid                    50.00   mg", "quote_basis": "derivative
    text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[2].recipe[8]",
    "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\":
    \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\":
    50,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.05,\n                        \"mmol_l\": 0.364591,\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}, {"evidence_id": "api507",
    "reference": "https://mediadive.dsmz.de/rest/medium/507", "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw",
    "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[2].recipe[8]",
    "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\":
    \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\":
    50,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.05,\n                        \"mmol_l\": 0.364591,\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}], "layer_decisions": [{"path":
    "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path":
    "ingredients[25].concentration", "decision": "correct", "rationale": "The supported
    stock concentration is flattened into the main ingredients. Restore the vitamin
    stock and 1 mL batch addition without inventing a receiving-litre denominator."},
    {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[25].concentration", "decision": "correct", "rationale":
    "Both primary recipes place this item in the vitamin stock, not directly in the
    main medium. Matching stock composition does not authenticate the complete medium
    or any separate KOMODO variant."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[25].concentration", "decision": "correct", "rationale":
    "The supported stock concentration is flattened into the main ingredients. Restore
    the vitamin stock and 1 mL batch addition without inventing a receiving-litre
    denominator."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml",
    "field_path": "ingredients[25].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[25].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml",
    "field_path": "ingredients[25].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[25].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml",
    "field_path": "ingredients[25].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path":
    "ingredients[25].concentration", "decision": "unsupported", "rationale": "The
    exact KOMODO variant endpoint returned 403. Its local copied signature and base-source
    link do not authenticate this amount. Preserve unresolved variant provenance pending
    exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[25].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id":
    "q27", "label": "(DL)-alpha-Lipoic acid", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml",
    "field_path": "ingredients[26].concentration", "stored": {"value": "0.05", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[26].concentration", "stored": {"value": "0.05", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[26].concentration", "stored": {"value": "0.05", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path":
    "ingredients[26].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[26].concentration",
    "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml",
    "field_path": "ingredients[26].concentration", "stored": {"value": "0.05", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path":
    "ingredients[26].concentration", "stored": {"value": "0.05", "unit": "G_PER_L"}},
    {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml", "field_path": "ingredients[26].concentration",
    "stored": {"value": "0.05", "unit": "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml",
    "field_path": "ingredients[26].concentration", "stored": {"value": "0.05", "unit":
    "G_PER_L"}}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[26].concentration", "stored": {"value": "0.05", "unit":
    "G_PER_L"}}], "decision": "mixed", "rationale": "Exact507a target/owner support,
    separate507 base conflict and unavailable KOMODO variants are distinguished in
    the layer decisions; no blanket transfer or approval of the ten encoded copies.",
    "source_stage": "Wolin vitamin stock", "sources": [{"evidence_id": "dsm507a",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79",
    "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d",
    "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 64-64",
    "quote": "(DL)-alpha-Lipoic acid                 50.00   mg", "quote_basis": "derivative
    text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[2].recipe[9]",
    "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\":
    \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\": 252,\n                        \"amount\":
    50,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.05,\n                        \"mmol_l\": 0.24233,\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}, {"evidence_id": "api507",
    "reference": "https://mediadive.dsmz.de/rest/medium/507", "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw",
    "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[2].recipe[9]",
    "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\":
    \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\": 252,\n                        \"amount\":
    50,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.05,\n                        \"mmol_l\": 0.24233,\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}], "layer_decisions": [{"path":
    "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml", "field_path":
    "ingredients[26].concentration", "decision": "correct", "rationale": "The supported
    stock concentration is flattened into the main ingredients. Restore the vitamin
    stock and 1 mL batch addition without inventing a receiving-litre denominator."},
    {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ingredients[26].concentration", "decision": "correct", "rationale":
    "Both primary recipes place this item in the vitamin stock, not directly in the
    main medium. Matching stock composition does not authenticate the complete medium
    or any separate KOMODO variant."}, {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ingredients[26].concentration", "decision": "correct", "rationale":
    "The supported stock concentration is flattened into the main ingredients. Restore
    the vitamin stock and 1 mL batch addition without inventing a receiving-litre
    denominator."}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml",
    "field_path": "ingredients[26].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ingredients[26].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml",
    "field_path": "ingredients[26].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ingredients[26].concentration",
    "decision": "unsupported", "rationale": "The exact KOMODO variant endpoint returned
    403. Its local copied signature and base-source link do not authenticate this
    amount. Preserve unresolved variant provenance pending exact evidence; do not
    copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml",
    "field_path": "ingredients[26].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}, {"path":
    "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml", "field_path":
    "ingredients[26].concentration", "decision": "unsupported", "rationale": "The
    exact KOMODO variant endpoint returned 403. Its local copied signature and base-source
    link do not authenticate this amount. Preserve unresolved variant provenance pending
    exact evidence; do not copy507 or507a automatically."}, {"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ingredients[26].concentration", "decision": "unsupported", "rationale":
    "The exact KOMODO variant endpoint returned 403. Its local copied signature and
    base-source link do not authenticate this amount. Preserve unresolved variant
    provenance pending exact evidence; do not copy507 or507a automatically."}]}, {"quantity_id":
    "q28", "label": "Existing pH: carboxydothermus_siderophilus_medium", "local_fields":
    [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml",
    "field_path": "ph_value", "stored": 6.9}], "decision": "evidence_only", "rationale":
    "The declared507a pH 6.9 lies within the printed 6.8–7.0 final range; preserve
    this supported value and source distinction.", "source_stage": "source-specific
    pH", "sources": [{"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.medium", "quote":
    "{\n            \"id\": \"507a\",\n            \"name\": \"CARBOXYDOTHERMUS SIDEROPHILUS
    MEDIUM\",\n            \"complex_medium\": \"yes\",\n            \"min_pH\": 6.9,\n            \"max_pH\":
    6.9,\n            \"source\": \"DSMZ\",\n            \"link\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf\"\n        }",
    "quote_basis": "raw UTF-8"}, {"evidence_id": "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79",
    "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d",
    "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 21-21",
    "quote": "After completing the medium adjust pH to 6.8 - 7.0.", "quote_basis":
    "derivative text"}]}, {"quantity_id": "q29", "label": "Existing pH: carboxydothermus_medium",
    "local_fields": [{"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ph_value", "stored": 6.9}], "decision": "evidence_only", "rationale":
    "The value agrees with the exact printed base range or named DSM override. This
    does not certify the complete KOMODO formulation or transfer that override to
    507a.", "source_stage": "source-specific pH", "sources": [{"evidence_id": "dsm507",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4",
    "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7",
    "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 23-23",
    "quote": "medium adjust pH to 6.8-7.0.", "quote_basis": "derivative text"}]},
    {"quantity_id": "q30", "label": "Existing pH range: carboxydothermus_medium",
    "local_fields": [{"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ph_range.min", "stored": 6.8}, {"path": "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml",
    "field_path": "ph_range.max", "stored": 7.0}], "decision": "evidence_only", "rationale":
    "The base507 source prints 6.8–7.0; its transfer to separately named variants
    remains unverified when exact variant evidence is unavailable.", "source_stage":
    "base range or unresolved variant assertion", "sources": [{"evidence_id": "dsm507",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4",
    "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7",
    "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 23-23",
    "quote": "medium adjust pH to 6.8-7.0.", "quote_basis": "derivative text"}]},
    {"quantity_id": "q31", "label": "Existing pH: carboxydothermus_siderophilus_medium",
    "local_fields": [{"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "ph_value", "stored": 6.9}], "decision": "evidence_only", "rationale":
    "The declared507a pH 6.9 lies within the printed 6.8–7.0 final range; preserve
    this supported value and source distinction.", "source_stage": "source-specific
    pH", "sources": [{"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.medium", "quote":
    "{\n            \"id\": \"507a\",\n            \"name\": \"CARBOXYDOTHERMUS SIDEROPHILUS
    MEDIUM\",\n            \"complex_medium\": \"yes\",\n            \"min_pH\": 6.9,\n            \"max_pH\":
    6.9,\n            \"source\": \"DSMZ\",\n            \"link\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf\"\n        }",
    "quote_basis": "raw UTF-8"}, {"evidence_id": "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79",
    "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d",
    "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 21-21",
    "quote": "After completing the medium adjust pH to 6.8 - 7.0.", "quote_basis":
    "derivative text"}]}, {"quantity_id": "q32", "label": "Existing pH: for_dsm_12326",
    "local_fields": [{"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml",
    "field_path": "ph_value", "stored": 6.9}], "decision": "unsupported", "rationale":
    "This local variant pH is not independently established by the available exact
    primary and the current KOMODO request failed. Preserve it as an unresolved assertion,
    not a validated growth optimum.", "source_stage": "source-specific pH", "sources":
    [{"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4",
    "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7",
    "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 23-23",
    "quote": "medium adjust pH to 6.8-7.0.", "quote_basis": "derivative text"}]},
    {"quantity_id": "q33", "label": "Existing pH range: for_dsm_12326", "local_fields":
    [{"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml", "field_path": "ph_range.min",
    "stored": 6.8}, {"path": "data/normalized_yaml/bacterial/for_dsm_12326.yaml",
    "field_path": "ph_range.max", "stored": 7.0}], "decision": "unsupported", "rationale":
    "The base507 source prints 6.8–7.0; its transfer to separately named variants
    remains unverified when exact variant evidence is unavailable.", "source_stage":
    "base range or unresolved variant assertion", "sources": [{"evidence_id": "dsm507",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4",
    "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7",
    "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 23-23",
    "quote": "medium adjust pH to 6.8-7.0.", "quote_basis": "derivative text"}]},
    {"quantity_id": "q34", "label": "Existing pH: for_dsm_18923", "local_fields":
    [{"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ph_value",
    "stored": 6.9}], "decision": "unsupported", "rationale": "This local variant pH
    is not independently established by the available exact primary and the current
    KOMODO request failed. Preserve it as an unresolved assertion, not a validated
    growth optimum.", "source_stage": "source-specific pH", "sources": [{"evidence_id":
    "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4",
    "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7",
    "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 23-23",
    "quote": "medium adjust pH to 6.8-7.0.", "quote_basis": "derivative text"}]},
    {"quantity_id": "q35", "label": "Existing pH range: for_dsm_18923", "local_fields":
    [{"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml", "field_path": "ph_range.min",
    "stored": 6.8}, {"path": "data/normalized_yaml/bacterial/for_dsm_18923.yaml",
    "field_path": "ph_range.max", "stored": 7.0}], "decision": "unsupported", "rationale":
    "The base507 source prints 6.8–7.0; its transfer to separately named variants
    remains unverified when exact variant evidence is unavailable.", "source_stage":
    "base range or unresolved variant assertion", "sources": [{"evidence_id": "dsm507",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4",
    "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7",
    "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 23-23",
    "quote": "medium adjust pH to 6.8-7.0.", "quote_basis": "derivative text"}]},
    {"quantity_id": "q36", "label": "Existing pH: for_dsm_21278", "local_fields":
    [{"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ph_value",
    "stored": 6.9}], "decision": "unsupported", "rationale": "This local variant pH
    is not independently established by the available exact primary and the current
    KOMODO request failed. Preserve it as an unresolved assertion, not a validated
    growth optimum.", "source_stage": "source-specific pH", "sources": [{"evidence_id":
    "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4",
    "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7",
    "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 23-23",
    "quote": "medium adjust pH to 6.8-7.0.", "quote_basis": "derivative text"}]},
    {"quantity_id": "q37", "label": "Existing pH range: for_dsm_21278", "local_fields":
    [{"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml", "field_path": "ph_range.min",
    "stored": 6.8}, {"path": "data/normalized_yaml/bacterial/for_dsm_21278.yaml",
    "field_path": "ph_range.max", "stored": 7.0}], "decision": "unsupported", "rationale":
    "The base507 source prints 6.8–7.0; its transfer to separately named variants
    remains unverified when exact variant evidence is unavailable.", "source_stage":
    "base range or unresolved variant assertion", "sources": [{"evidence_id": "dsm507",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4",
    "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7",
    "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 23-23",
    "quote": "medium adjust pH to 6.8-7.0.", "quote_basis": "derivative text"}]},
    {"quantity_id": "q38", "label": "Existing pH: for_dsm_21830", "local_fields":
    [{"path": "data/normalized_yaml/bacterial/for_dsm_21830.yaml", "field_path": "ph_value",
    "stored": 6.0}], "decision": "evidence_only", "rationale": "The value agrees with
    the exact printed base range or named DSM override. This does not certify the
    complete KOMODO formulation or transfer that override to 507a.", "source_stage":
    "source-specific pH", "sources": [{"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4",
    "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7",
    "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 32-32",
    "quote": "For DSM 21830: Adjust pH of complete medium to 6.0.", "quote_basis":
    "derivative text"}]}, {"quantity_id": "q39", "label": "Existing pH: for_dsm_23698",
    "local_fields": [{"path": "data/normalized_yaml/bacterial/for_dsm_23698.yaml",
    "field_path": "ph_value", "stored": 6.2}], "decision": "evidence_only", "rationale":
    "The value agrees with the exact printed base range or named DSM override. This
    does not certify the complete KOMODO formulation or transfer that override to
    507a.", "source_stage": "source-specific pH", "sources": [{"evidence_id": "dsm507",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4",
    "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7",
    "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 36-38",
    "quote": "For DSM 23698: Supplement medium with 2.00 g/l Na-pyruvate and omit
    sulfide. Adjust\nfinal pH of medium to 6.2. Change gas phase to 100% carbon monoxide
    prior to\ninoculation, but do not use excess pressure.", "quote_basis": "derivative
    text"}]}, {"quantity_id": "q40", "label": "Existing pH: medium_507_modified_for_dsm_7242",
    "local_fields": [{"path": "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml",
    "field_path": "ph_value", "stored": 7.0}], "decision": "unsupported", "rationale":
    "This local variant pH is not independently established by the available exact
    primary and the current KOMODO request failed. Preserve it as an unresolved assertion,
    not a validated growth optimum.", "source_stage": "source-specific pH", "sources":
    [{"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4",
    "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7",
    "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 23-23",
    "quote": "medium adjust pH to 6.8-7.0.", "quote_basis": "derivative text"}]},
    {"quantity_id": "q41", "label": "Existing pH: pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521",
    "local_fields": [{"path": "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml",
    "field_path": "ph_value", "stored": 7.0}], "decision": "unsupported", "rationale":
    "This local variant pH is not independently established by the available exact
    primary and the current KOMODO request failed. Preserve it as an unresolved assertion,
    not a validated growth optimum.", "source_stage": "source-specific pH", "sources":
    [{"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4",
    "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7",
    "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 23-23",
    "quote": "medium adjust pH to 6.8-7.0.", "quote_basis": "derivative text"}]},
    {"quantity_id": "q42", "label": "Retained507a preparation 1", "local_fields":
    [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml",
    "field_path": "preparation_steps[0].description", "stored": "Dissolve ingredients
    except bicarbonate, yeast extract, vitamins and sulfide, then sparge medium with
    100% N2 gas for 30 - 45 min to make it anoxic. Dispense medium under same gas
    atmosphere into anoxic Hungate-type tubes or serum vials to 30% of their volume
    and autoclave. Add yeast extract, vitamins (sterilized by filtration) and sulfide
    from sterile anoxic stock solutions prepared under 100% N2 gas atmosphere and
    bicarbonate from a sterile anoxic stock solution prepared under 80% N2 and 20%
    CO2 gas mixture. After completing the medium adjust pH to 6.8 - 7.0."}, {"path":
    "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path":
    "preparation_steps[0].description", "stored": "Dissolve ingredients except bicarbonate,
    yeast extract, vitamins and sulfide, then sparge medium with 100% N2 gas for 30
    - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic
    Hungate-type tubes or serum vials to 30% of their volume and autoclave. Add yeast
    extract, vitamins (sterilized by filtration) and sulfide from sterile anoxic stock
    solutions prepared under 100% N2 gas atmosphere and bicarbonate from a sterile
    anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture. After completing
    the medium adjust pH to 6.8 - 7.0."}], "decision": "evidence_only", "rationale":
    "Credit the complete retained literal source instructions. The third step belongs
    to SL-4 and must move with the stock. Sulfide is mentioned in preparation without
    a quantified507a table dose; retain that ambiguity and never borrow the 20 mL
    dose from 507. The 1 bar instruction is overpressure, not absolute pressure.",
    "source_stage": "507a main preparation", "sources": [{"evidence_id": "dsm507a",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79",
    "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d",
    "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 15-21",
    "quote": "1. Dissolve ingredients except bicarbonate, yeast extract, vitamins
    and sulfide, then\nsparge medium with 100% N2 gas for 30 - 45 min to make it anoxic.
    Dispense medium\nunder same gas atmosphere into anoxic Hungate-type tubes or serum
    vials to 30% of their\nvolume and autoclave. Add yeast extract, vitamins (sterilized
    by filtration) and sulfide from\nsterile anoxic stock solutions prepared under
    100% N2 gas atmosphere and bicarbonate\nfrom a sterile anoxic stock solution prepared
    under 80% N2 and 20% CO2 gas mixture.\nAfter completing the medium adjust pH to
    6.8 - 7.0.", "quote_basis": "derivative text"}]}, {"quantity_id": "q43", "label":
    "Retained507a preparation 2", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml",
    "field_path": "preparation_steps[1].description", "stored": "Inoculated vessels
    are pressurized with sterile carbon monoxide gas to 1 bar overpressure."}, {"path":
    "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml", "field_path":
    "preparation_steps[1].description", "stored": "Inoculated vessels are pressurized
    with sterile carbon monoxide gas to 1 bar overpressure."}], "decision": "evidence_only",
    "rationale": "Credit the complete retained literal source instructions. The third
    step belongs to SL-4 and must move with the stock. Sulfide is mentioned in preparation
    without a quantified507a table dose; retain that ambiguity and never borrow the
    20 mL dose from 507. The 1 bar instruction is overpressure, not absolute pressure.",
    "source_stage": "507a main preparation", "sources": [{"evidence_id": "dsm507a",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79",
    "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d",
    "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 22-23",
    "quote": "2. Inoculated vessels are pressurized with sterile carbon monoxide gas
    to 1 bar\noverpressure.", "quote_basis": "derivative text"}]}, {"quantity_id":
    "q44", "label": "Retained507a preparation 3", "local_fields": [{"path": "data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml",
    "field_path": "preparation_steps[2].description", "stored": "First dissolve EDTA
    in distilled water and adjust pH to 7.0 using 2 N NaOH; then add other compounds."},
    {"path": "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml",
    "field_path": "preparation_steps[2].description", "stored": "First dissolve EDTA
    in distilled water and adjust pH to 7.0 using 2 N NaOH; then add other compounds."}],
    "decision": "correct", "rationale": "Credit the complete retained literal source
    instructions. The third step belongs to SL-4 and must move with the stock. Sulfide
    is mentioned in preparation without a quantified507a table dose; retain that ambiguity
    and never borrow the 20 mL dose from 507. The 1 bar instruction is overpressure,
    not absolute pressure.", "source_stage": "SL-4 stock preparation", "sources":
    [{"evidence_id": "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79",
    "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d",
    "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 40-41",
    "quote": "First dissolve EDTA in distilled water and adjust pH to 7.0 using 2
    N NaOH; then add other\ncompounds.", "quote_basis": "derivative text"}]}, {"quantity_id":
    "q45", "label": "507a SL-4 addition", "local_fields": [], "decision": "evidence_only",
    "rationale": "The printed source batch volume is missing structurally. Restore
    its exact stage and unit without deriving a measured final volume or per-litre
    dose.", "source_stage": "507a receiving batch", "sources": [{"evidence_id": "dsm507a",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79",
    "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d",
    "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 9-9",
    "quote": "Trace element solution SL-4                          10.00           ml",
    "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[0].recipe[6]",
    "quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\":
    \"Trace element solution SL-4\",\n                        \"solution_id\": 20,\n                        \"amount\":
    10,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}]}, {"quantity_id": "q46",
    "label": "507a Vitamin addition", "local_fields": [], "decision": "evidence_only",
    "rationale": "The printed source batch volume is missing structurally. Restore
    its exact stage and unit without deriving a measured final volume or per-litre
    dose.", "source_stage": "507a receiving batch", "sources": [{"evidence_id": "dsm507a",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79",
    "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d",
    "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 12-12",
    "quote": "Wolin''s vitamin solution (10x)                        1.00           ml",
    "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[0].recipe[9]",
    "quote": "{\n                        \"recipe_order\": 10,\n                        \"solution\":
    \"Wolin''s vitamin solution (10x)\",\n                        \"solution_id\":
    5980,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_basis":
    "raw UTF-8"}]}, {"quantity_id": "q47", "label": "507a Main water input", "local_fields":
    [], "decision": "evidence_only", "rationale": "The printed source batch volume
    is missing structurally. Restore its exact stage and unit without deriving a measured
    final volume or per-litre dose.", "source_stage": "507a receiving batch", "sources":
    [{"evidence_id": "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79",
    "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d",
    "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 13-13",
    "quote": "Distilled water                                    1000.00           ml",
    "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[0].recipe[10]",
    "quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    1000,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}]}, {"quantity_id": "q48",
    "label": "507a stock water 1", "local_fields": [], "decision": "evidence_only",
    "rationale": "The source states 1000 mL water input for this stock; its provider-declared
    rate is distinct from a measured final volume. SL-4 has a pH adjustment but no
    explicit final-makeup sentence.", "source_stage": "507a stock solvent", "sources":
    [{"evidence_id": "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79",
    "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d",
    "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 38-38",
    "quote": "Distilled water                                       1000.00        ml",
    "quote_basis": "derivative text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[1].recipe[9]",
    "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    1000,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}]}, {"quantity_id": "q49",
    "label": "507a stock water 2", "local_fields": [], "decision": "evidence_only",
    "rationale": "The source states 1000 mL water input for this stock; its provider-declared
    rate is distinct from a measured final volume. SL-4 has a pH adjustment but no
    explicit final-makeup sentence.", "source_stage": "507a stock solvent", "sources":
    [{"evidence_id": "dsm507a", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507a.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507a.raw", "raw_sha256": "c670a3e4b7621fce7090bc9b370f9fed3af90656dcd803748d076490d6186e79",
    "text_sha256": "4e22ab1363788ae7d59f9ef43a03eca4422f8fdd33482e71d1bcf51afd701e8d",
    "accessed_at": "2026-10-28T06:51:39.622388Z", "locator": "dsm507a.txt lines 65-65",
    "quote": "Distilled water                      1000.00   ml", "quote_basis": "derivative
    text"}, {"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "data.solutions[2].recipe[10]",
    "quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    1000,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}]}, {"quantity_id": "q50",
    "label": "507 comparator SL-11 addition", "local_fields": [], "decision": "evidence_only",
    "rationale": "This belongs only to the separately identified 507 base source and
    is retained for identity/representation reconciliation. It is not a missing507a
    quantity and does not establish a complete unavailable KOMODO variant.", "source_stage":
    "507-only source comparison", "sources": [{"evidence_id": "dsm507", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf", "raw_path":
    "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4",
    "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7",
    "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 8-8",
    "quote": "Trace element solution SL-11                             1.00        ml",
    "quote_basis": "derivative text"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[0].recipe[5]",
    "quote": "{\n                        \"recipe_order\": 6,\n                        \"solution\":
    \"Trace element solution SL-11\",\n                        \"solution_id\": 1474,\n                        \"amount\":
    1,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}]}, {"quantity_id": "q51",
    "label": "507 comparator Resazurin stock addition", "local_fields": [], "decision":
    "evidence_only", "rationale": "This belongs only to the separately identified
    507 base source and is retained for identity/representation reconciliation. It
    is not a missing507a quantity and does not establish a complete unavailable KOMODO
    variant.", "source_stage": "507-only source comparison", "sources": [{"evidence_id":
    "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4",
    "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7",
    "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 9-9",
    "quote": "Sodium resazurin (0.1% w/v)                              0.50        ml",
    "quote_basis": "derivative text"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[0].recipe[6]",
    "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\":
    \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\":
    \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\":
    \"ml\",\n                        \"g_l\": 0.000489237,\n                        \"mmol_l\":
    0.00194783,\n                        \"optional\": 0\n                    }",
    "quote_basis": "raw UTF-8"}]}, {"quantity_id": "q52", "label": "507 comparator
    Vitamin addition", "local_fields": [], "decision": "evidence_only", "rationale":
    "This belongs only to the separately identified 507 base source and is retained
    for identity/representation reconciliation. It is not a missing507a quantity and
    does not establish a complete unavailable KOMODO variant.", "source_stage": "507-only
    source comparison", "sources": [{"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4",
    "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7",
    "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 12-12",
    "quote": "Wolin''s vitamin solution (10x)                           1.00        ml",
    "quote_basis": "derivative text"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[0].recipe[9]",
    "quote": "{\n                        \"recipe_order\": 10,\n                        \"solution\":
    \"Wolin''s vitamin solution (10x)\",\n                        \"solution_id\":
    5980,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_basis":
    "raw UTF-8"}]}, {"quantity_id": "q53", "label": "507 comparator Sulfide addition",
    "local_fields": [], "decision": "evidence_only", "rationale": "This belongs only
    to the separately identified 507 base source and is retained for identity/representation
    reconciliation. It is not a missing507a quantity and does not establish a complete
    unavailable KOMODO variant.", "source_stage": "507-only source comparison", "sources":
    [{"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4",
    "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7",
    "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 13-13",
    "quote": "Neutralized sulfide solution 3% (w/v)                   20.00        ml",
    "quote_basis": "derivative text"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[0].recipe[10]",
    "quote": "{\n                        \"recipe_order\": 11,\n                        \"solution\":
    \"Neutralized sulfide solution 3% (w/v)\",\n                        \"solution_id\":
    34,\n                        \"amount\": 20,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_basis":
    "raw UTF-8"}]}, {"quantity_id": "q54", "label": "507 comparator Main water", "local_fields":
    [], "decision": "evidence_only", "rationale": "This belongs only to the separately
    identified 507 base source and is retained for identity/representation reconciliation.
    It is not a missing507a quantity and does not establish a complete unavailable
    KOMODO variant.", "source_stage": "507-only source comparison", "sources": [{"evidence_id":
    "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4",
    "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7",
    "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 14-14",
    "quote": "Distilled water                                       1000.00        ml",
    "quote_basis": "derivative text"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[0].recipe[11]",
    "quote": "{\n                        \"recipe_order\": 13,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    1000,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}]}, {"quantity_id": "q55",
    "label": "507 comparator SL-11 water", "local_fields": [], "decision": "evidence_only",
    "rationale": "Retain this exact stock amount and source stage only. The sulfide
    3% w/v strength is explicit; its preparation-water input is not measured receiving
    volume. No transfer into 507a is justified.", "source_stage": "507-only stock
    comparison", "sources": [{"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4",
    "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7",
    "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 61-61",
    "quote": "Distilled water                                       1000.00      ml",
    "quote_basis": "derivative text"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[1].recipe[9]",
    "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    1000,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}]}, {"quantity_id": "q56",
    "label": "507 comparator Vitamin water", "local_fields": [], "decision": "evidence_only",
    "rationale": "Retain this exact stock amount and source stage only. The sulfide
    3% w/v strength is explicit; its preparation-water input is not measured receiving
    volume. No transfer into 507a is justified.", "source_stage": "507-only stock
    comparison", "sources": [{"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4",
    "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7",
    "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 80-80",
    "quote": "Distilled water                                       1000.00      ml",
    "quote_basis": "derivative text"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[2].recipe[10]",
    "quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    1000,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}]}, {"quantity_id": "q57",
    "label": "507 comparator Sulfide solute", "local_fields": [], "decision": "evidence_only",
    "rationale": "Retain this exact stock amount and source stage only. The sulfide
    3% w/v strength is explicit; its preparation-water input is not measured receiving
    volume. No transfer into 507a is justified.", "source_stage": "507-only stock
    comparison", "sources": [{"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4",
    "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7",
    "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 85-85",
    "quote": "Na2S x 9 H2O                                             3.00        g",
    "quote_basis": "derivative text"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[3].recipe[0]",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\":
    3,\n                        \"unit\": \"g\",\n                        \"g_l\":
    30,\n                        \"mmol_l\": 124.905,\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}]}, {"quantity_id": "q58",
    "label": "507 comparator Sulfide water", "local_fields": [], "decision": "evidence_only",
    "rationale": "Retain this exact stock amount and source stage only. The sulfide
    3% w/v strength is explicit; its preparation-water input is not measured receiving
    volume. No transfer into 507a is justified.", "source_stage": "507-only stock
    comparison", "sources": [{"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4",
    "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7",
    "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 86-86",
    "quote": "Distilled water                                        100.00       ml",
    "quote_basis": "derivative text"}, {"evidence_id": "api507", "reference": "https://mediadive.dsmz.de/rest/medium/507",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw", "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "data.solutions[3].recipe[1]",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    100,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "quote_basis": "raw UTF-8"}]}, {"quantity_id": "q59",
    "label": "507 main preparation", "local_fields": [], "decision": "evidence_only",
    "rationale": "This source-only process or named override remains tied to 507.
    Preserve explicit strengths, amounts, gas composition, vessel fraction, time,
    temperature and overpressure separately; unquantified titrant doses remain unknown.
    An identity lead is not a verified complete formulation for the unavailable KOMODO
    variants.", "source_stage": "507-specific preparation/variant", "sources": [{"evidence_id":
    "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4",
    "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7",
    "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 16-25",
    "quote": "1. Dissolve ingredients except bicarbonate, yeast extract, vitamins
    and sulfide, then\nsparge medium with 100% N2 gas for 30 - 45 min to make it anoxic.
    Dispense medium\nunder same gas atmosphere into anoxic Hungate-type tubes or serum
    vials to 30% of their\nvolume and autoclave. Add yeast extract, vitamins (sterilized
    by filtration) and sulfide from\nsterile anoxic stock solutions prepared under
    100% N2 gas atmosphere and bicarbonate\nfrom a sterile anoxic stock solution prepared
    under 80% N2 and 20% CO2 gas mixture.\nNeutralize the sodium sulfide with sterile
    H2SO4 (see medium 29). After completing the\nmedium adjust pH to 6.8-7.0.\n2.
    Inoculated vessels are pressurized with sterile carbon monoxide gas to 2 bar\noverpressure.",
    "quote_basis": "derivative text"}]}, {"quantity_id": "q60", "label": "507 SL-11
    makeup", "local_fields": [], "decision": "evidence_only", "rationale": "This source-only
    process or named override remains tied to 507. Preserve explicit strengths, amounts,
    gas composition, vessel fraction, time, temperature and overpressure separately;
    unquantified titrant doses remain unknown. An identity lead is not a verified
    complete formulation for the unavailable KOMODO variants.", "source_stage": "507-specific
    preparation/variant", "sources": [{"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4",
    "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7",
    "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 63-65",
    "quote": "Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH
    and add ferrous\nchloride. After ferrous chloride has dissolved add other compounds.
    Finally adjust pH to 6.0\nand bring volume to 1000 ml.", "quote_basis": "derivative
    text"}]}, {"quantity_id": "q61", "label": "507 sulfide preparation", "local_fields":
    [], "decision": "evidence_only", "rationale": "This source-only process or named
    override remains tied to 507. Preserve explicit strengths, amounts, gas composition,
    vessel fraction, time, temperature and overpressure separately; unquantified titrant
    doses remain unknown. An identity lead is not a verified complete formulation
    for the unavailable KOMODO variants.", "source_stage": "507-specific preparation/variant",
    "sources": [{"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4",
    "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7",
    "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 88-92",
    "quote": "The sulfide solution is prepared in a 250 ml screw-capped bottle with
    a butyl rubber\nseptum and a magnetic stirrer. The solution is bubbled with nitrogen
    gas, closed and\nautoclaved for 15 min. at 121°C. After cooling to room temperature
    the pH is adjusted to\nabout 7.0 by adding of sterile 2 M H2SO4 drop-wise with
    a syringe without opening the\nbottle.", "quote_basis": "derivative text"}]},
    {"quantity_id": "q62", "label": "DSM12326 supplement", "local_fields": [], "decision":
    "evidence_only", "rationale": "This source-only process or named override remains
    tied to 507. Preserve explicit strengths, amounts, gas composition, vessel fraction,
    time, temperature and overpressure separately; unquantified titrant doses remain
    unknown. An identity lead is not a verified complete formulation for the unavailable
    KOMODO variants.", "source_stage": "507-specific preparation/variant", "sources":
    [{"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4",
    "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7",
    "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 28-29",
    "quote": "For DSM 12326: Supplement medium with 1.00 ml/l selenite-tungstate solution
    (see\nmedium 385).", "quote_basis": "derivative text"}]}, {"quantity_id": "q63",
    "label": "DSM19011 override", "local_fields": [], "decision": "evidence_only",
    "rationale": "This source-only process or named override remains tied to 507.
    Preserve explicit strengths, amounts, gas composition, vessel fraction, time,
    temperature and overpressure separately; unquantified titrant doses remain unknown.
    An identity lead is not a verified complete formulation for the unavailable KOMODO
    variants.", "source_stage": "507-specific preparation/variant", "sources": [{"evidence_id":
    "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4",
    "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7",
    "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 30-31",
    "quote": "For DSM 19011: Supplement medium with 0.20 g/l Na-lactate. Change gas
    phase to 100%\ncarbon monoxide prior to inoculation, but do not use excess pressure.",
    "quote_basis": "derivative text"}]}, {"quantity_id": "q64", "label": "DSM21830
    pH override", "local_fields": [], "decision": "evidence_only", "rationale": "This
    source-only process or named override remains tied to 507. Preserve explicit strengths,
    amounts, gas composition, vessel fraction, time, temperature and overpressure
    separately; unquantified titrant doses remain unknown. An identity lead is not
    a verified complete formulation for the unavailable KOMODO variants.", "source_stage":
    "507-specific preparation/variant", "sources": [{"evidence_id": "dsm507", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf", "raw_path":
    "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4",
    "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7",
    "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 32-32",
    "quote": "For DSM 21830: Adjust pH of complete medium to 6.0.", "quote_basis":
    "derivative text"}]}, {"quantity_id": "q65", "label": "DSM22663 override", "local_fields":
    [], "decision": "evidence_only", "rationale": "This source-only process or named
    override remains tied to 507. Preserve explicit strengths, amounts, gas composition,
    vessel fraction, time, temperature and overpressure separately; unquantified titrant
    doses remain unknown. An identity lead is not a verified complete formulation
    for the unavailable KOMODO variants.", "source_stage": "507-specific preparation/variant",
    "sources": [{"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4",
    "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7",
    "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 33-35",
    "quote": "For DSM 22663: Supplement medium with 10.00 g/l sulfur and increase
    amount of yeast\nextract to 1.00 g/l. Sulfur is sterilized separately by steaming
    for 3 h on each of three\nsuccessive days.", "quote_basis": "derivative text"}]},
    {"quantity_id": "q66", "label": "DSM23698 override", "local_fields": [], "decision":
    "evidence_only", "rationale": "This source-only process or named override remains
    tied to 507. Preserve explicit strengths, amounts, gas composition, vessel fraction,
    time, temperature and overpressure separately; unquantified titrant doses remain
    unknown. An identity lead is not a verified complete formulation for the unavailable
    KOMODO variants.", "source_stage": "507-specific preparation/variant", "sources":
    [{"evidence_id": "dsm507", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf",
    "raw_path": "REVIEW_WORK/batch059/source07-09/dsm507.raw", "raw_sha256": "47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4",
    "text_sha256": "57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7",
    "accessed_at": "2026-10-28T06:51:39.624958Z", "locator": "dsm507.txt lines 36-38",
    "quote": "For DSM 23698: Supplement medium with 2.00 g/l Na-pyruvate and omit
    sulfide. Adjust\nfinal pH of medium to 6.2. Change gas phase to 100% carbon monoxide
    prior to\ninoculation, but do not use excess pressure.", "quote_basis": "derivative
    text"}]}, {"quantity_id": "q67", "label": "Provider volumes", "local_fields":
    [], "decision": "evidence_only", "rationale": "The providers declare 1011 mL for507a
    and 1022 mL for507. These explain their rate normalizations; they are not measured
    final volumes and cannot justify exchanging formulations.", "source_stage": "provider
    normalization", "sources": [{"evidence_id": "api507a", "reference": "https://mediadive.dsmz.de/rest/medium/507a",
    "raw_path": "REVIEW_WORK/batch059/source07-09/api507a.raw", "raw_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "text_sha256": "a2620715f2c6b3587cc43ff41237dfdfa84cdb273b069735844a20ea1e0255c7",
    "accessed_at": "2026-10-28T06:51:39.281663Z", "locator": "$.data.solutions[0].volume",
    "quote": "\"volume\": 1011", "quote_basis": "raw UTF-8"}, {"evidence_id": "api507",
    "reference": "https://mediadive.dsmz.de/rest/medium/507", "raw_path": "REVIEW_WORK/batch059/source07-09/api507.raw",
    "raw_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "text_sha256": "14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48",
    "accessed_at": "2026-10-28T06:51:39.443123Z", "locator": "$.data.solutions[0].volume",
    "quote": "\"volume\": 1022", "quote_basis": "raw UTF-8"}]}], "document_scopes":
    {"data/merge_yaml/merged/CARBOXYDOTHERMUS_SIDEROPHILUS_MEDIUM.yaml": null, "data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml":
    null, "data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml":
    null, "data/normalized_yaml/bacterial/for_dsm_12326.yaml": null, "data/normalized_yaml/bacterial/for_dsm_18923.yaml":
    null, "data/normalized_yaml/bacterial/for_dsm_21278.yaml": null, "data/normalized_yaml/bacterial/for_dsm_21830.yaml":
    null, "data/normalized_yaml/bacterial/for_dsm_23698.yaml": null, "data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml":
    null, "data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml":
    null}, "scope": "Every selected target/owner concentration plus explicit dependency
    fields; source-only rows/conditions and unchanged claims distinguished. Excluded
    parent quantities are not transferred."}'
- assessment_id: grounding
  area: grounding
  topic: Supplied forms and current ontology/MIM scope
  outcome: concern
  summary: Every actual asserted CHEBI primary and secondary slot is joined to a fresh
    exact non-obsolete OLS object and current packaged MIM rows. Nickel has a confirmed
    hydrate mismatch. Source Na2-EDTA in SL-4 has no hydrate qualifier, so anhydrous
    specificity remains unproven. Generic biotin does not by itself establish stereochemistry;
    DL lipoic acid is compatible with the non-stereospecific object. Calcium D-pantothenate
    agrees with the D-configured 31345 object but lacks the secondary slot. The absent
    anthraquinone slot is not counted as a validated ontology object, and historical
    candidate 85112 is not newly certified.
  target_ids:
  - CultureMech:001640
  evidence_ids:
  - groundings
  - mim
  - mim-meta
- assessment_id: history
  area: provenance
  topic: Existing repair credit and writer limits
  outcome: concern
  summary: All twenty exact historical reports and all current target/owner histories
    were read using lossless duplicate-cell pooling. Of347 literal historical source
    objects, 339 equal current responses; eight old 507 sulfide rows omit the now-present
    g_l/mmol_l fields. Current 507a raw bytes exactly match the old declared digest,
    while the current 507 raw digest differs; equal decoded objects do not authenticate
    the original507 raw event. No current owner has attached concentration evidence.
    The September report correctly raised source distinctions but incorrectly treats1011
    as measured final volume and states507a has no sulfide despite its preparation
    mention; those claims and automatic dilution/variant repair suggestions are not
    adopted. Current repair code is inspected as current implementation, not independent
    historical execution proof.
  target_ids:
  - CultureMech:001640
  evidence_ids:
  - history
  - old-reports
  - old-claims
  - writer-formulation
  - writer-merger
findings:
- finding_id: f1
  issue_key: culturemech-001640-source-duplicate
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Distinct 507 and 507a sources are asserted as duplicates
  description: The generated target combines nine owners and publishes reciprocal
    SOURCE_DUPLICATE assertions. Fresh primary sources distinguish507a anthraquinone/SL-4
    from 507 SL-11/resazurin/sulfide, different yeast input and different CO overpressure.
    The local 27-row signature cannot establish source equivalence. Separate these
    source identities and recover each exact variant before regenerating; retain current
    conservative merger safeguards, which already compare scientific fields and reject
    incompatible formulations.
  target_ids:
  - CultureMech:001640
  field_paths:
  - parent_media
  - variant_relationship
  - variant_modifications
  - merged_from
  - synonyms
  - data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml::variant_children[0]
  evidence_ids:
  - dsm507a
  - api507a
  - dsm507
  - api507
  - writer-formulation
  - writer-merger
  - writer-507
  rule_id: review-yaml-record/identity
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_12326.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_18923.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_21278.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_21830.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_23698.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml
    role: maintained source
- finding_id: f2
  issue_key: culturemech-001640-stock-topology
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Nineteen stock ingredients remain flattened into the main recipe
  description: For the exact 507a target/owner, nine SL-4 and ten vitamin components
    are encoded at stock strengths in main ingredients. Restore the two stock identities
    and printed batch additions, their separate water inputs and literal amount evidence.
    Preserve the supported main API rates on their declared basis. The copied KOMODO
    amounts require their own source reconciliation and are not repaired by applying507a
    to every owner.
  target_ids:
  - CultureMech:001640
  field_paths:
  - ingredients
  - solutions
  - preparation_steps[2]
  evidence_ids:
  - dsm507a
  - api507a
  - dsm507
  - api507
  - writer-mediadive
  rule_id: review-ingredient-concentrations/evidence-contract
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_12326.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_18923.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_21278.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_21830.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_23698.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml
    role: maintained source
- finding_id: f3
  issue_key: culturemech-001640-variant-controls
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Variant-specific quantities and atmosphere metadata are not represented reliably
  description: The exact base507 source specifies a DSM12326 supplement and distinct
    DSM21830/23698 overrides, while the corresponding local wrappers retain the copied507a
    matrix. Other variant formulations remain unavailable behind 403 responses. Aerobic:Yes
    notes conflict with the linked base source anoxic preparation and require source-specific
    correction; do not infer new organism-growth claims. Credit existing pH values
    that match named source overrides without endorsing entire variants. Preserve507a
    preparation and its unquantified sulfide ambiguity.
  target_ids:
  - CultureMech:001640
  field_paths:
  - notes
  - preparation_steps
  - ph_value
  - variant_modifications
  evidence_ids:
  - dsm507
  - dsm507a
  - api507
  - api507a
  - komodo507
  - komodo507.1
  - komodo507.2
  - komodo507.3
  - komodo507.4
  - komodo507.5
  - komodo507.7
  - komodo507_7242
  rule_id: review-yaml-record/representation
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_12326.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_18923.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_21278.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_21830.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_23698.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml
    role: maintained source
- finding_id: f4
  issue_key: culturemech-001640-nickel-form
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: The supplied nickel hexahydrate has an anhydrous ontology identity
  description: All ten copies assert CHEBI:34887 in primary and secondary nickel slots
    despite supplied NiCl2·6H2O. The fresh 53542 object identifies nickel dichloride
    hexahydrate. Correct actual supplied-form assertions while keeping unresolved
    variant formulation identity separate. Canonical label agreement and current MIM
    membership do not certify hydration.
  target_ids:
  - CultureMech:001640
  field_paths:
  - ingredients[15].term
  - ingredients[15].mediaingredientmech_chebi_term
  evidence_ids:
  - chebi34887
  - chebi53542
  - dsm507a
  - dsm507
  rule_id: review-yaml-record/grounding
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_12326.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_18923.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_21278.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_21830.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_23698.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml
    role: maintained source
- finding_id: f5
  issue_key: culturemech-001640-repair-writer
  category: provenance
  severity: major
  status: open
  certainty: confirmed
  title: The topology repair writer preserves the unsupported duplicate assumption
  description: Current repair_komodo_507_carboxydothermus_score10.py hardcodes the
    shared 27-row signature and SOURCE_DUPLICATE graph. Its matching-event replacement
    uses a fixed historical timestamp. Correct the maintained evidence and writer
    assumptions with a genuinely new append-only event; do not blindly rerun it or
    rewrite old history as though this new review occurred then. An ingredients_curated
    flag is not source authentication.
  target_ids:
  - CultureMech:001640
  field_paths:
  - curation_history
  - parent_media
  - variant_relationship
  - data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml::data_quality_flags
  evidence_ids:
  - writer-507
  - history
  - old-reports
  rule_id: review-yaml-record/provenance
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_12326.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_18923.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_21278.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_21830.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_23698.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml
    role: maintained source
- finding_id: f6
  issue_key: culturemech-001640-missing-grounding
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Two existing descriptors need bounded grounding follow-up
  description: Anthraquinone disulfonate has no primary or secondary ontology slot,
    and calcium D-pantothenate lacks its secondary linkage. The exact source compound
    identity is present, but the old report candidate 85112 is not freshly authenticated
    in this review; resolve the exact disodium form before adopting it. Existing 31345
    agrees with the source D-configured pantothenate and current index.
  target_ids:
  - CultureMech:001640
  field_paths:
  - ingredients[5]
  - ingredients[23]
  evidence_ids:
  - dsm507a
  - api507a
  - chebi31345
  - mim
  rule_id: review-yaml-record/grounding
  native_severity: P3
  normalization_reason: Bounded metadata, provenance or unresolved grounding follow-up;
    no critical scientific failure is inferred.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_12326.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_18923.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_21278.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_21830.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_23698.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml
    role: maintained source
actions:
- action_id: a1
  description: The generated target combines nine owners and publishes reciprocal
    SOURCE_DUPLICATE assertions. Fresh primary sources distinguish507a anthraquinone/SL-4
    from 507 SL-11/resazurin/sulfide, different yeast input and different CO overpressure.
    The local 27-row signature cannot establish source equivalence. Separate these
    source identities and recover each exact variant before regenerating; retain current
    conservative merger safeguards, which already compare scientific fields and reject
    incompatible formulations.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:001640
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_12326.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_18923.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_21278.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_21830.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_23698.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml
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
  description: For the exact 507a target/owner, nine SL-4 and ten vitamin components
    are encoded at stock strengths in main ingredients. Restore the two stock identities
    and printed batch additions, their separate water inputs and literal amount evidence.
    Preserve the supported main API rates on their declared basis. The copied KOMODO
    amounts require their own source reconciliation and are not repaired by applying507a
    to every owner.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:001640
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_12326.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_18923.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_21278.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_21830.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_23698.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml
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
  description: The exact base507 source specifies a DSM12326 supplement and distinct
    DSM21830/23698 overrides, while the corresponding local wrappers retain the copied507a
    matrix. Other variant formulations remain unavailable behind 403 responses. Aerobic:Yes
    notes conflict with the linked base source anoxic preparation and require source-specific
    correction; do not infer new organism-growth claims. Credit existing pH values
    that match named source overrides without endorsing entire variants. Preserve507a
    preparation and its unquantified sulfide ambiguity.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:001640
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_12326.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_18923.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_21278.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_21830.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_23698.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml
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
  description: All ten copies assert CHEBI:34887 in primary and secondary nickel slots
    despite supplied NiCl2·6H2O. The fresh 53542 object identifies nickel dichloride
    hexahydrate. Correct actual supplied-form assertions while keeping unresolved
    variant formulation identity separate. Canonical label agreement and current MIM
    membership do not certify hydration.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:001640
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_12326.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_18923.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_21278.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_21830.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_23698.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml
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
  description: Current repair_komodo_507_carboxydothermus_score10.py hardcodes the
    shared 27-row signature and SOURCE_DUPLICATE graph. Its matching-event replacement
    uses a fixed historical timestamp. Correct the maintained evidence and writer
    assumptions with a genuinely new append-only event; do not blindly rerun it or
    rewrite old history as though this new review occurred then. An ingredients_curated
    flag is not source authentication.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:001640
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_12326.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_18923.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_21278.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_21830.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_23698.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml
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
  description: Anthraquinone disulfonate has no primary or secondary ontology slot,
    and calcium D-pantothenate lacks its secondary linkage. The exact source compound
    identity is present, but the old report candidate 85112 is not freshly authenticated
    in this review; resolve the exact disodium form before adopting it. Existing 31345
    agrees with the source D-configured pantothenate and current index.
  finding_ids:
  - f6
  target_ids:
  - CultureMech:001640
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_507_CARBOXYDOTHERMUS_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/carboxydothermus_siderophilus_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_12326.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_18923.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_21278.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_21830.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_23698.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_507_modified_for_dsm_7242.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/pyruvate_as_an_alternative_substrate_for_dsm_6008_dsm_14886_and_dsm_16521.yaml
    role: maintained source
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
limitations:
- Current canonical checks validate encoded structure/labels; zero reference checks
  do not verify external source claims.
- All primary PDF pages were read visually as well as in their complete extracted
  text. Current source status, retrieval times and complete raw/text bytes remain
  in the capture catalog.
- Completion is partial because the eight exact historical KOMODO MediaInfo hyperlinks
  and exact MediaList route returned HTTP 403. Earlier getRecipe failures were guessed
  discovery leads and are retained separately. Full current-field coverage does not
  mean all variants are scientifically verified.
- The parent graph includes a separate DSM23132 child outside the selected nine owners.
  Its relationship assertion is read in the parent, but that separate YAML and its
  quantities are not assessed or modified.
- The older report mentions standalone main/SL-4/Wolin records outside this selected
  input scope. No new current defect is asserted for those uninspected standalone
  records.
- 507a preparation mentions sulfide but supplies no stock dose in its table or API.
  This remains unresolved; the 20 mL addition and 3% stock from 507 are not transferred.
- Historical imported timestamps with malformed .fZ or absent time zones are retained
  provenance, not used as new review access times. Native diagnostics passing do not
  certify every old timestamp or historical scientific assertion.
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
