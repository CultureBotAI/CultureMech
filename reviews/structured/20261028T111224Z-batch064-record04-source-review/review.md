# Clostridium viride medium: trace-stock scope and supplied chemical forms

- Review: 20261028T111224Z-batch064-record04-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T10:58:20.672451Z
- Finished UTC: 2026-10-28T11:12:24.282264Z
- Reviewer: Codex independent source reviewer (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The selected DSM526 record and its sole owner agree with the current primary identity and retain both preparation descriptions. Eleven trace-stock components are nevertheless flattened into the main ingredient list, and the 4 mL stock addition is absent. Explicit API main g_l values are credited without assuming a measured final volume. Sodium resazurin and nickel chloride hydrate identifiers need source-form reconciliation; evidence placement and stock-stage annotation remain incomplete.

## Scope And Provenance

Full selected record and exact maintained contributors; explicitly scoped dependency and external-source limits retained.

Selection: Actual batch064 native selection index 04.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:001657 | data/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.yaml | generated | clostridium_viride_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:001657 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-strict | passed | True | CultureMech:001657 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-terms | passed | True | CultureMech:001657 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-references | passed | True | CultureMech:001657 | Native reference checker performed zero reference checks; this is not claim authentication. |

## Scientific And Domain Assessments

### Exact DSM526 selected identity

identity: supported. Targets: CultureMech:001657.

The selected target and sole maintained owner identify DSM526/Clostridium viride and agree with the current primary/API. A historical report on a separate KOMODO aminovalericum record is comparison context only; its identity conflict, absent preparation, aerobic flag and extra carbonate are not findings on this record.

### Existing preparation is retained

completeness: concern. Targets: CultureMech:001657.

Both source preparation descriptions and the final pH range already exist and are supported. The important loss is stock structure and claim linkage, not wholesale missing preparation. Variable titrant doses and unspecified concentrated-acid strength remain unknown.

### Quantity scope and inventory

quantity: concern. Targets: CultureMech:001657.

Every selected target/owner concentration field has an explicit disposition; scoped dependency fields and source-only preparation are separate from receiving-medium rates.

[{"quantity_id": "q1", "topic": "5-Aminovaleric acid", "source": [{"evidence_id": "api526", "reference": "https://mediadive.dsmz.de/rest/medium/526", "raw_path": "REVIEW_WORK/batch064/source02-04/api526.bin", "raw_sha256": "01836967bf3384dfae78e42a3e14a300c515ed714676eb7eef7e856596a1ac89", "locator": "$.data.solutions[0].recipe[0]", "accessed_at": "2026-10-28T10:58:25.078229Z", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"5-Aminovaleric acid\",\n                        \"compound_id\": 538,\n                        \"amount\": 15,\n                        \"unit\": \"g\",\n                        \"g_l\": 15,\n                        \"mmol_l\": 128.041,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound": "5-Aminovaleric acid", "compound_id": 538, "amount": 15, "unit": "g", "g_l": 15, "mmol_l": 128.041, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm526", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium526.pdf", "raw_path": "REVIEW_WORK/batch064/source02-04/dsm526.bin", "raw_sha256": "970d6cccca0169339385018b2f55acaf2d3167714d213119d6b9f7d654090310", "locator": "PDF extracted line 3; visually checked page", "accessed_at": "2026-10-28T10:58:25.212182Z", "quote": "   5-Aminovaleric acid                                        15.00         g"}], "decision": "evidence_only", "rationale": "The explicit current API main g_l equals this stored numerical rate and is credited as a provider assertion. The primary gives the source batch amount and 1000 mL input water, not a measured final makeup. API separately reports volume 1004 mL and does not consistently derive its g_l by dividing these masses by that volume; no convenient denominator is selected or new rate calculated.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "15", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit current API main g_l equals this stored numerical rate and is credited as a provider assertion. The primary gives the source batch amount and 1000 mL input water, not a measured final makeup. API separately reports volume 1004 mL and does not consistently derive its g_l by dividing these masses by that volume; no convenient denominator is selected or new rate calculated."}, {"path": "data/normalized_yaml/bacterial/clostridium_viride_medium.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "15", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit current API main g_l equals this stored numerical rate and is credited as a provider assertion. The primary gives the source batch amount and 1000 mL input water, not a measured final makeup. API separately reports volume 1004 mL and does not consistently derive its g_l by dividing these masses by that volume; no convenient denominator is selected or new rate calculated."}]}, {"quantity_id": "q2", "topic": "K2HPO4", "source": [{"evidence_id": "api526", "reference": "https://mediadive.dsmz.de/rest/medium/526", "raw_path": "REVIEW_WORK/batch064/source02-04/api526.bin", "raw_sha256": "01836967bf3384dfae78e42a3e14a300c515ed714676eb7eef7e856596a1ac89", "locator": "$.data.solutions[0].recipe[1]", "accessed_at": "2026-10-28T10:58:25.078229Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 8.7,\n                        \"unit\": \"g\",\n                        \"g_l\": 8.7,\n                        \"mmol_l\": 49.9495,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound": "K2HPO4", "compound_id": 10, "amount": 8.7, "unit": "g", "g_l": 8.7, "mmol_l": 49.9495, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm526", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium526.pdf", "raw_path": "REVIEW_WORK/batch064/source02-04/dsm526.bin", "raw_sha256": "970d6cccca0169339385018b2f55acaf2d3167714d213119d6b9f7d654090310", "locator": "PDF extracted line 4; visually checked page", "accessed_at": "2026-10-28T10:58:25.212182Z", "quote": "   K2HPO4                                                      8.70         g"}], "decision": "evidence_only", "rationale": "The explicit current API main g_l equals this stored numerical rate and is credited as a provider assertion. The primary gives the source batch amount and 1000 mL input water, not a measured final makeup. API separately reports volume 1004 mL and does not consistently derive its g_l by dividing these masses by that volume; no convenient denominator is selected or new rate calculated.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "8.7", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit current API main g_l equals this stored numerical rate and is credited as a provider assertion. The primary gives the source batch amount and 1000 mL input water, not a measured final makeup. API separately reports volume 1004 mL and does not consistently derive its g_l by dividing these masses by that volume; no convenient denominator is selected or new rate calculated."}, {"path": "data/normalized_yaml/bacterial/clostridium_viride_medium.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "8.7", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit current API main g_l equals this stored numerical rate and is credited as a provider assertion. The primary gives the source batch amount and 1000 mL input water, not a measured final makeup. API separately reports volume 1004 mL and does not consistently derive its g_l by dividing these masses by that volume; no convenient denominator is selected or new rate calculated."}]}, {"quantity_id": "q3", "topic": "Yeast extract", "source": [{"evidence_id": "api526", "reference": "https://mediadive.dsmz.de/rest/medium/526", "raw_path": "REVIEW_WORK/batch064/source02-04/api526.bin", "raw_sha256": "01836967bf3384dfae78e42a3e14a300c515ed714676eb7eef7e856596a1ac89", "locator": "$.data.solutions[0].recipe[2]", "accessed_at": "2026-10-28T10:58:25.078229Z", "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 7.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 7.5,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound": "Yeast extract", "compound_id": 16, "amount": 7.5, "unit": "g", "g_l": 7.5, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm526", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium526.pdf", "raw_path": "REVIEW_WORK/batch064/source02-04/dsm526.bin", "raw_sha256": "970d6cccca0169339385018b2f55acaf2d3167714d213119d6b9f7d654090310", "locator": "PDF extracted line 5; visually checked page", "accessed_at": "2026-10-28T10:58:25.212182Z", "quote": "   Yeast extract                                               7.50         g"}], "decision": "evidence_only", "rationale": "The explicit current API main g_l equals this stored numerical rate and is credited as a provider assertion. The primary gives the source batch amount and 1000 mL input water, not a measured final makeup. API separately reports volume 1004 mL and does not consistently derive its g_l by dividing these masses by that volume; no convenient denominator is selected or new rate calculated.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "7.5", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit current API main g_l equals this stored numerical rate and is credited as a provider assertion. The primary gives the source batch amount and 1000 mL input water, not a measured final makeup. API separately reports volume 1004 mL and does not consistently derive its g_l by dividing these masses by that volume; no convenient denominator is selected or new rate calculated."}, {"path": "data/normalized_yaml/bacterial/clostridium_viride_medium.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "7.5", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit current API main g_l equals this stored numerical rate and is credited as a provider assertion. The primary gives the source batch amount and 1000 mL input water, not a measured final makeup. API separately reports volume 1004 mL and does not consistently derive its g_l by dividing these masses by that volume; no convenient denominator is selected or new rate calculated."}]}, {"quantity_id": "q4", "topic": "Sodium resazurin", "source": [{"evidence_id": "api526", "reference": "https://mediadive.dsmz.de/rest/medium/526", "raw_path": "REVIEW_WORK/batch064/source02-04/api526.bin", "raw_sha256": "01836967bf3384dfae78e42a3e14a300c515ed714676eb7eef7e856596a1ac89", "locator": "$.data.solutions[0].recipe[4]", "accessed_at": "2026-10-28T10:58:25.078229Z", "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.0005,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound": "Sodium resazurin", "compound_id": 1852, "attribute": "0.1% w/v", "amount": 0.5, "unit": "ml", "g_l": 0.0005, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm526", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium526.pdf", "raw_path": "REVIEW_WORK/batch064/source02-04/dsm526.bin", "raw_sha256": "970d6cccca0169339385018b2f55acaf2d3167714d213119d6b9f7d654090310", "locator": "PDF extracted line 7; visually checked page", "accessed_at": "2026-10-28T10:58:25.212182Z", "quote": "   Sodium resazurin (0.1% w/v)                                 0.50        ml"}], "decision": "evidence_only", "rationale": "The explicit current API main g_l equals this stored numerical rate and is credited as a provider assertion. The primary gives the source batch amount and 1000 mL input water, not a measured final makeup. API separately reports volume 1004 mL and does not consistently derive its g_l by dividing these masses by that volume; no convenient denominator is selected or new rate calculated.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.0005", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit current API main g_l equals this stored numerical rate and is credited as a provider assertion. The primary gives the source batch amount and 1000 mL input water, not a measured final makeup. API separately reports volume 1004 mL and does not consistently derive its g_l by dividing these masses by that volume; no convenient denominator is selected or new rate calculated."}, {"path": "data/normalized_yaml/bacterial/clostridium_viride_medium.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.0005", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit current API main g_l equals this stored numerical rate and is credited as a provider assertion. The primary gives the source batch amount and 1000 mL input water, not a measured final makeup. API separately reports volume 1004 mL and does not consistently derive its g_l by dividing these masses by that volume; no convenient denominator is selected or new rate calculated."}]}, {"quantity_id": "q5", "topic": "NaHCO3", "source": [{"evidence_id": "api526", "reference": "https://mediadive.dsmz.de/rest/medium/526", "raw_path": "REVIEW_WORK/batch064/source02-04/api526.bin", "raw_sha256": "01836967bf3384dfae78e42a3e14a300c515ed714676eb7eef7e856596a1ac89", "locator": "$.data.solutions[0].recipe[5]", "accessed_at": "2026-10-28T10:58:25.078229Z", "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"amount\": 2.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.5,\n                        \"mmol_l\": 29.7594,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 6, "compound": "NaHCO3", "compound_id": 55, "amount": 2.5, "unit": "g", "g_l": 2.5, "mmol_l": 29.7594, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm526", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium526.pdf", "raw_path": "REVIEW_WORK/batch064/source02-04/dsm526.bin", "raw_sha256": "970d6cccca0169339385018b2f55acaf2d3167714d213119d6b9f7d654090310", "locator": "PDF extracted line 8; visually checked page", "accessed_at": "2026-10-28T10:58:25.212182Z", "quote": "   NaHCO3                                                      2.50         g"}], "decision": "evidence_only", "rationale": "The explicit current API main g_l equals this stored numerical rate and is credited as a provider assertion. The primary gives the source batch amount and 1000 mL input water, not a measured final makeup. API separately reports volume 1004 mL and does not consistently derive its g_l by dividing these masses by that volume; no convenient denominator is selected or new rate calculated.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "2.5", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit current API main g_l equals this stored numerical rate and is credited as a provider assertion. The primary gives the source batch amount and 1000 mL input water, not a measured final makeup. API separately reports volume 1004 mL and does not consistently derive its g_l by dividing these masses by that volume; no convenient denominator is selected or new rate calculated."}, {"path": "data/normalized_yaml/bacterial/clostridium_viride_medium.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "2.5", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit current API main g_l equals this stored numerical rate and is credited as a provider assertion. The primary gives the source batch amount and 1000 mL input water, not a measured final makeup. API separately reports volume 1004 mL and does not consistently derive its g_l by dividing these masses by that volume; no convenient denominator is selected or new rate calculated."}]}, {"quantity_id": "q6", "topic": "L-Cysteine HCl x H2O", "source": [{"evidence_id": "api526", "reference": "https://mediadive.dsmz.de/rest/medium/526", "raw_path": "REVIEW_WORK/batch064/source02-04/api526.bin", "raw_sha256": "01836967bf3384dfae78e42a3e14a300c515ed714676eb7eef7e856596a1ac89", "locator": "$.data.solutions[0].recipe[6]", "accessed_at": "2026-10-28T10:58:25.078229Z", "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"L-Cysteine HCl x H2O\",\n                        \"compound_id\": 770,\n                        \"amount\": 0.25,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\": 1.4234,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 7, "compound": "L-Cysteine HCl x H2O", "compound_id": 770, "amount": 0.25, "unit": "g", "g_l": 0.25, "mmol_l": 1.4234, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm526", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium526.pdf", "raw_path": "REVIEW_WORK/batch064/source02-04/dsm526.bin", "raw_sha256": "970d6cccca0169339385018b2f55acaf2d3167714d213119d6b9f7d654090310", "locator": "PDF extracted line 9; visually checked page", "accessed_at": "2026-10-28T10:58:25.212182Z", "quote": "   L-Cysteine HCl x H2O                                        0.25         g"}], "decision": "evidence_only", "rationale": "The explicit current API main g_l equals this stored numerical rate and is credited as a provider assertion. The primary gives the source batch amount and 1000 mL input water, not a measured final makeup. API separately reports volume 1004 mL and does not consistently derive its g_l by dividing these masses by that volume; no convenient denominator is selected or new rate calculated.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.25", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit current API main g_l equals this stored numerical rate and is credited as a provider assertion. The primary gives the source batch amount and 1000 mL input water, not a measured final makeup. API separately reports volume 1004 mL and does not consistently derive its g_l by dividing these masses by that volume; no convenient denominator is selected or new rate calculated."}, {"path": "data/normalized_yaml/bacterial/clostridium_viride_medium.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.25", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit current API main g_l equals this stored numerical rate and is credited as a provider assertion. The primary gives the source batch amount and 1000 mL input water, not a measured final makeup. API separately reports volume 1004 mL and does not consistently derive its g_l by dividing these masses by that volume; no convenient denominator is selected or new rate calculated."}]}, {"quantity_id": "q7", "topic": "Nitrilotriacetic acid stock stage", "source": [{"evidence_id": "api526", "reference": "https://mediadive.dsmz.de/rest/medium/526", "raw_path": "REVIEW_WORK/batch064/source02-04/api526.bin", "raw_sha256": "01836967bf3384dfae78e42a3e14a300c515ed714676eb7eef7e856596a1ac89", "locator": "$.data.solutions[1].recipe[0]", "accessed_at": "2026-10-28T10:58:25.078229Z", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Nitrilotriacetic acid\",\n                        \"compound_id\": 189,\n                        \"attribute\": \"NTA\",\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 5,\n                        \"mmol_l\": 26.1588,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound": "Nitrilotriacetic acid", "compound_id": 189, "attribute": "NTA", "amount": 5, "unit": "g", "g_l": 5, "mmol_l": 26.1588, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm526", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium526.pdf", "raw_path": "REVIEW_WORK/batch064/source02-04/dsm526.bin", "raw_sha256": "970d6cccca0169339385018b2f55acaf2d3167714d213119d6b9f7d654090310", "locator": "PDF extracted line 23; visually checked page", "accessed_at": "2026-10-28T10:58:25.212182Z", "quote": "   Nitrilotriacetic acid (NTA)                                 5.00         g"}], "decision": "correct", "rationale": "This explicit API g_l and primary amount belong to the separate Trace elements solution VR stock. The value is credited as stock strength but its direct main-medium placement is incorrect. Restore the stock composition and separate batch receiving dose; do not label these as final-medium concentrations.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "5", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This explicit API g_l and primary amount belong to the separate Trace elements solution VR stock. The value is credited as stock strength but its direct main-medium placement is incorrect. Restore the stock composition and separate batch receiving dose; do not label these as final-medium concentrations."}, {"path": "data/normalized_yaml/bacterial/clostridium_viride_medium.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "5", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This explicit API g_l and primary amount belong to the separate Trace elements solution VR stock. The value is credited as stock strength but its direct main-medium placement is incorrect. Restore the stock composition and separate batch receiving dose; do not label these as final-medium concentrations."}]}, {"quantity_id": "q8", "topic": "MgSO4 x 7 H2O stock stage", "source": [{"evidence_id": "api526", "reference": "https://mediadive.dsmz.de/rest/medium/526", "raw_path": "REVIEW_WORK/batch064/source02-04/api526.bin", "raw_sha256": "01836967bf3384dfae78e42a3e14a300c515ed714676eb7eef7e856596a1ac89", "locator": "$.data.solutions[1].recipe[1]", "accessed_at": "2026-10-28T10:58:25.078229Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 24,\n                        \"unit\": \"g\",\n                        \"g_l\": 24,\n                        \"mmol_l\": 97.3726,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound": "MgSO4 x 7 H2O", "compound_id": 8, "amount": 24, "unit": "g", "g_l": 24, "mmol_l": 97.3726, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm526", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium526.pdf", "raw_path": "REVIEW_WORK/batch064/source02-04/dsm526.bin", "raw_sha256": "970d6cccca0169339385018b2f55acaf2d3167714d213119d6b9f7d654090310", "locator": "PDF extracted line 24; visually checked page", "accessed_at": "2026-10-28T10:58:25.212182Z", "quote": "   MgSO4 x 7 H2O                                              24.00         g"}], "decision": "correct", "rationale": "This explicit API g_l and primary amount belong to the separate Trace elements solution VR stock. The value is credited as stock strength but its direct main-medium placement is incorrect. Restore the stock composition and separate batch receiving dose; do not label these as final-medium concentrations.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "24", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This explicit API g_l and primary amount belong to the separate Trace elements solution VR stock. The value is credited as stock strength but its direct main-medium placement is incorrect. Restore the stock composition and separate batch receiving dose; do not label these as final-medium concentrations."}, {"path": "data/normalized_yaml/bacterial/clostridium_viride_medium.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "24", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This explicit API g_l and primary amount belong to the separate Trace elements solution VR stock. The value is credited as stock strength but its direct main-medium placement is incorrect. Restore the stock composition and separate batch receiving dose; do not label these as final-medium concentrations."}]}, {"quantity_id": "q9", "topic": "CaCl2 x 2 H2O stock stage", "source": [{"evidence_id": "api526", "reference": "https://mediadive.dsmz.de/rest/medium/526", "raw_path": "REVIEW_WORK/batch064/source02-04/api526.bin", "raw_sha256": "01836967bf3384dfae78e42a3e14a300c515ed714676eb7eef7e856596a1ac89", "locator": "$.data.solutions[1].recipe[2]", "accessed_at": "2026-10-28T10:58:25.078229Z", "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 3.40101,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound": "CaCl2 x 2 H2O", "compound_id": 7, "amount": 0.5, "unit": "g", "g_l": 0.5, "mmol_l": 3.40101, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm526", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium526.pdf", "raw_path": "REVIEW_WORK/batch064/source02-04/dsm526.bin", "raw_sha256": "970d6cccca0169339385018b2f55acaf2d3167714d213119d6b9f7d654090310", "locator": "PDF extracted line 25; visually checked page", "accessed_at": "2026-10-28T10:58:25.212182Z", "quote": "   CaCl2 x 2 H2O                                               0.50         g"}], "decision": "correct", "rationale": "This explicit API g_l and primary amount belong to the separate Trace elements solution VR stock. The value is credited as stock strength but its direct main-medium placement is incorrect. Restore the stock composition and separate batch receiving dose; do not label these as final-medium concentrations.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This explicit API g_l and primary amount belong to the separate Trace elements solution VR stock. The value is credited as stock strength but its direct main-medium placement is incorrect. Restore the stock composition and separate batch receiving dose; do not label these as final-medium concentrations."}, {"path": "data/normalized_yaml/bacterial/clostridium_viride_medium.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This explicit API g_l and primary amount belong to the separate Trace elements solution VR stock. The value is credited as stock strength but its direct main-medium placement is incorrect. Restore the stock composition and separate batch receiving dose; do not label these as final-medium concentrations."}]}, {"quantity_id": "q10", "topic": "FeSO4 x 7 H2O stock stage", "source": [{"evidence_id": "api526", "reference": "https://mediadive.dsmz.de/rest/medium/526", "raw_path": "REVIEW_WORK/batch064/source02-04/api526.bin", "raw_sha256": "01836967bf3384dfae78e42a3e14a300c515ed714676eb7eef7e856596a1ac89", "locator": "$.data.solutions[1].recipe[3]", "accessed_at": "2026-10-28T10:58:25.078229Z", "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 1.79846,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound": "FeSO4 x 7 H2O", "compound_id": 12, "amount": 0.5, "unit": "g", "g_l": 0.5, "mmol_l": 1.79846, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm526", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium526.pdf", "raw_path": "REVIEW_WORK/batch064/source02-04/dsm526.bin", "raw_sha256": "970d6cccca0169339385018b2f55acaf2d3167714d213119d6b9f7d654090310", "locator": "PDF extracted line 26; visually checked page", "accessed_at": "2026-10-28T10:58:25.212182Z", "quote": "   FeSO4 x 7 H2O                                               0.50         g"}], "decision": "correct", "rationale": "This explicit API g_l and primary amount belong to the separate Trace elements solution VR stock. The value is credited as stock strength but its direct main-medium placement is incorrect. Restore the stock composition and separate batch receiving dose; do not label these as final-medium concentrations.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This explicit API g_l and primary amount belong to the separate Trace elements solution VR stock. The value is credited as stock strength but its direct main-medium placement is incorrect. Restore the stock composition and separate batch receiving dose; do not label these as final-medium concentrations."}, {"path": "data/normalized_yaml/bacterial/clostridium_viride_medium.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This explicit API g_l and primary amount belong to the separate Trace elements solution VR stock. The value is credited as stock strength but its direct main-medium placement is incorrect. Restore the stock composition and separate batch receiving dose; do not label these as final-medium concentrations."}]}, {"quantity_id": "q11", "topic": "NiCl2 x 6 H2O stock stage", "source": [{"evidence_id": "api526", "reference": "https://mediadive.dsmz.de/rest/medium/526", "raw_path": "REVIEW_WORK/batch064/source02-04/api526.bin", "raw_sha256": "01836967bf3384dfae78e42a3e14a300c515ed714676eb7eef7e856596a1ac89", "locator": "$.data.solutions[1].recipe[4]", "accessed_at": "2026-10-28T10:58:25.078229Z", "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 0.25,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\": 1.92903,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound": "NiCl2 x 6 H2O", "compound_id": 40, "amount": 0.25, "unit": "g", "g_l": 0.25, "mmol_l": 1.92903, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm526", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium526.pdf", "raw_path": "REVIEW_WORK/batch064/source02-04/dsm526.bin", "raw_sha256": "970d6cccca0169339385018b2f55acaf2d3167714d213119d6b9f7d654090310", "locator": "PDF extracted line 27; visually checked page", "accessed_at": "2026-10-28T10:58:25.212182Z", "quote": "   NiCl2 x 6 H2O                                               0.25         g"}], "decision": "correct", "rationale": "This explicit API g_l and primary amount belong to the separate Trace elements solution VR stock. The value is credited as stock strength but its direct main-medium placement is incorrect. Restore the stock composition and separate batch receiving dose; do not label these as final-medium concentrations.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.25", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This explicit API g_l and primary amount belong to the separate Trace elements solution VR stock. The value is credited as stock strength but its direct main-medium placement is incorrect. Restore the stock composition and separate batch receiving dose; do not label these as final-medium concentrations."}, {"path": "data/normalized_yaml/bacterial/clostridium_viride_medium.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.25", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This explicit API g_l and primary amount belong to the separate Trace elements solution VR stock. The value is credited as stock strength but its direct main-medium placement is incorrect. Restore the stock composition and separate batch receiving dose; do not label these as final-medium concentrations."}]}, {"quantity_id": "q12", "topic": "ZnSO4 x 7 H2O stock stage", "source": [{"evidence_id": "api526", "reference": "https://mediadive.dsmz.de/rest/medium/526", "raw_path": "REVIEW_WORK/batch064/source02-04/api526.bin", "raw_sha256": "01836967bf3384dfae78e42a3e14a300c515ed714676eb7eef7e856596a1ac89", "locator": "$.data.solutions[1].recipe[5]", "accessed_at": "2026-10-28T10:58:25.078229Z", "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\": 0.44,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.44,\n                        \"mmol_l\": 1.53011,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 6, "compound": "ZnSO4 x 7 H2O", "compound_id": 35, "amount": 0.44, "unit": "g", "g_l": 0.44, "mmol_l": 1.53011, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm526", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium526.pdf", "raw_path": "REVIEW_WORK/batch064/source02-04/dsm526.bin", "raw_sha256": "970d6cccca0169339385018b2f55acaf2d3167714d213119d6b9f7d654090310", "locator": "PDF extracted line 28; visually checked page", "accessed_at": "2026-10-28T10:58:25.212182Z", "quote": "   ZnSO4 x 7 H2O                                               0.44         g"}], "decision": "correct", "rationale": "This explicit API g_l and primary amount belong to the separate Trace elements solution VR stock. The value is credited as stock strength but its direct main-medium placement is incorrect. Restore the stock composition and separate batch receiving dose; do not label these as final-medium concentrations.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.yaml", "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.44", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This explicit API g_l and primary amount belong to the separate Trace elements solution VR stock. The value is credited as stock strength but its direct main-medium placement is incorrect. Restore the stock composition and separate batch receiving dose; do not label these as final-medium concentrations."}, {"path": "data/normalized_yaml/bacterial/clostridium_viride_medium.yaml", "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.44", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This explicit API g_l and primary amount belong to the separate Trace elements solution VR stock. The value is credited as stock strength but its direct main-medium placement is incorrect. Restore the stock composition and separate batch receiving dose; do not label these as final-medium concentrations."}]}, {"quantity_id": "q13", "topic": "MnSO4 x H2O stock stage", "source": [{"evidence_id": "api526", "reference": "https://mediadive.dsmz.de/rest/medium/526", "raw_path": "REVIEW_WORK/batch064/source02-04/api526.bin", "raw_sha256": "01836967bf3384dfae78e42a3e14a300c515ed714676eb7eef7e856596a1ac89", "locator": "$.data.solutions[1].recipe[6]", "accessed_at": "2026-10-28T10:58:25.078229Z", "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"MnSO4 x H2O\",\n                        \"compound_id\": 14,\n                        \"amount\": 0.25,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\": 1.47915,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 7, "compound": "MnSO4 x H2O", "compound_id": 14, "amount": 0.25, "unit": "g", "g_l": 0.25, "mmol_l": 1.47915, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm526", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium526.pdf", "raw_path": "REVIEW_WORK/batch064/source02-04/dsm526.bin", "raw_sha256": "970d6cccca0169339385018b2f55acaf2d3167714d213119d6b9f7d654090310", "locator": "PDF extracted line 29; visually checked page", "accessed_at": "2026-10-28T10:58:25.212182Z", "quote": "   MnSO4 x H2O                                                 0.25         g"}], "decision": "correct", "rationale": "This explicit API g_l and primary amount belong to the separate Trace elements solution VR stock. The value is credited as stock strength but its direct main-medium placement is incorrect. Restore the stock composition and separate batch receiving dose; do not label these as final-medium concentrations.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.yaml", "field_path": "ingredients[12].concentration", "stored_value": {"value": "0.25", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This explicit API g_l and primary amount belong to the separate Trace elements solution VR stock. The value is credited as stock strength but its direct main-medium placement is incorrect. Restore the stock composition and separate batch receiving dose; do not label these as final-medium concentrations."}, {"path": "data/normalized_yaml/bacterial/clostridium_viride_medium.yaml", "field_path": "ingredients[12].concentration", "stored_value": {"value": "0.25", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This explicit API g_l and primary amount belong to the separate Trace elements solution VR stock. The value is credited as stock strength but its direct main-medium placement is incorrect. Restore the stock composition and separate batch receiving dose; do not label these as final-medium concentrations."}]}, {"quantity_id": "q14", "topic": "CoCl2 x 6 H2O stock stage", "source": [{"evidence_id": "api526", "reference": "https://mediadive.dsmz.de/rest/medium/526", "raw_path": "REVIEW_WORK/batch064/source02-04/api526.bin", "raw_sha256": "01836967bf3384dfae78e42a3e14a300c515ed714676eb7eef7e856596a1ac89", "locator": "$.data.solutions[1].recipe[7]", "accessed_at": "2026-10-28T10:58:25.078229Z", "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 0.25,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\": 1.92546,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 8, "compound": "CoCl2 x 6 H2O", "compound_id": 38, "amount": 0.25, "unit": "g", "g_l": 0.25, "mmol_l": 1.92546, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm526", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium526.pdf", "raw_path": "REVIEW_WORK/batch064/source02-04/dsm526.bin", "raw_sha256": "970d6cccca0169339385018b2f55acaf2d3167714d213119d6b9f7d654090310", "locator": "PDF extracted line 30; visually checked page", "accessed_at": "2026-10-28T10:58:25.212182Z", "quote": "   CoCl2 x 6 H2O                                               0.25         g"}], "decision": "correct", "rationale": "This explicit API g_l and primary amount belong to the separate Trace elements solution VR stock. The value is credited as stock strength but its direct main-medium placement is incorrect. Restore the stock composition and separate batch receiving dose; do not label these as final-medium concentrations.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.yaml", "field_path": "ingredients[13].concentration", "stored_value": {"value": "0.25", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This explicit API g_l and primary amount belong to the separate Trace elements solution VR stock. The value is credited as stock strength but its direct main-medium placement is incorrect. Restore the stock composition and separate batch receiving dose; do not label these as final-medium concentrations."}, {"path": "data/normalized_yaml/bacterial/clostridium_viride_medium.yaml", "field_path": "ingredients[13].concentration", "stored_value": {"value": "0.25", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This explicit API g_l and primary amount belong to the separate Trace elements solution VR stock. The value is credited as stock strength but its direct main-medium placement is incorrect. Restore the stock composition and separate batch receiving dose; do not label these as final-medium concentrations."}]}, {"quantity_id": "q15", "topic": "VOSO4 x 5 H2O stock stage", "source": [{"evidence_id": "api526", "reference": "https://mediadive.dsmz.de/rest/medium/526", "raw_path": "REVIEW_WORK/batch064/source02-04/api526.bin", "raw_sha256": "01836967bf3384dfae78e42a3e14a300c515ed714676eb7eef7e856596a1ac89", "locator": "$.data.solutions[1].recipe[8]", "accessed_at": "2026-10-28T10:58:25.078229Z", "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"VOSO4 x 5 H2O\",\n                        \"compound_id\": 277,\n                        \"amount\": 0.25,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\": 0.987826,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 9, "compound": "VOSO4 x 5 H2O", "compound_id": 277, "amount": 0.25, "unit": "g", "g_l": 0.25, "mmol_l": 0.987826, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm526", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium526.pdf", "raw_path": "REVIEW_WORK/batch064/source02-04/dsm526.bin", "raw_sha256": "970d6cccca0169339385018b2f55acaf2d3167714d213119d6b9f7d654090310", "locator": "PDF extracted line 31; visually checked page", "accessed_at": "2026-10-28T10:58:25.212182Z", "quote": "   VOSO4 x 5 H2O                                               0.25         g"}], "decision": "correct", "rationale": "This explicit API g_l and primary amount belong to the separate Trace elements solution VR stock. The value is credited as stock strength but its direct main-medium placement is incorrect. Restore the stock composition and separate batch receiving dose; do not label these as final-medium concentrations.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.yaml", "field_path": "ingredients[14].concentration", "stored_value": {"value": "0.25", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This explicit API g_l and primary amount belong to the separate Trace elements solution VR stock. The value is credited as stock strength but its direct main-medium placement is incorrect. Restore the stock composition and separate batch receiving dose; do not label these as final-medium concentrations."}, {"path": "data/normalized_yaml/bacterial/clostridium_viride_medium.yaml", "field_path": "ingredients[14].concentration", "stored_value": {"value": "0.25", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This explicit API g_l and primary amount belong to the separate Trace elements solution VR stock. The value is credited as stock strength but its direct main-medium placement is incorrect. Restore the stock composition and separate batch receiving dose; do not label these as final-medium concentrations."}]}, {"quantity_id": "q16", "topic": "Na2MoO4 x 2 H2O stock stage", "source": [{"evidence_id": "api526", "reference": "https://mediadive.dsmz.de/rest/medium/526", "raw_path": "REVIEW_WORK/batch064/source02-04/api526.bin", "raw_sha256": "01836967bf3384dfae78e42a3e14a300c515ed714676eb7eef7e856596a1ac89", "locator": "$.data.solutions[1].recipe[9]", "accessed_at": "2026-10-28T10:58:25.078229Z", "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 0.25,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.25,\n                        \"mmol_l\": 1.03327,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 10, "compound": "Na2MoO4 x 2 H2O", "compound_id": 9, "amount": 0.25, "unit": "g", "g_l": 0.25, "mmol_l": 1.03327, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm526", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium526.pdf", "raw_path": "REVIEW_WORK/batch064/source02-04/dsm526.bin", "raw_sha256": "970d6cccca0169339385018b2f55acaf2d3167714d213119d6b9f7d654090310", "locator": "PDF extracted line 32; visually checked page", "accessed_at": "2026-10-28T10:58:25.212182Z", "quote": "   Na2MoO4 x 2 H2O                                             0.25         g"}], "decision": "correct", "rationale": "This explicit API g_l and primary amount belong to the separate Trace elements solution VR stock. The value is credited as stock strength but its direct main-medium placement is incorrect. Restore the stock composition and separate batch receiving dose; do not label these as final-medium concentrations.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.yaml", "field_path": "ingredients[15].concentration", "stored_value": {"value": "0.25", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This explicit API g_l and primary amount belong to the separate Trace elements solution VR stock. The value is credited as stock strength but its direct main-medium placement is incorrect. Restore the stock composition and separate batch receiving dose; do not label these as final-medium concentrations."}, {"path": "data/normalized_yaml/bacterial/clostridium_viride_medium.yaml", "field_path": "ingredients[15].concentration", "stored_value": {"value": "0.25", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This explicit API g_l and primary amount belong to the separate Trace elements solution VR stock. The value is credited as stock strength but its direct main-medium placement is incorrect. Restore the stock composition and separate batch receiving dose; do not label these as final-medium concentrations."}]}, {"quantity_id": "q17", "topic": "CuSO4 x 5 H2O stock stage", "source": [{"evidence_id": "api526", "reference": "https://mediadive.dsmz.de/rest/medium/526", "raw_path": "REVIEW_WORK/batch064/source02-04/api526.bin", "raw_sha256": "01836967bf3384dfae78e42a3e14a300c515ed714676eb7eef7e856596a1ac89", "locator": "$.data.solutions[1].recipe[10]", "accessed_at": "2026-10-28T10:58:25.078229Z", "quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"CuSO4 x 5 H2O\",\n                        \"compound_id\": 121,\n                        \"amount\": 0.12,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.12,\n                        \"mmol_l\": 0.480604,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 11, "compound": "CuSO4 x 5 H2O", "compound_id": 121, "amount": 0.12, "unit": "g", "g_l": 0.12, "mmol_l": 0.480604, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm526", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium526.pdf", "raw_path": "REVIEW_WORK/batch064/source02-04/dsm526.bin", "raw_sha256": "970d6cccca0169339385018b2f55acaf2d3167714d213119d6b9f7d654090310", "locator": "PDF extracted line 33; visually checked page", "accessed_at": "2026-10-28T10:58:25.212182Z", "quote": "   CuSO4 x 5 H2O                                               0.12         g"}], "decision": "correct", "rationale": "This explicit API g_l and primary amount belong to the separate Trace elements solution VR stock. The value is credited as stock strength but its direct main-medium placement is incorrect. Restore the stock composition and separate batch receiving dose; do not label these as final-medium concentrations.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.yaml", "field_path": "ingredients[16].concentration", "stored_value": {"value": "0.12", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This explicit API g_l and primary amount belong to the separate Trace elements solution VR stock. The value is credited as stock strength but its direct main-medium placement is incorrect. Restore the stock composition and separate batch receiving dose; do not label these as final-medium concentrations."}, {"path": "data/normalized_yaml/bacterial/clostridium_viride_medium.yaml", "field_path": "ingredients[16].concentration", "stored_value": {"value": "0.12", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This explicit API g_l and primary amount belong to the separate Trace elements solution VR stock. The value is credited as stock strength but its direct main-medium placement is incorrect. Restore the stock composition and separate batch receiving dose; do not label these as final-medium concentrations."}]}, {"quantity_id": "q18", "topic": "VR stock receiving dose", "source": [{"evidence_id": "api526", "reference": "https://mediadive.dsmz.de/rest/medium/526", "raw_path": "REVIEW_WORK/batch064/source02-04/api526.bin", "raw_sha256": "01836967bf3384dfae78e42a3e14a300c515ed714676eb7eef7e856596a1ac89", "locator": "$.data.solutions[0].recipe[3]", "accessed_at": "2026-10-28T10:58:25.078229Z", "quote": "{\n                        \"recipe_order\": 4,\n                        \"solution\": \"Trace elements solution VR\",\n                        \"solution_id\": 1163,\n                        \"amount\": 4,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 4, "solution": "Trace elements solution VR", "solution_id": 1163, "amount": 4, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm526", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium526.pdf", "raw_path": "REVIEW_WORK/batch064/source02-04/dsm526.bin", "raw_sha256": "970d6cccca0169339385018b2f55acaf2d3167714d213119d6b9f7d654090310", "locator": "PDF extracted line 6; visually checked page", "accessed_at": "2026-10-28T10:58:25.212182Z", "quote": "   Trace elements solution VR                                  4.00        ml"}], "decision": "add", "rationale": "Both sources explicitly add 4 mL of the separate VR stock to the stated recipe. Restore this missing relationship/dose in recipe-batch context. The 1000 mL water input does not itself justify an unqualified final-liter dose.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Both sources explicitly add 4 mL of the separate VR stock to the stated recipe. Restore this missing relationship/dose in recipe-batch context. The 1000 mL water input does not itself justify an unqualified final-liter dose.", "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_viride_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Both sources explicitly add 4 mL of the separate VR stock to the stated recipe. Restore this missing relationship/dose in recipe-batch context. The 1000 mL water input does not itself justify an unqualified final-liter dose.", "missing": true}]}, {"quantity_id": "q19", "topic": "Indicator stock dose and strength", "source": [{"evidence_id": "api526", "reference": "https://mediadive.dsmz.de/rest/medium/526", "raw_path": "REVIEW_WORK/batch064/source02-04/api526.bin", "raw_sha256": "01836967bf3384dfae78e42a3e14a300c515ed714676eb7eef7e856596a1ac89", "locator": "$.data.solutions[0].recipe[4]", "accessed_at": "2026-10-28T10:58:25.078229Z", "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.0005,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound": "Sodium resazurin", "compound_id": 1852, "attribute": "0.1% w/v", "amount": 0.5, "unit": "ml", "g_l": 0.0005, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm526", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium526.pdf", "raw_path": "REVIEW_WORK/batch064/source02-04/dsm526.bin", "raw_sha256": "970d6cccca0169339385018b2f55acaf2d3167714d213119d6b9f7d654090310", "locator": "PDF extracted line 7; visually checked page", "accessed_at": "2026-10-28T10:58:25.212182Z", "quote": "   Sodium resazurin (0.1% w/v)                                 0.50        ml"}], "decision": "evidence_only", "rationale": "The source explicitly supplies 0.5 mL of 0.1% w/v sodium-resazurin solution. This is 0.5 mg per batch, consistent with the provider nominal amount. Retain supplied form, stock attributes and batch context; the existing numerical mass rate does not document the physical stock addition.", "layer_assessments": []}, {"quantity_id": "q20", "topic": "Scoped source water input — Main sol. 526", "source": [{"evidence_id": "api526", "reference": "https://mediadive.dsmz.de/rest/medium/526", "raw_path": "REVIEW_WORK/batch064/source02-04/api526.bin", "raw_sha256": "01836967bf3384dfae78e42a3e14a300c515ed714676eb7eef7e856596a1ac89", "locator": "$.data.solutions[0].recipe[7]", "accessed_at": "2026-10-28T10:58:25.078229Z", "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 8, "compound": "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "Source solvent input only; no measured final-volume or new ingredient-rate assertion.", "layer_assessments": []}, {"quantity_id": "q21", "topic": "Scoped source water input — Trace elements solution VR", "source": [{"evidence_id": "api526", "reference": "https://mediadive.dsmz.de/rest/medium/526", "raw_path": "REVIEW_WORK/batch064/source02-04/api526.bin", "raw_sha256": "01836967bf3384dfae78e42a3e14a300c515ed714676eb7eef7e856596a1ac89", "locator": "$.data.solutions[1].recipe[11]", "accessed_at": "2026-10-28T10:58:25.078229Z", "quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 12, "compound": "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "Source solvent input only; no measured final-volume or new ingredient-rate assertion.", "layer_assessments": []}, {"quantity_id": "q22", "topic": "Existing final pH range", "source": [{"evidence_id": "dsm526", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium526.pdf", "raw_path": "REVIEW_WORK/batch064/source02-04/dsm526.bin", "raw_sha256": "970d6cccca0169339385018b2f55acaf2d3167714d213119d6b9f7d654090310", "locator": "Exact visually checked PDF section", "accessed_at": "2026-10-28T10:58:25.212182Z", "quote": "After autoclaving adjust pH of medium\nto 7.6 - 7.8 using a sterile anoxic stock solution of Na2CO3 (5% w/v) prepared under 80% N\n2 and 20% CO2 gas atmosphere."}], "decision": "evidence_only", "rationale": "Existing final pH range 7.6–7.8 agrees with the source. Initial pH 7.0 belongs to a different preparation stage. Preserve both stages and their exact evidence without treating titrant strength as a dose.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.yaml", "field_path": "ph_range", "stored_value": {"min": 7.6, "max": 7.8}, "decision": "evidence_only", "rationale": "Existing final pH range 7.6–7.8 agrees with the source. Initial pH 7.0 belongs to a different preparation stage. Preserve both stages and their exact evidence without treating titrant strength as a dose."}, {"path": "data/normalized_yaml/bacterial/clostridium_viride_medium.yaml", "field_path": "ph_range", "stored_value": {"min": 7.6, "max": 7.8}, "decision": "evidence_only", "rationale": "Existing final pH range 7.6–7.8 agrees with the source. Initial pH 7.0 belongs to a different preparation stage. Preserve both stages and their exact evidence without treating titrant strength as a dose."}]}, {"quantity_id": "q23", "topic": "Existing main process and unquantified titrant dose", "source": [{"evidence_id": "api526", "reference": "https://mediadive.dsmz.de/rest/medium/526", "raw_path": "REVIEW_WORK/batch064/source02-04/api526.bin", "raw_sha256": "01836967bf3384dfae78e42a3e14a300c515ed714676eb7eef7e856596a1ac89", "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T10:58:25.078229Z", "quote": "{\n                        \"step\": \"Dissolve ingredients (except bicarbonate and cysteine), adjust pH to 7.0 with NaOH and sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min. Add and dissolve solid bicarbonate and cysteine, dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. After autoclaving adjust pH of medium to 7.6 - 7.8 using a sterile anoxic stock solution of Na2CO3 (5% w/v) prepared under 80% N2 and 20% CO2 gas atmosphere.\"\n                    }", "exact_decoded_object": {"step": "Dissolve ingredients (except bicarbonate and cysteine), adjust pH to 7.0 with NaOH and sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min. Add and dissolve solid bicarbonate and cysteine, dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. After autoclaving adjust pH of medium to 7.6 - 7.8 using a sterile anoxic stock solution of Na2CO3 (5% w/v) prepared under 80% N2 and 20% CO2 gas atmosphere."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm526", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium526.pdf", "raw_path": "REVIEW_WORK/batch064/source02-04/dsm526.bin", "raw_sha256": "970d6cccca0169339385018b2f55acaf2d3167714d213119d6b9f7d654090310", "locator": "Exact visually checked PDF section", "accessed_at": "2026-10-28T10:58:25.212182Z", "quote": "Dissolve ingredients (except bicarbonate and cysteine), adjust pH to 7.0 with NaOH and\nsparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min. Add and dissolve\nsolid bicarbonate and cysteine, dispense medium under same gas atmosphere into anoxic\nHungate-type tubes or serum vials and autoclave. After autoclaving adjust pH of medium\nto 7.6 - 7.8 using a sterile anoxic stock solution of Na2CO3 (5% w/v) prepared under 80% N\n2 and 20% CO2 gas atmosphere."}], "decision": "evidence_only", "rationale": "Existing main preparation accurately preserves initial pH 7.0, 80/20 gas, 30–45 minutes, addition order, autoclaving and final pH 7.6–7.8 using 5% w/v carbonate stock. No carbonate dose is printed, so it must not become a quantified or variable main ingredient. This is source preparation, not organism-specific growth evidence.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.yaml", "field_path": "preparation_steps[0].description", "stored_value": "Dissolve ingredients (except bicarbonate and cysteine), adjust pH to 7.0 with NaOH and sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min. Add and dissolve solid bicarbonate and cysteine, dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. After autoclaving adjust pH of medium to 7.6 - 7.8 using a sterile anoxic stock solution of Na2CO3 (5% w/v) prepared under 80% N2 and 20% CO2 gas atmosphere.", "decision": "evidence_only", "rationale": "Existing main preparation accurately preserves initial pH 7.0, 80/20 gas, 30–45 minutes, addition order, autoclaving and final pH 7.6–7.8 using 5% w/v carbonate stock. No carbonate dose is printed, so it must not become a quantified or variable main ingredient. This is source preparation, not organism-specific growth evidence."}, {"path": "data/normalized_yaml/bacterial/clostridium_viride_medium.yaml", "field_path": "preparation_steps[0].description", "stored_value": "Dissolve ingredients (except bicarbonate and cysteine), adjust pH to 7.0 with NaOH and sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45 min. Add and dissolve solid bicarbonate and cysteine, dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. After autoclaving adjust pH of medium to 7.6 - 7.8 using a sterile anoxic stock solution of Na2CO3 (5% w/v) prepared under 80% N2 and 20% CO2 gas atmosphere.", "decision": "evidence_only", "rationale": "Existing main preparation accurately preserves initial pH 7.0, 80/20 gas, 30–45 minutes, addition order, autoclaving and final pH 7.6–7.8 using 5% w/v carbonate stock. No carbonate dose is printed, so it must not become a quantified or variable main ingredient. This is source preparation, not organism-specific growth evidence."}]}, {"quantity_id": "q24", "topic": "Existing VR stock process and numerical fields", "source": [{"evidence_id": "api526", "reference": "https://mediadive.dsmz.de/rest/medium/526", "raw_path": "REVIEW_WORK/batch064/source02-04/api526.bin", "raw_sha256": "01836967bf3384dfae78e42a3e14a300c515ed714676eb7eef7e856596a1ac89", "locator": "$.data.solutions[1].steps[0]", "accessed_at": "2026-10-28T10:58:25.078229Z", "quote": "{\n                        \"step\": \"Dissolve mineral salts in 700 ml water acidified with 2 ml of conc. HCl. Separately dissolve 5.00 g of NTA in 300 ml water add 10 N NaOH until all the NTA has dissolved and the pH is 7.0. While stirring, slowly add the NTA solution to the salt solution. Stir until the solution is almost clear. Store cool and dark.\"\n                    }", "exact_decoded_object": {"step": "Dissolve mineral salts in 700 ml water acidified with 2 ml of conc. HCl. Separately dissolve 5.00 g of NTA in 300 ml water add 10 N NaOH until all the NTA has dissolved and the pH is 7.0. While stirring, slowly add the NTA solution to the salt solution. Stir until the solution is almost clear. Store cool and dark."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm526", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium526.pdf", "raw_path": "REVIEW_WORK/batch064/source02-04/dsm526.bin", "raw_sha256": "970d6cccca0169339385018b2f55acaf2d3167714d213119d6b9f7d654090310", "locator": "Exact visually checked PDF section", "accessed_at": "2026-10-28T10:58:25.212182Z", "quote": "Dissolve mineral salts in 700 ml water acidified with 2 ml of conc. HCl. Separately dissolve\n5.00 g of NTA in 300 ml water add 10 N NaOH until all the NTA has dissolved and the pH is\n7.0. While stirring, slowly add the NTA solution to the salt solution. Stir until the solution is\nalmost clear. Store cool and dark."}], "decision": "evidence_only", "rationale": "The exact stock process is already present: 700 mL salt water plus 2 mL concentrated HCl, separately 5 g NTA in 300 mL water, 10 N NaOH to pH 7.0, combination and cool/dark storage. Preserve this text at the VR stock stage. Concentrated HCl strength and NaOH dose are unspecified; input sums plus titrants do not prove a final stock volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.yaml", "field_path": "preparation_steps[1].description", "stored_value": "Dissolve mineral salts in 700 ml water acidified with 2 ml of conc. HCl. Separately dissolve 5.00 g of NTA in 300 ml water add 10 N NaOH until all the NTA has dissolved and the pH is 7.0. While stirring, slowly add the NTA solution to the salt solution. Stir until the solution is almost clear. Store cool and dark.", "decision": "evidence_only", "rationale": "The exact stock process is already present: 700 mL salt water plus 2 mL concentrated HCl, separately 5 g NTA in 300 mL water, 10 N NaOH to pH 7.0, combination and cool/dark storage. Preserve this text at the VR stock stage. Concentrated HCl strength and NaOH dose are unspecified; input sums plus titrants do not prove a final stock volume."}, {"path": "data/normalized_yaml/bacterial/clostridium_viride_medium.yaml", "field_path": "preparation_steps[1].description", "stored_value": "Dissolve mineral salts in 700 ml water acidified with 2 ml of conc. HCl. Separately dissolve 5.00 g of NTA in 300 ml water add 10 N NaOH until all the NTA has dissolved and the pH is 7.0. While stirring, slowly add the NTA solution to the salt solution. Stir until the solution is almost clear. Store cool and dark.", "decision": "evidence_only", "rationale": "The exact stock process is already present: 700 mL salt water plus 2 mL concentrated HCl, separately 5 g NTA in 300 mL water, 10 N NaOH to pH 7.0, combination and cool/dark storage. Preserve this text at the VR stock stage. Concentrated HCl strength and NaOH dose are unspecified; input sums plus titrants do not prove a final stock volume."}]}]

### Current ontology and MIM correspondence

grounding: concern. Targets: CultureMech:001657.

Every current ontology/MIM slot was checked against raw OLS and exact packaged rows. Sodium salt versus neutral dye and nickel hexahydrate versus anhydrous chloride are confirmed mismatches. Other listed hydrates retain their source forms; current preferred-row REJECTED status is preserved as catalog metadata, not a claim that the matching accession is invalid.

### History and evidence scope

provenance: concern. Targets: CultureMech:001657.

Complete selected histories, three exact concentration reports and scoped plan row were read, plus the full September report only as comparison context. The current API digest and 22 raw literal objects match historical bytes. Old retrieval times and broad recommendations are not reauthenticated; missing direct claim evidence remains unresolved.

### Growth and taxonomic evidence

scope: unknown. Targets: CultureMech:001657.

Generic cultivation applications and bacterial filing are not strain-level growth evidence. No organism-specific growth, temperature or atmosphere is inferred from names or source catalog identifiers.

### Canonical diagnostics

schema: supported. Targets: CultureMech:001657.

All four original canonical diagnostics passed. Reference checks were zero; structural and term diagnostics do not establish formulation accuracy.

## Findings

### f1: Restore the VR trace-stock stage and dose

major / open / confirmed; issue key: culturemech-001657-restore-the-vr-trace-stock-stage-and-dose.

Eleven trace-stock ingredients are published as direct main-medium components at their stock strengths. The source instead defines the separate VR solution and adds4 mL per stated recipe batch. Its preparation is already present as root step 2 but lacks the stock context. Six explicit provider main g_l values remain credited, without resolving conflicting volume metadata by assumption.

### f2: Reconcile sodium-resazurin and nickel hydrate forms

major / open / confirmed; issue key: culturemech-001657-reconcile-sodium-resazurin-and-nickel-hydrate-forms.

Ingredient 3 names sodium resazurin but CHEBI:8806 denotes neutral resazurin. Ingredient 10 names nickel chloride hexahydrate but CHEBI:34887 denotes anhydrous nickel dichloride; current CHEBI:53542 explicitly denotes the hexahydrate. Supported amounts and their source stages remain unchanged by this identifier assessment.

### f3: Link existing supported claims and preserve historical scope

minor / open / confirmed; issue key: culturemech-001657-link-existing-supported-claims-and-preserve-historical-scope.

Neither local layer provides claim-level evidence for its amounts, pH and preparation. The current response exactly authenticates 22 historical literal objects and the old response digest, but not the old access event or every historical interpretation. The September comparison report describes a different selected record; its per-final-liter assumption and absent-preparation conclusions are not adopted here.

## Recommended Actions And Acceptance Checks

### action1

In the maintained owner, restore the exact VR stock composition and separate 4 mL recipe-batch addition, removing the eleven misplaced stock-only main ingredients. Retain the supported main numerical values with provider/primary basis clearly separated, and retain existing stock preparation at its proper stage before regeneration.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action2

Verify the exact sodium-salt identifier or retain its grounding explicitly unresolved; reconcile nickel with the independently verified hexahydrate term and current mapping evidence. Preserve the supported source amounts and stock stages, and never substitute anhydrous masses or invent a salt accession.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action3

Add exact root evidence linking supported ingredient, stock, pH and preparation claims to the current source and its stage. Preserve original events byte-for-byte; append new verified context rather than rewriting history. Keep the comparison-only report explicitly scoped and do not copy its unrelated defects into this record.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local-target | data/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.yaml; Complete document | context_only | Complete selected generated record; no changes made. |
| owner-1 | data/normalized_yaml/bacterial/clostridium_viride_medium.yaml; Complete document | context_only | Complete maintained contributor including current curation history, evidence, quantities and preparation; no changes made. |
| identity-search | REVIEW_WORK/batch064/record04/identity-search.json | supports | Exact generated lineage resolves every maintained contributor; no filename-only transfer from neighboring variants. |
| historical-1 | reports/archive/media_variant_dsmz_komodo_source_duplicate_review.md; Exact selected-owner matching rows, if present, plus report purpose/method and validation claims only; all other pair-specific conclusions outside scope. | context_only | Historical source-duplicate report: only exact selected-owner rows, where present, and its stated signature method are in scope. Similarity does not prove complete preparation identity; no assertion about absent exact pairs is inferred. |
| historical-2 | reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/clostridium_viride_medium.yaml.md; Complete exact-header report, including unchanged/unsupported claims, source objects and narrative; repeated literal rows compared losslessly. | context_only | Current independent capture exactly matches the cited old response digest; 22 historical literal/decoded objects join. Access-event provenance remains historical. |
| historical-3 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.md; Complete exact-header report, including unchanged/unsupported claims, source objects and narrative; repeated literal rows compared losslessly. | context_only | Historical derivative context; current response does not authenticate the old full raw digest. Exact object matches and differences are recorded separately; old conclusions are reassessed. |
| historical-4 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/clostridium_viride_medium.md; Complete exact-header report, including unchanged/unsupported claims, source objects and narrative; repeated literal rows compared losslessly. | context_only | Historical derivative context; current response does not authenticate the old full raw digest. Exact object matches and differences are recorded separately; old conclusions are reassessed. |
| historical-5 | reports/yaml_record_review/20260922T090734Z-clostridium_aminovalericum_medium.md; Complete comparison report read; it reviews CultureMech:005889 clostridium_aminovalericum_medium, not the selected CultureMech:001657. Only its explicit DSM526 comparison claims are considered; its missing-preparation, Aerobic:Yes, extra-carbonate and identity findings are not transferred. | context_only | Comparison-only derivative context. Its per-parent-liter wording is not adopted because the primary lists water input without final makeup. Current selected owner already preserves preparation and has no extra carbonate ingredient. |
| historical-reader | REVIEW_WORK/batch064/record04/historical-reader.json | context_only | Full exact-header historical texts and scoped large report, with literal/decoded current-source joins and explicit mismatches. Historical access events are not reauthenticated. |
| historical-plan-1 | reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/plan.json; $.records[70] | context_only | Exact selected contributor plan row only, including unchanged decisions and original source provenance. Current source comparisons never reauthenticate the historical access event. |
| historical-plan-rows | REVIEW_WORK/batch064/record04/historical-plan-rows.json | context_only | Exact scoped plan-row membership; full parent payload retained as an inspected pin without transferring neighboring records. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition, _parse_api_solutions, _parse_preparation_steps | context_only | Current composition parser restricts ingredients to the primary solution, excludes solvent and recognized stock additions, and retains explicit g_l. The solution parser preserves referenced or percent-defined stocks and source attributes. Preparation parsing still concatenates all solution steps into root preparation_steps; source-stage annotation remains important. These present functions do not prove the historical execution that produced this record. |
| writer-merge | src/culturemech/merge/merger.py; merge_group | context_only | Current merge_group copies a sole contributor with merge metadata. For multiple contributors it passes records to merge_formulation_evidence, which checks compatibility; it does not authorize merging different preparation assertions. |
| writer-formulation | src/culturemech/merge/formulation.py; formulation_content, merge_formulation_evidence | context_only | Current compatibility preserves scientific fields and list order and rejects unequal formulations; only specified provenance/evidence lists are unioned. It performs no concentration conversion or stock expansion and does not authenticate historical merges. |
| writer-cleanup | scripts/cleanup_recipe_ingredients.py; merge_duplicate_ingredients, merge_ingredient_group | context_only | Current cleanup groups identical normalized names, keeps the first entry as a base, flags differing concentrations and combines a warning note; it does not sum concentrations. It can still discard distinctions when names repeat, so source stage must be retained. Current behavior does not establish the historical cause of an existing discrepancy. |
| writer-resolver | src/culturemech/enrich/dsmz_resolver.py; DSMZCompositionResolver.merge_composition | context_only | Current merge_composition copies nonplaceholder ingredients and available solutions, ph_value when absent, physical_state and medium_type. It does not copy preparation_steps or ph_range; present behavior is not proof of historical execution. |
| writer-komodo | src/culturemech/import/komodo_web_importer.py; _convert_to_culturemech | context_only | Current _convert_to_culturemech builds KOMODO identity, source mapping and aerobic notes from table flags and emits placeholder ingredients. It uses time.strftime with %f, which does not itself establish a valid fractional timestamp. Existing malformed events remain original evidence, not a license to rewrite history. |
| attached-evidence-joins | REVIEW_WORK/batch064/record04/attached-evidence-joins.json | context_only | Every existing attached evidence claim is preserved and compared to the exact freshly captured response. Matching snippets do not authenticate historical access times. |
| complete-source-rows | REVIEW_WORK/batch064/record04/complete-source-rows.json | context_only | Every source recipe row and preparation object, with exact raw substring and decoded JSON locator, kept in its own solution stage. No biological recommendation follows from provider equipment metadata. |
| dsm526 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium526.pdf; Exact source identity and scoped formulation/preparation | supports | Official DSM526 full one-page primary, text and visual read. Main recipe, eleven-component VR stock and both complete preparations are distinct. Input water and titration stocks are not final-volume declarations. |
| api526 | https://mediadive.dsmz.de/rest/medium/526; Exact source identity and scoped formulation/preparation | supports | Current exact provider DSM526 response. Six explicit main g_l values are preserved as declared values; main volume metadata is 1004 mL, so no recalculation or measured final-volume interpretation is silently imposed. VR stock g_l is a separate stage. |
| chebi53542 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_53542; _embedded.terms exact CHEBI:53542; label/definition/formula | supports | Exact current OLS nickel dichloride hexahydrate identity, definition and hydration formula; candidate supplied-form match for the source hexahydrate, not an automatic mass conversion. |
| chebi15887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_15887; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_131527; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_8806; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32139; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi91248 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_91248; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi44557 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_44557; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31795; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86158; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_75836; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_34887; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32312; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi86364 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86364; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_53503; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi132758 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_132758; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_75213; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi31440 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31440; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| quantities | REVIEW_WORK/batch064/record04/quantity-inventory.json | context_only | Complete local concentration and source-stage decision inventory; includes exact local paths and source failure limits. |
| grounding | REVIEW_WORK/batch064/record04/grounding-inventory.json | context_only | All recursive asserted identifier/label slots, exact current OLS objects and current packaged MIM preferred-row joins. |
| history | REVIEW_WORK/batch064/record04/history-and-evidence-inventory.json | context_only | Complete current history, references and attached evidence; source-specific claims are assessed without authenticating historical execution from code. |
| scalars | REVIEW_WORK/batch064/record04/scalar-census.json | context_only | Lossless scalar census of the selected target and all maintained contributors. |
| validate-schema | REVIEW_WORK/batch064/record04/validate-schema.json | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed<br> |
| validate-strict | REVIEW_WORK/batch064/record04/validate-strict.json | supports | Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                REVIEW_WORK/batch064/record04/strict.tsv<br> |
| validate-terms | REVIEW_WORK/batch064/record04/validate-terms.json | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed<br> |
| validate-references | REVIEW_WORK/batch064/record04/validate-references.json | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed<br> |

## Limits And Additional Notes

- Primary water quantities are inputs rather than explicit final-makeup instructions. API main volume 1004 mL and its declared g_l are retained as separate provider facts, without silently recalculating rates or claiming measured final concentrations.
- The source does not quantify the final carbonate-stock dose, NaOH titration volume or concentration of concentrated HCl. None is inferred from typical practice or summed solvent inputs.
- The historical aminovalericum/KOMODO report is outside selected ownership. Its missing preparation, extra carbonate and aerobic/identity findings are not transferred to this already documented DSM owner.
- No strain-level growth, taxonomic assignment or culture performance is inferred from the recipe name or generic application. Current ontology/catalog/code facts are not proof of historical validity or execution.
- Fresh review; historical lost snapshots were not reconstructed. All inspected source files remain unchanged.
- No formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T111224Z-batch064-record04-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Clostridium viride medium: trace-stock scope and supplied chemical forms'
started_at: '2026-10-28T10:58:20.672451Z'
finished_at: '2026-10-28T11:12:24.282264Z'
reviewer:
  identity: Codex independent source reviewer
  kind: agent
  independence: independent
  independence_basis: Fresh assessment of the inspected checkout and newly captured
    primary/provider/ontology evidence; no reconstruction of lost reviews and no record
    edits.
skill: .claude/skills/review-yaml-record/SKILL.md; .claude/skills/review-ingredient-concentrations/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: The selected DSM526 record and its sole owner agree with the current primary
  identity and retain both preparation descriptions. Eleven trace-stock components
  are nevertheless flattened into the main ingredient list, and the 4 mL stock addition
  is absent. Explicit API main g_l values are credited without assuming a measured
  final volume. Sodium resazurin and nickel chloride hydrate identifiers need source-form
  reconciliation; evidence placement and stock-stage annotation remain incomplete.
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
  - path: data/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.yaml
    sha256: 34e911b3094ca557a537de2682bb8d8fc95508cab9df0f354cd488fbc8d4076c
    role: target
  - path: data/normalized_yaml/bacterial/clostridium_viride_medium.yaml
    sha256: 6bf64b9c9fad2ac2b06dae4ae4f4d5cf0f3285a7925141464e7ba8d9c1b69211
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/plan.json
    sha256: bc8c96d09770525e6b6ba6dc0c7680354cf9bc6baa5249e79e82b65328203147
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/clostridium_viride_medium.yaml.md
    sha256: 05dc07833a84b78cdd1c52e2ee6d3d8b863c036f6ab5a1cf69be7ba646352747
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.md
    sha256: bbba3edf88d9ddaef6ad9650afb74976412b387ddbb9c04c8c174eaffaba1ff6
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/clostridium_viride_medium.md
    sha256: b92ff3a7742ce0296733e35b6e885bb7d1498f1f69fe8443394bfce6ed6971b7
    role: context
  - path: reports/yaml_record_review/20260922T090734Z-clostridium_aminovalericum_medium.md
    sha256: f206b96702eea896aa24d53ec02c95690810fd93a0f383cd22dc35695117b262
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
  selection: Actual batch064 native selection index 04.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:001657
targets:
- target_id: CultureMech:001657
  path: data/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.yaml
  label: clostridium_viride_medium
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_viride_medium.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Original once-only canonical command exited 0; full stdout/stderr retained
    and read.
  target_ids:
  - CultureMech:001657
  command: just validate-schema data/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.yaml
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
  - CultureMech:001657
  command: just validate-strict data/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.yaml
    --out REVIEW_WORK/batch064/record04/strict.tsv --workers 1 --quiet
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
  - CultureMech:001657
  command: just validate-terms data/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.yaml
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
  - CultureMech:001657
  command: just validate-references data/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
  scope_note: Exact selected target; scientific source and owner assessments are separate.
evidence:
- evidence_id: local-target
  kind: record_content
  reference: data/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.yaml
  locator: Complete document
  accessed_at: '2026-10-28T11:12:24.164602Z'
  support: context_only
  summary: Complete selected generated record; no changes made.
  snapshot_sha256: 34e911b3094ca557a537de2682bb8d8fc95508cab9df0f354cd488fbc8d4076c
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/clostridium_viride_medium.yaml
  locator: Complete document
  accessed_at: '2026-10-28T11:12:24.164602Z'
  support: context_only
  summary: Complete maintained contributor including current curation history, evidence,
    quantities and preparation; no changes made.
  snapshot_sha256: 6bf64b9c9fad2ac2b06dae4ae4f4d5cf0f3285a7925141464e7ba8d9c1b69211
- evidence_id: identity-search
  kind: search
  reference: REVIEW_WORK/batch064/record04/identity-search.json
  accessed_at: '2026-10-28T11:12:24.211602Z'
  support: supports
  summary: Exact generated lineage resolves every maintained contributor; no filename-only
    transfer from neighboring variants.
  search_scope: Complete recursive normalized YAML filename census including ignored
    and hidden paths; exact merged_from stems and stable identity resolve the owner;
    excluded namesakes are retained in the census. Similar names and source accessions
    are not promoted to owners.
  snapshot_sha256: c36f95fef35eb28b2d064bc1a0de2fd1b95e0e41b7756ff8bdaa2245e7ed3ffd
- evidence_id: historical-1
  kind: record_content
  reference: reports/archive/media_variant_dsmz_komodo_source_duplicate_review.md
  locator: Exact selected-owner matching rows, if present, plus report purpose/method
    and validation claims only; all other pair-specific conclusions outside scope.
  accessed_at: '2026-10-28T11:12:24.164602Z'
  support: context_only
  summary: 'Historical source-duplicate report: only exact selected-owner rows, where
    present, and its stated signature method are in scope. Similarity does not prove
    complete preparation identity; no assertion about absent exact pairs is inferred.'
  snapshot_sha256: a723d4b7950bf4ac296a8a7fe4890d4d0881199a5d17c12a5fe39c2afbc40a10
- evidence_id: historical-2
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/clostridium_viride_medium.yaml.md
  locator: Complete exact-header report, including unchanged/unsupported claims, source
    objects and narrative; repeated literal rows compared losslessly.
  accessed_at: '2026-10-28T11:12:24.164602Z'
  support: context_only
  summary: Current independent capture exactly matches the cited old response digest;
    22 historical literal/decoded objects join. Access-event provenance remains historical.
  snapshot_sha256: 05dc07833a84b78cdd1c52e2ee6d3d8b863c036f6ab5a1cf69be7ba646352747
- evidence_id: historical-3
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.md
  locator: Complete exact-header report, including unchanged/unsupported claims, source
    objects and narrative; repeated literal rows compared losslessly.
  accessed_at: '2026-10-28T11:12:24.164602Z'
  support: context_only
  summary: Historical derivative context; current response does not authenticate the
    old full raw digest. Exact object matches and differences are recorded separately;
    old conclusions are reassessed.
  snapshot_sha256: bbba3edf88d9ddaef6ad9650afb74976412b387ddbb9c04c8c174eaffaba1ff6
- evidence_id: historical-4
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/clostridium_viride_medium.md
  locator: Complete exact-header report, including unchanged/unsupported claims, source
    objects and narrative; repeated literal rows compared losslessly.
  accessed_at: '2026-10-28T11:12:24.164602Z'
  support: context_only
  summary: Historical derivative context; current response does not authenticate the
    old full raw digest. Exact object matches and differences are recorded separately;
    old conclusions are reassessed.
  snapshot_sha256: b92ff3a7742ce0296733e35b6e885bb7d1498f1f69fe8443394bfce6ed6971b7
- evidence_id: historical-5
  kind: record_content
  reference: reports/yaml_record_review/20260922T090734Z-clostridium_aminovalericum_medium.md
  locator: Complete comparison report read; it reviews CultureMech:005889 clostridium_aminovalericum_medium,
    not the selected CultureMech:001657. Only its explicit DSM526 comparison claims
    are considered; its missing-preparation, Aerobic:Yes, extra-carbonate and identity
    findings are not transferred.
  accessed_at: '2026-10-28T11:12:24.164602Z'
  support: context_only
  summary: Comparison-only derivative context. Its per-parent-liter wording is not
    adopted because the primary lists water input without final makeup. Current selected
    owner already preserves preparation and has no extra carbonate ingredient.
  snapshot_sha256: f206b96702eea896aa24d53ec02c95690810fd93a0f383cd22dc35695117b262
- evidence_id: historical-reader
  kind: record_content
  reference: REVIEW_WORK/batch064/record04/historical-reader.json
  accessed_at: '2026-10-28T11:12:24.215095Z'
  support: context_only
  summary: Full exact-header historical texts and scoped large report, with literal/decoded
    current-source joins and explicit mismatches. Historical access events are not
    reauthenticated.
  snapshot_sha256: a2577df368fced49b144482f582996ab395eaaed8c7870aa63bb9a9e2b2a2cec
- evidence_id: historical-plan-1
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/plan.json
  locator: $.records[70]
  accessed_at: '2026-10-28T11:12:24.164602Z'
  support: context_only
  summary: Exact selected contributor plan row only, including unchanged decisions
    and original source provenance. Current source comparisons never reauthenticate
    the historical access event.
  snapshot_sha256: bc8c96d09770525e6b6ba6dc0c7680354cf9bc6baa5249e79e82b65328203147
- evidence_id: historical-plan-rows
  kind: record_content
  reference: REVIEW_WORK/batch064/record04/historical-plan-rows.json
  accessed_at: '2026-10-28T11:12:24.250698Z'
  support: context_only
  summary: Exact scoped plan-row membership; full parent payload retained as an inspected
    pin without transferring neighboring records.
  snapshot_sha256: 9eeb31d0f5af895ff9d647ca7f7f59b05494bf510abf5790d465374c74c49b1e
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition, _parse_api_solutions, _parse_preparation_steps
  accessed_at: '2026-10-28T11:12:24.164602Z'
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
  accessed_at: '2026-10-28T11:12:24.164602Z'
  support: context_only
  summary: Current merge_group copies a sole contributor with merge metadata. For
    multiple contributors it passes records to merge_formulation_evidence, which checks
    compatibility; it does not authorize merging different preparation assertions.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content, merge_formulation_evidence
  accessed_at: '2026-10-28T11:12:24.164602Z'
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
  accessed_at: '2026-10-28T11:12:24.164602Z'
  support: context_only
  summary: Current cleanup groups identical normalized names, keeps the first entry
    as a base, flags differing concentrations and combines a warning note; it does
    not sum concentrations. It can still discard distinctions when names repeat, so
    source stage must be retained. Current behavior does not establish the historical
    cause of an existing discrepancy.
  snapshot_sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
- evidence_id: writer-resolver
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: DSMZCompositionResolver.merge_composition
  accessed_at: '2026-10-28T11:12:24.164602Z'
  support: context_only
  summary: Current merge_composition copies nonplaceholder ingredients and available
    solutions, ph_value when absent, physical_state and medium_type. It does not copy
    preparation_steps or ph_range; present behavior is not proof of historical execution.
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: writer-komodo
  kind: record_content
  reference: src/culturemech/import/komodo_web_importer.py
  locator: _convert_to_culturemech
  accessed_at: '2026-10-28T11:12:24.164602Z'
  support: context_only
  summary: Current _convert_to_culturemech builds KOMODO identity, source mapping
    and aerobic notes from table flags and emits placeholder ingredients. It uses
    time.strftime with %f, which does not itself establish a valid fractional timestamp.
    Existing malformed events remain original evidence, not a license to rewrite history.
  snapshot_sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
- evidence_id: attached-evidence-joins
  kind: record_content
  reference: REVIEW_WORK/batch064/record04/attached-evidence-joins.json
  accessed_at: '2026-10-28T11:12:24.254059Z'
  support: context_only
  summary: Every existing attached evidence claim is preserved and compared to the
    exact freshly captured response. Matching snippets do not authenticate historical
    access times.
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
- evidence_id: complete-source-rows
  kind: record_content
  reference: REVIEW_WORK/batch064/record04/complete-source-rows.json
  accessed_at: '2026-10-28T11:12:24.256774Z'
  support: context_only
  summary: Every source recipe row and preparation object, with exact raw substring
    and decoded JSON locator, kept in its own solution stage. No biological recommendation
    follows from provider equipment metadata.
  snapshot_sha256: 01e1a31e5e5aeea04582a538ee416698cddc1bdda48846d995cc44b3b43e148c
- evidence_id: dsm526
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium526.pdf
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T10:58:25.212182Z'
  support: supports
  summary: Official DSM526 full one-page primary, text and visual read. Main recipe,
    eleven-component VR stock and both complete preparations are distinct. Input water
    and titration stocks are not final-volume declarations.
  snapshot_sha256: 970d6cccca0169339385018b2f55acaf2d3167714d213119d6b9f7d654090310
- evidence_id: api526
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/526
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T10:58:25.078229Z'
  support: supports
  summary: Current exact provider DSM526 response. Six explicit main g_l values are
    preserved as declared values; main volume metadata is 1004 mL, so no recalculation
    or measured final-volume interpretation is silently imposed. VR stock g_l is a
    separate stage.
  snapshot_sha256: 01836967bf3384dfae78e42a3e14a300c515ed714676eb7eef7e856596a1ac89
- evidence_id: chebi53542
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_53542
  locator: _embedded.terms exact CHEBI:53542; label/definition/formula
  accessed_at: '2026-10-28T10:58:30.453440Z'
  support: supports
  summary: Exact current OLS nickel dichloride hexahydrate identity, definition and
    hydration formula; candidate supplied-form match for the source hexahydrate, not
    an automatic mass conversion.
  snapshot_sha256: 1e444345efd33c02d5050deadd66637cc6dae004c55e6962c62abd172291e526
- evidence_id: chebi15887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_15887
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:58:25.862062Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 341e86d5b83fe219f73b529b4fed1cd225c5075bfef041fc4affdce14a5f60e8
- evidence_id: chebi131527
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_131527
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:58:25.374657Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 97e9c2b05f3937c5beeebb4e6338aa6730f9e422ee0e7570a6c622dda8d97a86
- evidence_id: chebi8806
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_8806
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:58:32.585266Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: ceb05e9dd7fba3802d28b34c50bbb604ded87951e4ea3a812739824a84648d72
- evidence_id: chebi32139
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32139
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:58:28.626109Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 314c75cd12ea5d1343b4c0bafd40e0ad72c15b19d64f8cb9152000c0d8839f56
- evidence_id: chebi91248
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_91248
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:58:32.995475Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 98a5682728cfda4162de150a88ae8c4b3a70c2d7c248634a5108be50a888a692
- evidence_id: chebi44557
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_44557
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:58:29.841544Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 371aa3b809db6c5d1ec8f8b8be40011e6b1132b1c0be40e70fb927788728d65a
- evidence_id: chebi31795
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31795
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:58:28.650200Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 1635f67d01e00cabdef4ed0d9ef6d5383787c56bd0447051deb90ad353b499a2
- evidence_id: chebi86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86158
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:58:31.715177Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: df8f702eb5b9d3e50209bfa2b0c4b6f1db30c116e56a58e348cbd4bf3bc0ebc1
- evidence_id: chebi75836
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_75836
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:58:31.303628Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: e12b865122aab78645385260e1e83ff28f3c45365cb67c9181166628f68974b3
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_34887
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:58:29.817042Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: a43b8268f70ae50c4cfbc53e12bbd195618c521619cfab8f71d3704b338af95b
- evidence_id: chebi32312
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32312
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:58:29.181912Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 6bf1390236046f1cb7b21e2fc324fccba6e6eac2bc4e519f12d998f0edce671b
- evidence_id: chebi86364
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86364
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:58:32.319749Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 0e8fbfc2ee82502bd7a5b4b3ba6cfaaae0ad1779400d07af8e2e0f726af793e9
- evidence_id: chebi53503
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_53503
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:58:30.430311Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 31dc996638b0cc1341ed24fcb38ec344af726c99d376ac94e952210fcb9ed583
- evidence_id: chebi132758
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_132758
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:58:25.681643Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 5b27d8ade0a3fcaa9512a9ee14e0b1efd90fe035ffc28ee4521225bc6761fc13
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_75213
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:58:31.252961Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 0271a149a298ff837ad8f690ce8cb0acf111f5d25c5efaf6fa828401ab951d56
- evidence_id: chebi31440
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31440
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:58:28.586742Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 453e496e1e59b82bb42cd3252d410b9dc77d0c11e49f3da70496a82978e80505
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch064/record04/quantity-inventory.json
  accessed_at: '2026-10-28T11:12:24.281586Z'
  support: context_only
  summary: Complete local concentration and source-stage decision inventory; includes
    exact local paths and source failure limits.
  snapshot_sha256: dc1c14b60727b330e9b83d38369c76cac3b03ecf7769ac2585aabcfea437a5ee
- evidence_id: grounding
  kind: record_content
  reference: REVIEW_WORK/batch064/record04/grounding-inventory.json
  accessed_at: '2026-10-28T11:12:24.281641Z'
  support: context_only
  summary: All recursive asserted identifier/label slots, exact current OLS objects
    and current packaged MIM preferred-row joins.
  snapshot_sha256: 390b4ba3ddf79f68d224dc63774f55cb188b6682cae15d4f1980f1a3548fc390
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch064/record04/history-and-evidence-inventory.json
  accessed_at: '2026-10-28T11:12:24.281879Z'
  support: context_only
  summary: Complete current history, references and attached evidence; source-specific
    claims are assessed without authenticating historical execution from code.
  snapshot_sha256: acd8c113700ef1cd3340677efa54e25538bb0740734814bdd6d724b05129347d
- evidence_id: scalars
  kind: record_content
  reference: REVIEW_WORK/batch064/record04/scalar-census.json
  accessed_at: '2026-10-28T11:12:24.281901Z'
  support: context_only
  summary: Lossless scalar census of the selected target and all maintained contributors.
  snapshot_sha256: 136c0de55eaadab554ffda31651ae013499cb19a2607c99e85293b883222f68b
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch064/record04/validate-schema.json
  accessed_at: '2026-10-28T10:58:21.700978Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed

    '
  snapshot_sha256: bafeb45b64b7d21e2a9696147309cbf6f753df2d6815bed90020f73b739a5044
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch064/record04/validate-strict.json
  accessed_at: '2026-10-28T10:58:22.615093Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         REVIEW_WORK/batch064/record04/strict.tsv\n"
  snapshot_sha256: db131a5c92f6049992c4011e6f6fd55e6a3a15b8784b9cb2fa6de38ef0780848
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch064/record04/validate-terms.json
  accessed_at: '2026-10-28T10:58:23.649870Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed

    '
  snapshot_sha256: a969e49259cb99e3eda83eb8e963bf136980b3808c5168fd7779279cec38d08d
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch064/record04/validate-references.json
  accessed_at: '2026-10-28T10:58:24.343683Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed

    '
  snapshot_sha256: fcc8f450d8696faeaaca4e68a4372c1717a9575d6dd95a8da859f4c154afcc5d
assessments:
- assessment_id: a1
  area: identity
  topic: Exact DSM526 selected identity
  outcome: supported
  summary: The selected target and sole maintained owner identify DSM526/Clostridium
    viride and agree with the current primary/API. A historical report on a separate
    KOMODO aminovalericum record is comparison context only; its identity conflict,
    absent preparation, aerobic flag and extra carbonate are not findings on this
    record.
  target_ids:
  - CultureMech:001657
  evidence_ids:
  - local-target
  - owner-1
  - identity-search
  - dsm526
  - api526
  - historical-reader
- assessment_id: a2
  area: completeness
  topic: Existing preparation is retained
  outcome: concern
  summary: Both source preparation descriptions and the final pH range already exist
    and are supported. The important loss is stock structure and claim linkage, not
    wholesale missing preparation. Variable titrant doses and unspecified concentrated-acid
    strength remain unknown.
  target_ids:
  - CultureMech:001657
  evidence_ids:
  - dsm526
  - api526
  - quantities
  - owner-1
- assessment_id: a3
  area: quantity
  topic: Quantity scope and inventory
  outcome: concern
  summary: Every selected target/owner concentration field has an explicit disposition;
    scoped dependency fields and source-only preparation are separate from receiving-medium
    rates.
  target_ids:
  - CultureMech:001657
  evidence_ids:
  - quantities
  details: '[{"quantity_id": "q1", "topic": "5-Aminovaleric acid", "source": [{"evidence_id":
    "api526", "reference": "https://mediadive.dsmz.de/rest/medium/526", "raw_path":
    "REVIEW_WORK/batch064/source02-04/api526.bin", "raw_sha256": "01836967bf3384dfae78e42a3e14a300c515ed714676eb7eef7e856596a1ac89",
    "locator": "$.data.solutions[0].recipe[0]", "accessed_at": "2026-10-28T10:58:25.078229Z",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"5-Aminovaleric acid\",\n                        \"compound_id\": 538,\n                        \"amount\":
    15,\n                        \"unit\": \"g\",\n                        \"g_l\":
    15,\n                        \"mmol_l\": 128.041,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound":
    "5-Aminovaleric acid", "compound_id": 538, "amount": 15, "unit": "g", "g_l": 15,
    "mmol_l": 128.041, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, {"evidence_id":
    "dsm526", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium526.pdf",
    "raw_path": "REVIEW_WORK/batch064/source02-04/dsm526.bin", "raw_sha256": "970d6cccca0169339385018b2f55acaf2d3167714d213119d6b9f7d654090310",
    "locator": "PDF extracted line 3; visually checked page", "accessed_at": "2026-10-28T10:58:25.212182Z",
    "quote": "   5-Aminovaleric acid                                        15.00         g"}],
    "decision": "evidence_only", "rationale": "The explicit current API main g_l equals
    this stored numerical rate and is credited as a provider assertion. The primary
    gives the source batch amount and 1000 mL input water, not a measured final makeup.
    API separately reports volume 1004 mL and does not consistently derive its g_l
    by dividing these masses by that volume; no convenient denominator is selected
    or new rate calculated.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "15",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit current
    API main g_l equals this stored numerical rate and is credited as a provider assertion.
    The primary gives the source batch amount and 1000 mL input water, not a measured
    final makeup. API separately reports volume 1004 mL and does not consistently
    derive its g_l by dividing these masses by that volume; no convenient denominator
    is selected or new rate calculated."}, {"path": "data/normalized_yaml/bacterial/clostridium_viride_medium.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "15",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit current
    API main g_l equals this stored numerical rate and is credited as a provider assertion.
    The primary gives the source batch amount and 1000 mL input water, not a measured
    final makeup. API separately reports volume 1004 mL and does not consistently
    derive its g_l by dividing these masses by that volume; no convenient denominator
    is selected or new rate calculated."}]}, {"quantity_id": "q2", "topic": "K2HPO4",
    "source": [{"evidence_id": "api526", "reference": "https://mediadive.dsmz.de/rest/medium/526",
    "raw_path": "REVIEW_WORK/batch064/source02-04/api526.bin", "raw_sha256": "01836967bf3384dfae78e42a3e14a300c515ed714676eb7eef7e856596a1ac89",
    "locator": "$.data.solutions[0].recipe[1]", "accessed_at": "2026-10-28T10:58:25.078229Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\":
    8.7,\n                        \"unit\": \"g\",\n                        \"g_l\":
    8.7,\n                        \"mmol_l\": 49.9495,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound":
    "K2HPO4", "compound_id": 10, "amount": 8.7, "unit": "g", "g_l": 8.7, "mmol_l":
    49.9495, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm526",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium526.pdf",
    "raw_path": "REVIEW_WORK/batch064/source02-04/dsm526.bin", "raw_sha256": "970d6cccca0169339385018b2f55acaf2d3167714d213119d6b9f7d654090310",
    "locator": "PDF extracted line 4; visually checked page", "accessed_at": "2026-10-28T10:58:25.212182Z",
    "quote": "   K2HPO4                                                      8.70         g"}],
    "decision": "evidence_only", "rationale": "The explicit current API main g_l equals
    this stored numerical rate and is credited as a provider assertion. The primary
    gives the source batch amount and 1000 mL input water, not a measured final makeup.
    API separately reports volume 1004 mL and does not consistently derive its g_l
    by dividing these masses by that volume; no convenient denominator is selected
    or new rate calculated.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "8.7",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit current
    API main g_l equals this stored numerical rate and is credited as a provider assertion.
    The primary gives the source batch amount and 1000 mL input water, not a measured
    final makeup. API separately reports volume 1004 mL and does not consistently
    derive its g_l by dividing these masses by that volume; no convenient denominator
    is selected or new rate calculated."}, {"path": "data/normalized_yaml/bacterial/clostridium_viride_medium.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "8.7",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit current
    API main g_l equals this stored numerical rate and is credited as a provider assertion.
    The primary gives the source batch amount and 1000 mL input water, not a measured
    final makeup. API separately reports volume 1004 mL and does not consistently
    derive its g_l by dividing these masses by that volume; no convenient denominator
    is selected or new rate calculated."}]}, {"quantity_id": "q3", "topic": "Yeast
    extract", "source": [{"evidence_id": "api526", "reference": "https://mediadive.dsmz.de/rest/medium/526",
    "raw_path": "REVIEW_WORK/batch064/source02-04/api526.bin", "raw_sha256": "01836967bf3384dfae78e42a3e14a300c515ed714676eb7eef7e856596a1ac89",
    "locator": "$.data.solutions[0].recipe[2]", "accessed_at": "2026-10-28T10:58:25.078229Z",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\":
    7.5,\n                        \"unit\": \"g\",\n                        \"g_l\":
    7.5,\n                        \"optional\": 0\n                    }", "exact_decoded_object":
    {"recipe_order": 3, "compound": "Yeast extract", "compound_id": 16, "amount":
    7.5, "unit": "g", "g_l": 7.5, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, {"evidence_id":
    "dsm526", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium526.pdf",
    "raw_path": "REVIEW_WORK/batch064/source02-04/dsm526.bin", "raw_sha256": "970d6cccca0169339385018b2f55acaf2d3167714d213119d6b9f7d654090310",
    "locator": "PDF extracted line 5; visually checked page", "accessed_at": "2026-10-28T10:58:25.212182Z",
    "quote": "   Yeast extract                                               7.50         g"}],
    "decision": "evidence_only", "rationale": "The explicit current API main g_l equals
    this stored numerical rate and is credited as a provider assertion. The primary
    gives the source batch amount and 1000 mL input water, not a measured final makeup.
    API separately reports volume 1004 mL and does not consistently derive its g_l
    by dividing these masses by that volume; no convenient denominator is selected
    or new rate calculated.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "7.5",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit current
    API main g_l equals this stored numerical rate and is credited as a provider assertion.
    The primary gives the source batch amount and 1000 mL input water, not a measured
    final makeup. API separately reports volume 1004 mL and does not consistently
    derive its g_l by dividing these masses by that volume; no convenient denominator
    is selected or new rate calculated."}, {"path": "data/normalized_yaml/bacterial/clostridium_viride_medium.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "7.5",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit current
    API main g_l equals this stored numerical rate and is credited as a provider assertion.
    The primary gives the source batch amount and 1000 mL input water, not a measured
    final makeup. API separately reports volume 1004 mL and does not consistently
    derive its g_l by dividing these masses by that volume; no convenient denominator
    is selected or new rate calculated."}]}, {"quantity_id": "q4", "topic": "Sodium
    resazurin", "source": [{"evidence_id": "api526", "reference": "https://mediadive.dsmz.de/rest/medium/526",
    "raw_path": "REVIEW_WORK/batch064/source02-04/api526.bin", "raw_sha256": "01836967bf3384dfae78e42a3e14a300c515ed714676eb7eef7e856596a1ac89",
    "locator": "$.data.solutions[0].recipe[4]", "accessed_at": "2026-10-28T10:58:25.078229Z",
    "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\":
    \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\":
    \"ml\",\n                        \"g_l\": 0.0005,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound":
    "Sodium resazurin", "compound_id": 1852, "attribute": "0.1% w/v", "amount": 0.5,
    "unit": "ml", "g_l": 0.0005, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, {"evidence_id":
    "dsm526", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium526.pdf",
    "raw_path": "REVIEW_WORK/batch064/source02-04/dsm526.bin", "raw_sha256": "970d6cccca0169339385018b2f55acaf2d3167714d213119d6b9f7d654090310",
    "locator": "PDF extracted line 7; visually checked page", "accessed_at": "2026-10-28T10:58:25.212182Z",
    "quote": "   Sodium resazurin (0.1% w/v)                                 0.50        ml"}],
    "decision": "evidence_only", "rationale": "The explicit current API main g_l equals
    this stored numerical rate and is credited as a provider assertion. The primary
    gives the source batch amount and 1000 mL input water, not a measured final makeup.
    API separately reports volume 1004 mL and does not consistently derive its g_l
    by dividing these masses by that volume; no convenient denominator is selected
    or new rate calculated.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.yaml",
    "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.0005",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit current
    API main g_l equals this stored numerical rate and is credited as a provider assertion.
    The primary gives the source batch amount and 1000 mL input water, not a measured
    final makeup. API separately reports volume 1004 mL and does not consistently
    derive its g_l by dividing these masses by that volume; no convenient denominator
    is selected or new rate calculated."}, {"path": "data/normalized_yaml/bacterial/clostridium_viride_medium.yaml",
    "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.0005",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit current
    API main g_l equals this stored numerical rate and is credited as a provider assertion.
    The primary gives the source batch amount and 1000 mL input water, not a measured
    final makeup. API separately reports volume 1004 mL and does not consistently
    derive its g_l by dividing these masses by that volume; no convenient denominator
    is selected or new rate calculated."}]}, {"quantity_id": "q5", "topic": "NaHCO3",
    "source": [{"evidence_id": "api526", "reference": "https://mediadive.dsmz.de/rest/medium/526",
    "raw_path": "REVIEW_WORK/batch064/source02-04/api526.bin", "raw_sha256": "01836967bf3384dfae78e42a3e14a300c515ed714676eb7eef7e856596a1ac89",
    "locator": "$.data.solutions[0].recipe[5]", "accessed_at": "2026-10-28T10:58:25.078229Z",
    "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\":
    \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"amount\":
    2.5,\n                        \"unit\": \"g\",\n                        \"g_l\":
    2.5,\n                        \"mmol_l\": 29.7594,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 6, "compound":
    "NaHCO3", "compound_id": 55, "amount": 2.5, "unit": "g", "g_l": 2.5, "mmol_l":
    29.7594, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm526",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium526.pdf",
    "raw_path": "REVIEW_WORK/batch064/source02-04/dsm526.bin", "raw_sha256": "970d6cccca0169339385018b2f55acaf2d3167714d213119d6b9f7d654090310",
    "locator": "PDF extracted line 8; visually checked page", "accessed_at": "2026-10-28T10:58:25.212182Z",
    "quote": "   NaHCO3                                                      2.50         g"}],
    "decision": "evidence_only", "rationale": "The explicit current API main g_l equals
    this stored numerical rate and is credited as a provider assertion. The primary
    gives the source batch amount and 1000 mL input water, not a measured final makeup.
    API separately reports volume 1004 mL and does not consistently derive its g_l
    by dividing these masses by that volume; no convenient denominator is selected
    or new rate calculated.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.yaml",
    "field_path": "ingredients[4].concentration", "stored_value": {"value": "2.5",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit current
    API main g_l equals this stored numerical rate and is credited as a provider assertion.
    The primary gives the source batch amount and 1000 mL input water, not a measured
    final makeup. API separately reports volume 1004 mL and does not consistently
    derive its g_l by dividing these masses by that volume; no convenient denominator
    is selected or new rate calculated."}, {"path": "data/normalized_yaml/bacterial/clostridium_viride_medium.yaml",
    "field_path": "ingredients[4].concentration", "stored_value": {"value": "2.5",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit current
    API main g_l equals this stored numerical rate and is credited as a provider assertion.
    The primary gives the source batch amount and 1000 mL input water, not a measured
    final makeup. API separately reports volume 1004 mL and does not consistently
    derive its g_l by dividing these masses by that volume; no convenient denominator
    is selected or new rate calculated."}]}, {"quantity_id": "q6", "topic": "L-Cysteine
    HCl x H2O", "source": [{"evidence_id": "api526", "reference": "https://mediadive.dsmz.de/rest/medium/526",
    "raw_path": "REVIEW_WORK/batch064/source02-04/api526.bin", "raw_sha256": "01836967bf3384dfae78e42a3e14a300c515ed714676eb7eef7e856596a1ac89",
    "locator": "$.data.solutions[0].recipe[6]", "accessed_at": "2026-10-28T10:58:25.078229Z",
    "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\":
    \"L-Cysteine HCl x H2O\",\n                        \"compound_id\": 770,\n                        \"amount\":
    0.25,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.25,\n                        \"mmol_l\": 1.4234,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 7, "compound":
    "L-Cysteine HCl x H2O", "compound_id": 770, "amount": 0.25, "unit": "g", "g_l":
    0.25, "mmol_l": 1.4234, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, {"evidence_id":
    "dsm526", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium526.pdf",
    "raw_path": "REVIEW_WORK/batch064/source02-04/dsm526.bin", "raw_sha256": "970d6cccca0169339385018b2f55acaf2d3167714d213119d6b9f7d654090310",
    "locator": "PDF extracted line 9; visually checked page", "accessed_at": "2026-10-28T10:58:25.212182Z",
    "quote": "   L-Cysteine HCl x H2O                                        0.25         g"}],
    "decision": "evidence_only", "rationale": "The explicit current API main g_l equals
    this stored numerical rate and is credited as a provider assertion. The primary
    gives the source batch amount and 1000 mL input water, not a measured final makeup.
    API separately reports volume 1004 mL and does not consistently derive its g_l
    by dividing these masses by that volume; no convenient denominator is selected
    or new rate calculated.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.yaml",
    "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.25",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit current
    API main g_l equals this stored numerical rate and is credited as a provider assertion.
    The primary gives the source batch amount and 1000 mL input water, not a measured
    final makeup. API separately reports volume 1004 mL and does not consistently
    derive its g_l by dividing these masses by that volume; no convenient denominator
    is selected or new rate calculated."}, {"path": "data/normalized_yaml/bacterial/clostridium_viride_medium.yaml",
    "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.25",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The explicit current
    API main g_l equals this stored numerical rate and is credited as a provider assertion.
    The primary gives the source batch amount and 1000 mL input water, not a measured
    final makeup. API separately reports volume 1004 mL and does not consistently
    derive its g_l by dividing these masses by that volume; no convenient denominator
    is selected or new rate calculated."}]}, {"quantity_id": "q7", "topic": "Nitrilotriacetic
    acid stock stage", "source": [{"evidence_id": "api526", "reference": "https://mediadive.dsmz.de/rest/medium/526",
    "raw_path": "REVIEW_WORK/batch064/source02-04/api526.bin", "raw_sha256": "01836967bf3384dfae78e42a3e14a300c515ed714676eb7eef7e856596a1ac89",
    "locator": "$.data.solutions[1].recipe[0]", "accessed_at": "2026-10-28T10:58:25.078229Z",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"Nitrilotriacetic acid\",\n                        \"compound_id\": 189,\n                        \"attribute\":
    \"NTA\",\n                        \"amount\": 5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 5,\n                        \"mmol_l\":
    26.1588,\n                        \"optional\": 0\n                    }", "exact_decoded_object":
    {"recipe_order": 1, "compound": "Nitrilotriacetic acid", "compound_id": 189, "attribute":
    "NTA", "amount": 5, "unit": "g", "g_l": 5, "mmol_l": 26.1588, "optional": 0},
    "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}, {"evidence_id": "dsm526", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium526.pdf",
    "raw_path": "REVIEW_WORK/batch064/source02-04/dsm526.bin", "raw_sha256": "970d6cccca0169339385018b2f55acaf2d3167714d213119d6b9f7d654090310",
    "locator": "PDF extracted line 23; visually checked page", "accessed_at": "2026-10-28T10:58:25.212182Z",
    "quote": "   Nitrilotriacetic acid (NTA)                                 5.00         g"}],
    "decision": "correct", "rationale": "This explicit API g_l and primary amount
    belong to the separate Trace elements solution VR stock. The value is credited
    as stock strength but its direct main-medium placement is incorrect. Restore the
    stock composition and separate batch receiving dose; do not label these as final-medium
    concentrations.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.yaml",
    "field_path": "ingredients[6].concentration", "stored_value": {"value": "5", "unit":
    "G_PER_L"}, "decision": "correct", "rationale": "This explicit API g_l and primary
    amount belong to the separate Trace elements solution VR stock. The value is credited
    as stock strength but its direct main-medium placement is incorrect. Restore the
    stock composition and separate batch receiving dose; do not label these as final-medium
    concentrations."}, {"path": "data/normalized_yaml/bacterial/clostridium_viride_medium.yaml",
    "field_path": "ingredients[6].concentration", "stored_value": {"value": "5", "unit":
    "G_PER_L"}, "decision": "correct", "rationale": "This explicit API g_l and primary
    amount belong to the separate Trace elements solution VR stock. The value is credited
    as stock strength but its direct main-medium placement is incorrect. Restore the
    stock composition and separate batch receiving dose; do not label these as final-medium
    concentrations."}]}, {"quantity_id": "q8", "topic": "MgSO4 x 7 H2O stock stage",
    "source": [{"evidence_id": "api526", "reference": "https://mediadive.dsmz.de/rest/medium/526",
    "raw_path": "REVIEW_WORK/batch064/source02-04/api526.bin", "raw_sha256": "01836967bf3384dfae78e42a3e14a300c515ed714676eb7eef7e856596a1ac89",
    "locator": "$.data.solutions[1].recipe[1]", "accessed_at": "2026-10-28T10:58:25.078229Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\":
    24,\n                        \"unit\": \"g\",\n                        \"g_l\":
    24,\n                        \"mmol_l\": 97.3726,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound":
    "MgSO4 x 7 H2O", "compound_id": 8, "amount": 24, "unit": "g", "g_l": 24, "mmol_l":
    97.3726, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm526",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium526.pdf",
    "raw_path": "REVIEW_WORK/batch064/source02-04/dsm526.bin", "raw_sha256": "970d6cccca0169339385018b2f55acaf2d3167714d213119d6b9f7d654090310",
    "locator": "PDF extracted line 24; visually checked page", "accessed_at": "2026-10-28T10:58:25.212182Z",
    "quote": "   MgSO4 x 7 H2O                                              24.00         g"}],
    "decision": "correct", "rationale": "This explicit API g_l and primary amount
    belong to the separate Trace elements solution VR stock. The value is credited
    as stock strength but its direct main-medium placement is incorrect. Restore the
    stock composition and separate batch receiving dose; do not label these as final-medium
    concentrations.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.yaml",
    "field_path": "ingredients[7].concentration", "stored_value": {"value": "24",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This explicit API g_l
    and primary amount belong to the separate Trace elements solution VR stock. The
    value is credited as stock strength but its direct main-medium placement is incorrect.
    Restore the stock composition and separate batch receiving dose; do not label
    these as final-medium concentrations."}, {"path": "data/normalized_yaml/bacterial/clostridium_viride_medium.yaml",
    "field_path": "ingredients[7].concentration", "stored_value": {"value": "24",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This explicit API g_l
    and primary amount belong to the separate Trace elements solution VR stock. The
    value is credited as stock strength but its direct main-medium placement is incorrect.
    Restore the stock composition and separate batch receiving dose; do not label
    these as final-medium concentrations."}]}, {"quantity_id": "q9", "topic": "CaCl2
    x 2 H2O stock stage", "source": [{"evidence_id": "api526", "reference": "https://mediadive.dsmz.de/rest/medium/526",
    "raw_path": "REVIEW_WORK/batch064/source02-04/api526.bin", "raw_sha256": "01836967bf3384dfae78e42a3e14a300c515ed714676eb7eef7e856596a1ac89",
    "locator": "$.data.solutions[1].recipe[2]", "accessed_at": "2026-10-28T10:58:25.078229Z",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\":
    0.5,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.5,\n                        \"mmol_l\": 3.40101,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound":
    "CaCl2 x 2 H2O", "compound_id": 7, "amount": 0.5, "unit": "g", "g_l": 0.5, "mmol_l":
    3.40101, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm526",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium526.pdf",
    "raw_path": "REVIEW_WORK/batch064/source02-04/dsm526.bin", "raw_sha256": "970d6cccca0169339385018b2f55acaf2d3167714d213119d6b9f7d654090310",
    "locator": "PDF extracted line 25; visually checked page", "accessed_at": "2026-10-28T10:58:25.212182Z",
    "quote": "   CaCl2 x 2 H2O                                               0.50         g"}],
    "decision": "correct", "rationale": "This explicit API g_l and primary amount
    belong to the separate Trace elements solution VR stock. The value is credited
    as stock strength but its direct main-medium placement is incorrect. Restore the
    stock composition and separate batch receiving dose; do not label these as final-medium
    concentrations.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.yaml",
    "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.5",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This explicit API g_l
    and primary amount belong to the separate Trace elements solution VR stock. The
    value is credited as stock strength but its direct main-medium placement is incorrect.
    Restore the stock composition and separate batch receiving dose; do not label
    these as final-medium concentrations."}, {"path": "data/normalized_yaml/bacterial/clostridium_viride_medium.yaml",
    "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.5",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This explicit API g_l
    and primary amount belong to the separate Trace elements solution VR stock. The
    value is credited as stock strength but its direct main-medium placement is incorrect.
    Restore the stock composition and separate batch receiving dose; do not label
    these as final-medium concentrations."}]}, {"quantity_id": "q10", "topic": "FeSO4
    x 7 H2O stock stage", "source": [{"evidence_id": "api526", "reference": "https://mediadive.dsmz.de/rest/medium/526",
    "raw_path": "REVIEW_WORK/batch064/source02-04/api526.bin", "raw_sha256": "01836967bf3384dfae78e42a3e14a300c515ed714676eb7eef7e856596a1ac89",
    "locator": "$.data.solutions[1].recipe[3]", "accessed_at": "2026-10-28T10:58:25.078229Z",
    "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\":
    0.5,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.5,\n                        \"mmol_l\": 1.79846,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound":
    "FeSO4 x 7 H2O", "compound_id": 12, "amount": 0.5, "unit": "g", "g_l": 0.5, "mmol_l":
    1.79846, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm526",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium526.pdf",
    "raw_path": "REVIEW_WORK/batch064/source02-04/dsm526.bin", "raw_sha256": "970d6cccca0169339385018b2f55acaf2d3167714d213119d6b9f7d654090310",
    "locator": "PDF extracted line 26; visually checked page", "accessed_at": "2026-10-28T10:58:25.212182Z",
    "quote": "   FeSO4 x 7 H2O                                               0.50         g"}],
    "decision": "correct", "rationale": "This explicit API g_l and primary amount
    belong to the separate Trace elements solution VR stock. The value is credited
    as stock strength but its direct main-medium placement is incorrect. Restore the
    stock composition and separate batch receiving dose; do not label these as final-medium
    concentrations.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.yaml",
    "field_path": "ingredients[9].concentration", "stored_value": {"value": "0.5",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This explicit API g_l
    and primary amount belong to the separate Trace elements solution VR stock. The
    value is credited as stock strength but its direct main-medium placement is incorrect.
    Restore the stock composition and separate batch receiving dose; do not label
    these as final-medium concentrations."}, {"path": "data/normalized_yaml/bacterial/clostridium_viride_medium.yaml",
    "field_path": "ingredients[9].concentration", "stored_value": {"value": "0.5",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This explicit API g_l
    and primary amount belong to the separate Trace elements solution VR stock. The
    value is credited as stock strength but its direct main-medium placement is incorrect.
    Restore the stock composition and separate batch receiving dose; do not label
    these as final-medium concentrations."}]}, {"quantity_id": "q11", "topic": "NiCl2
    x 6 H2O stock stage", "source": [{"evidence_id": "api526", "reference": "https://mediadive.dsmz.de/rest/medium/526",
    "raw_path": "REVIEW_WORK/batch064/source02-04/api526.bin", "raw_sha256": "01836967bf3384dfae78e42a3e14a300c515ed714676eb7eef7e856596a1ac89",
    "locator": "$.data.solutions[1].recipe[4]", "accessed_at": "2026-10-28T10:58:25.078229Z",
    "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\":
    0.25,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.25,\n                        \"mmol_l\": 1.92903,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound":
    "NiCl2 x 6 H2O", "compound_id": 40, "amount": 0.25, "unit": "g", "g_l": 0.25,
    "mmol_l": 1.92903, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, {"evidence_id":
    "dsm526", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium526.pdf",
    "raw_path": "REVIEW_WORK/batch064/source02-04/dsm526.bin", "raw_sha256": "970d6cccca0169339385018b2f55acaf2d3167714d213119d6b9f7d654090310",
    "locator": "PDF extracted line 27; visually checked page", "accessed_at": "2026-10-28T10:58:25.212182Z",
    "quote": "   NiCl2 x 6 H2O                                               0.25         g"}],
    "decision": "correct", "rationale": "This explicit API g_l and primary amount
    belong to the separate Trace elements solution VR stock. The value is credited
    as stock strength but its direct main-medium placement is incorrect. Restore the
    stock composition and separate batch receiving dose; do not label these as final-medium
    concentrations.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.yaml",
    "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.25",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This explicit API g_l
    and primary amount belong to the separate Trace elements solution VR stock. The
    value is credited as stock strength but its direct main-medium placement is incorrect.
    Restore the stock composition and separate batch receiving dose; do not label
    these as final-medium concentrations."}, {"path": "data/normalized_yaml/bacterial/clostridium_viride_medium.yaml",
    "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.25",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This explicit API g_l
    and primary amount belong to the separate Trace elements solution VR stock. The
    value is credited as stock strength but its direct main-medium placement is incorrect.
    Restore the stock composition and separate batch receiving dose; do not label
    these as final-medium concentrations."}]}, {"quantity_id": "q12", "topic": "ZnSO4
    x 7 H2O stock stage", "source": [{"evidence_id": "api526", "reference": "https://mediadive.dsmz.de/rest/medium/526",
    "raw_path": "REVIEW_WORK/batch064/source02-04/api526.bin", "raw_sha256": "01836967bf3384dfae78e42a3e14a300c515ed714676eb7eef7e856596a1ac89",
    "locator": "$.data.solutions[1].recipe[5]", "accessed_at": "2026-10-28T10:58:25.078229Z",
    "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\":
    \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\":
    0.44,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.44,\n                        \"mmol_l\": 1.53011,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 6, "compound":
    "ZnSO4 x 7 H2O", "compound_id": 35, "amount": 0.44, "unit": "g", "g_l": 0.44,
    "mmol_l": 1.53011, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, {"evidence_id":
    "dsm526", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium526.pdf",
    "raw_path": "REVIEW_WORK/batch064/source02-04/dsm526.bin", "raw_sha256": "970d6cccca0169339385018b2f55acaf2d3167714d213119d6b9f7d654090310",
    "locator": "PDF extracted line 28; visually checked page", "accessed_at": "2026-10-28T10:58:25.212182Z",
    "quote": "   ZnSO4 x 7 H2O                                               0.44         g"}],
    "decision": "correct", "rationale": "This explicit API g_l and primary amount
    belong to the separate Trace elements solution VR stock. The value is credited
    as stock strength but its direct main-medium placement is incorrect. Restore the
    stock composition and separate batch receiving dose; do not label these as final-medium
    concentrations.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.yaml",
    "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.44",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This explicit API g_l
    and primary amount belong to the separate Trace elements solution VR stock. The
    value is credited as stock strength but its direct main-medium placement is incorrect.
    Restore the stock composition and separate batch receiving dose; do not label
    these as final-medium concentrations."}, {"path": "data/normalized_yaml/bacterial/clostridium_viride_medium.yaml",
    "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.44",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This explicit API g_l
    and primary amount belong to the separate Trace elements solution VR stock. The
    value is credited as stock strength but its direct main-medium placement is incorrect.
    Restore the stock composition and separate batch receiving dose; do not label
    these as final-medium concentrations."}]}, {"quantity_id": "q13", "topic": "MnSO4
    x H2O stock stage", "source": [{"evidence_id": "api526", "reference": "https://mediadive.dsmz.de/rest/medium/526",
    "raw_path": "REVIEW_WORK/batch064/source02-04/api526.bin", "raw_sha256": "01836967bf3384dfae78e42a3e14a300c515ed714676eb7eef7e856596a1ac89",
    "locator": "$.data.solutions[1].recipe[6]", "accessed_at": "2026-10-28T10:58:25.078229Z",
    "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\":
    \"MnSO4 x H2O\",\n                        \"compound_id\": 14,\n                        \"amount\":
    0.25,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.25,\n                        \"mmol_l\": 1.47915,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 7, "compound":
    "MnSO4 x H2O", "compound_id": 14, "amount": 0.25, "unit": "g", "g_l": 0.25, "mmol_l":
    1.47915, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm526",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium526.pdf",
    "raw_path": "REVIEW_WORK/batch064/source02-04/dsm526.bin", "raw_sha256": "970d6cccca0169339385018b2f55acaf2d3167714d213119d6b9f7d654090310",
    "locator": "PDF extracted line 29; visually checked page", "accessed_at": "2026-10-28T10:58:25.212182Z",
    "quote": "   MnSO4 x H2O                                                 0.25         g"}],
    "decision": "correct", "rationale": "This explicit API g_l and primary amount
    belong to the separate Trace elements solution VR stock. The value is credited
    as stock strength but its direct main-medium placement is incorrect. Restore the
    stock composition and separate batch receiving dose; do not label these as final-medium
    concentrations.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.yaml",
    "field_path": "ingredients[12].concentration", "stored_value": {"value": "0.25",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This explicit API g_l
    and primary amount belong to the separate Trace elements solution VR stock. The
    value is credited as stock strength but its direct main-medium placement is incorrect.
    Restore the stock composition and separate batch receiving dose; do not label
    these as final-medium concentrations."}, {"path": "data/normalized_yaml/bacterial/clostridium_viride_medium.yaml",
    "field_path": "ingredients[12].concentration", "stored_value": {"value": "0.25",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This explicit API g_l
    and primary amount belong to the separate Trace elements solution VR stock. The
    value is credited as stock strength but its direct main-medium placement is incorrect.
    Restore the stock composition and separate batch receiving dose; do not label
    these as final-medium concentrations."}]}, {"quantity_id": "q14", "topic": "CoCl2
    x 6 H2O stock stage", "source": [{"evidence_id": "api526", "reference": "https://mediadive.dsmz.de/rest/medium/526",
    "raw_path": "REVIEW_WORK/batch064/source02-04/api526.bin", "raw_sha256": "01836967bf3384dfae78e42a3e14a300c515ed714676eb7eef7e856596a1ac89",
    "locator": "$.data.solutions[1].recipe[7]", "accessed_at": "2026-10-28T10:58:25.078229Z",
    "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\":
    \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\":
    0.25,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.25,\n                        \"mmol_l\": 1.92546,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 8, "compound":
    "CoCl2 x 6 H2O", "compound_id": 38, "amount": 0.25, "unit": "g", "g_l": 0.25,
    "mmol_l": 1.92546, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, {"evidence_id":
    "dsm526", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium526.pdf",
    "raw_path": "REVIEW_WORK/batch064/source02-04/dsm526.bin", "raw_sha256": "970d6cccca0169339385018b2f55acaf2d3167714d213119d6b9f7d654090310",
    "locator": "PDF extracted line 30; visually checked page", "accessed_at": "2026-10-28T10:58:25.212182Z",
    "quote": "   CoCl2 x 6 H2O                                               0.25         g"}],
    "decision": "correct", "rationale": "This explicit API g_l and primary amount
    belong to the separate Trace elements solution VR stock. The value is credited
    as stock strength but its direct main-medium placement is incorrect. Restore the
    stock composition and separate batch receiving dose; do not label these as final-medium
    concentrations.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.yaml",
    "field_path": "ingredients[13].concentration", "stored_value": {"value": "0.25",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This explicit API g_l
    and primary amount belong to the separate Trace elements solution VR stock. The
    value is credited as stock strength but its direct main-medium placement is incorrect.
    Restore the stock composition and separate batch receiving dose; do not label
    these as final-medium concentrations."}, {"path": "data/normalized_yaml/bacterial/clostridium_viride_medium.yaml",
    "field_path": "ingredients[13].concentration", "stored_value": {"value": "0.25",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This explicit API g_l
    and primary amount belong to the separate Trace elements solution VR stock. The
    value is credited as stock strength but its direct main-medium placement is incorrect.
    Restore the stock composition and separate batch receiving dose; do not label
    these as final-medium concentrations."}]}, {"quantity_id": "q15", "topic": "VOSO4
    x 5 H2O stock stage", "source": [{"evidence_id": "api526", "reference": "https://mediadive.dsmz.de/rest/medium/526",
    "raw_path": "REVIEW_WORK/batch064/source02-04/api526.bin", "raw_sha256": "01836967bf3384dfae78e42a3e14a300c515ed714676eb7eef7e856596a1ac89",
    "locator": "$.data.solutions[1].recipe[8]", "accessed_at": "2026-10-28T10:58:25.078229Z",
    "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\":
    \"VOSO4 x 5 H2O\",\n                        \"compound_id\": 277,\n                        \"amount\":
    0.25,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.25,\n                        \"mmol_l\": 0.987826,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 9, "compound":
    "VOSO4 x 5 H2O", "compound_id": 277, "amount": 0.25, "unit": "g", "g_l": 0.25,
    "mmol_l": 0.987826, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, {"evidence_id":
    "dsm526", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium526.pdf",
    "raw_path": "REVIEW_WORK/batch064/source02-04/dsm526.bin", "raw_sha256": "970d6cccca0169339385018b2f55acaf2d3167714d213119d6b9f7d654090310",
    "locator": "PDF extracted line 31; visually checked page", "accessed_at": "2026-10-28T10:58:25.212182Z",
    "quote": "   VOSO4 x 5 H2O                                               0.25         g"}],
    "decision": "correct", "rationale": "This explicit API g_l and primary amount
    belong to the separate Trace elements solution VR stock. The value is credited
    as stock strength but its direct main-medium placement is incorrect. Restore the
    stock composition and separate batch receiving dose; do not label these as final-medium
    concentrations.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.yaml",
    "field_path": "ingredients[14].concentration", "stored_value": {"value": "0.25",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This explicit API g_l
    and primary amount belong to the separate Trace elements solution VR stock. The
    value is credited as stock strength but its direct main-medium placement is incorrect.
    Restore the stock composition and separate batch receiving dose; do not label
    these as final-medium concentrations."}, {"path": "data/normalized_yaml/bacterial/clostridium_viride_medium.yaml",
    "field_path": "ingredients[14].concentration", "stored_value": {"value": "0.25",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This explicit API g_l
    and primary amount belong to the separate Trace elements solution VR stock. The
    value is credited as stock strength but its direct main-medium placement is incorrect.
    Restore the stock composition and separate batch receiving dose; do not label
    these as final-medium concentrations."}]}, {"quantity_id": "q16", "topic": "Na2MoO4
    x 2 H2O stock stage", "source": [{"evidence_id": "api526", "reference": "https://mediadive.dsmz.de/rest/medium/526",
    "raw_path": "REVIEW_WORK/batch064/source02-04/api526.bin", "raw_sha256": "01836967bf3384dfae78e42a3e14a300c515ed714676eb7eef7e856596a1ac89",
    "locator": "$.data.solutions[1].recipe[9]", "accessed_at": "2026-10-28T10:58:25.078229Z",
    "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\":
    \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\":
    0.25,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.25,\n                        \"mmol_l\": 1.03327,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 10, "compound":
    "Na2MoO4 x 2 H2O", "compound_id": 9, "amount": 0.25, "unit": "g", "g_l": 0.25,
    "mmol_l": 1.03327, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, {"evidence_id":
    "dsm526", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium526.pdf",
    "raw_path": "REVIEW_WORK/batch064/source02-04/dsm526.bin", "raw_sha256": "970d6cccca0169339385018b2f55acaf2d3167714d213119d6b9f7d654090310",
    "locator": "PDF extracted line 32; visually checked page", "accessed_at": "2026-10-28T10:58:25.212182Z",
    "quote": "   Na2MoO4 x 2 H2O                                             0.25         g"}],
    "decision": "correct", "rationale": "This explicit API g_l and primary amount
    belong to the separate Trace elements solution VR stock. The value is credited
    as stock strength but its direct main-medium placement is incorrect. Restore the
    stock composition and separate batch receiving dose; do not label these as final-medium
    concentrations.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.yaml",
    "field_path": "ingredients[15].concentration", "stored_value": {"value": "0.25",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This explicit API g_l
    and primary amount belong to the separate Trace elements solution VR stock. The
    value is credited as stock strength but its direct main-medium placement is incorrect.
    Restore the stock composition and separate batch receiving dose; do not label
    these as final-medium concentrations."}, {"path": "data/normalized_yaml/bacterial/clostridium_viride_medium.yaml",
    "field_path": "ingredients[15].concentration", "stored_value": {"value": "0.25",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This explicit API g_l
    and primary amount belong to the separate Trace elements solution VR stock. The
    value is credited as stock strength but its direct main-medium placement is incorrect.
    Restore the stock composition and separate batch receiving dose; do not label
    these as final-medium concentrations."}]}, {"quantity_id": "q17", "topic": "CuSO4
    x 5 H2O stock stage", "source": [{"evidence_id": "api526", "reference": "https://mediadive.dsmz.de/rest/medium/526",
    "raw_path": "REVIEW_WORK/batch064/source02-04/api526.bin", "raw_sha256": "01836967bf3384dfae78e42a3e14a300c515ed714676eb7eef7e856596a1ac89",
    "locator": "$.data.solutions[1].recipe[10]", "accessed_at": "2026-10-28T10:58:25.078229Z",
    "quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\":
    \"CuSO4 x 5 H2O\",\n                        \"compound_id\": 121,\n                        \"amount\":
    0.12,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.12,\n                        \"mmol_l\": 0.480604,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 11, "compound":
    "CuSO4 x 5 H2O", "compound_id": 121, "amount": 0.12, "unit": "g", "g_l": 0.12,
    "mmol_l": 0.480604, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, {"evidence_id":
    "dsm526", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium526.pdf",
    "raw_path": "REVIEW_WORK/batch064/source02-04/dsm526.bin", "raw_sha256": "970d6cccca0169339385018b2f55acaf2d3167714d213119d6b9f7d654090310",
    "locator": "PDF extracted line 33; visually checked page", "accessed_at": "2026-10-28T10:58:25.212182Z",
    "quote": "   CuSO4 x 5 H2O                                               0.12         g"}],
    "decision": "correct", "rationale": "This explicit API g_l and primary amount
    belong to the separate Trace elements solution VR stock. The value is credited
    as stock strength but its direct main-medium placement is incorrect. Restore the
    stock composition and separate batch receiving dose; do not label these as final-medium
    concentrations.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.yaml",
    "field_path": "ingredients[16].concentration", "stored_value": {"value": "0.12",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This explicit API g_l
    and primary amount belong to the separate Trace elements solution VR stock. The
    value is credited as stock strength but its direct main-medium placement is incorrect.
    Restore the stock composition and separate batch receiving dose; do not label
    these as final-medium concentrations."}, {"path": "data/normalized_yaml/bacterial/clostridium_viride_medium.yaml",
    "field_path": "ingredients[16].concentration", "stored_value": {"value": "0.12",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This explicit API g_l
    and primary amount belong to the separate Trace elements solution VR stock. The
    value is credited as stock strength but its direct main-medium placement is incorrect.
    Restore the stock composition and separate batch receiving dose; do not label
    these as final-medium concentrations."}]}, {"quantity_id": "q18", "topic": "VR
    stock receiving dose", "source": [{"evidence_id": "api526", "reference": "https://mediadive.dsmz.de/rest/medium/526",
    "raw_path": "REVIEW_WORK/batch064/source02-04/api526.bin", "raw_sha256": "01836967bf3384dfae78e42a3e14a300c515ed714676eb7eef7e856596a1ac89",
    "locator": "$.data.solutions[0].recipe[3]", "accessed_at": "2026-10-28T10:58:25.078229Z",
    "quote": "{\n                        \"recipe_order\": 4,\n                        \"solution\":
    \"Trace elements solution VR\",\n                        \"solution_id\": 1163,\n                        \"amount\":
    4,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 4, "solution":
    "Trace elements solution VR", "solution_id": 1163, "amount": 4, "unit": "ml",
    "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}, {"evidence_id": "dsm526", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium526.pdf", "raw_path":
    "REVIEW_WORK/batch064/source02-04/dsm526.bin", "raw_sha256": "970d6cccca0169339385018b2f55acaf2d3167714d213119d6b9f7d654090310",
    "locator": "PDF extracted line 6; visually checked page", "accessed_at": "2026-10-28T10:58:25.212182Z",
    "quote": "   Trace elements solution VR                                  4.00        ml"}],
    "decision": "add", "rationale": "Both sources explicitly add 4 mL of the separate
    VR stock to the stated recipe. Restore this missing relationship/dose in recipe-batch
    context. The 1000 mL water input does not itself justify an unqualified final-liter
    dose.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Both sources explicitly add 4 mL of the separate VR stock to the stated recipe.
    Restore this missing relationship/dose in recipe-batch context. The 1000 mL water
    input does not itself justify an unqualified final-liter dose.", "missing": true},
    {"path": "data/normalized_yaml/bacterial/clostridium_viride_medium.yaml", "field_path":
    "solutions", "stored_value": null, "decision": "add", "rationale": "Both sources
    explicitly add 4 mL of the separate VR stock to the stated recipe. Restore this
    missing relationship/dose in recipe-batch context. The 1000 mL water input does
    not itself justify an unqualified final-liter dose.", "missing": true}]}, {"quantity_id":
    "q19", "topic": "Indicator stock dose and strength", "source": [{"evidence_id":
    "api526", "reference": "https://mediadive.dsmz.de/rest/medium/526", "raw_path":
    "REVIEW_WORK/batch064/source02-04/api526.bin", "raw_sha256": "01836967bf3384dfae78e42a3e14a300c515ed714676eb7eef7e856596a1ac89",
    "locator": "$.data.solutions[0].recipe[4]", "accessed_at": "2026-10-28T10:58:25.078229Z",
    "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\":
    \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\":
    \"ml\",\n                        \"g_l\": 0.0005,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound":
    "Sodium resazurin", "compound_id": 1852, "attribute": "0.1% w/v", "amount": 0.5,
    "unit": "ml", "g_l": 0.0005, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, {"evidence_id":
    "dsm526", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium526.pdf",
    "raw_path": "REVIEW_WORK/batch064/source02-04/dsm526.bin", "raw_sha256": "970d6cccca0169339385018b2f55acaf2d3167714d213119d6b9f7d654090310",
    "locator": "PDF extracted line 7; visually checked page", "accessed_at": "2026-10-28T10:58:25.212182Z",
    "quote": "   Sodium resazurin (0.1% w/v)                                 0.50        ml"}],
    "decision": "evidence_only", "rationale": "The source explicitly supplies 0.5
    mL of 0.1% w/v sodium-resazurin solution. This is 0.5 mg per batch, consistent
    with the provider nominal amount. Retain supplied form, stock attributes and batch
    context; the existing numerical mass rate does not document the physical stock
    addition.", "layer_assessments": []}, {"quantity_id": "q20", "topic": "Scoped
    source water input — Main sol. 526", "source": [{"evidence_id": "api526", "reference":
    "https://mediadive.dsmz.de/rest/medium/526", "raw_path": "REVIEW_WORK/batch064/source02-04/api526.bin",
    "raw_sha256": "01836967bf3384dfae78e42a3e14a300c515ed714676eb7eef7e856596a1ac89",
    "locator": "$.data.solutions[0].recipe[7]", "accessed_at": "2026-10-28T10:58:25.078229Z",
    "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    1000,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 8, "compound":
    "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional":
    0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}], "decision": "evidence_only", "rationale": "Source
    solvent input only; no measured final-volume or new ingredient-rate assertion.",
    "layer_assessments": []}, {"quantity_id": "q21", "topic": "Scoped source water
    input — Trace elements solution VR", "source": [{"evidence_id": "api526", "reference":
    "https://mediadive.dsmz.de/rest/medium/526", "raw_path": "REVIEW_WORK/batch064/source02-04/api526.bin",
    "raw_sha256": "01836967bf3384dfae78e42a3e14a300c515ed714676eb7eef7e856596a1ac89",
    "locator": "$.data.solutions[1].recipe[11]", "accessed_at": "2026-10-28T10:58:25.078229Z",
    "quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    1000,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 12, "compound":
    "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional":
    0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}], "decision": "evidence_only", "rationale": "Source
    solvent input only; no measured final-volume or new ingredient-rate assertion.",
    "layer_assessments": []}, {"quantity_id": "q22", "topic": "Existing final pH range",
    "source": [{"evidence_id": "dsm526", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium526.pdf",
    "raw_path": "REVIEW_WORK/batch064/source02-04/dsm526.bin", "raw_sha256": "970d6cccca0169339385018b2f55acaf2d3167714d213119d6b9f7d654090310",
    "locator": "Exact visually checked PDF section", "accessed_at": "2026-10-28T10:58:25.212182Z",
    "quote": "After autoclaving adjust pH of medium\nto 7.6 - 7.8 using a sterile
    anoxic stock solution of Na2CO3 (5% w/v) prepared under 80% N\n2 and 20% CO2 gas
    atmosphere."}], "decision": "evidence_only", "rationale": "Existing final pH range
    7.6–7.8 agrees with the source. Initial pH 7.0 belongs to a different preparation
    stage. Preserve both stages and their exact evidence without treating titrant
    strength as a dose.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.yaml",
    "field_path": "ph_range", "stored_value": {"min": 7.6, "max": 7.8}, "decision":
    "evidence_only", "rationale": "Existing final pH range 7.6–7.8 agrees with the
    source. Initial pH 7.0 belongs to a different preparation stage. Preserve both
    stages and their exact evidence without treating titrant strength as a dose."},
    {"path": "data/normalized_yaml/bacterial/clostridium_viride_medium.yaml", "field_path":
    "ph_range", "stored_value": {"min": 7.6, "max": 7.8}, "decision": "evidence_only",
    "rationale": "Existing final pH range 7.6–7.8 agrees with the source. Initial
    pH 7.0 belongs to a different preparation stage. Preserve both stages and their
    exact evidence without treating titrant strength as a dose."}]}, {"quantity_id":
    "q23", "topic": "Existing main process and unquantified titrant dose", "source":
    [{"evidence_id": "api526", "reference": "https://mediadive.dsmz.de/rest/medium/526",
    "raw_path": "REVIEW_WORK/batch064/source02-04/api526.bin", "raw_sha256": "01836967bf3384dfae78e42a3e14a300c515ed714676eb7eef7e856596a1ac89",
    "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T10:58:25.078229Z",
    "quote": "{\n                        \"step\": \"Dissolve ingredients (except
    bicarbonate and cysteine), adjust pH to 7.0 with NaOH and sparge medium with 80%
    N2 and 20% CO2 gas mixture for 30 - 45 min. Add and dissolve solid bicarbonate
    and cysteine, dispense medium under same gas atmosphere into anoxic Hungate-type
    tubes or serum vials and autoclave. After autoclaving adjust pH of medium to 7.6
    - 7.8 using a sterile anoxic stock solution of Na2CO3 (5% w/v) prepared under
    80% N2 and 20% CO2 gas atmosphere.\"\n                    }", "exact_decoded_object":
    {"step": "Dissolve ingredients (except bicarbonate and cysteine), adjust pH to
    7.0 with NaOH and sparge medium with 80% N2 and 20% CO2 gas mixture for 30 - 45
    min. Add and dissolve solid bicarbonate and cysteine, dispense medium under same
    gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. After
    autoclaving adjust pH of medium to 7.6 - 7.8 using a sterile anoxic stock solution
    of Na2CO3 (5% w/v) prepared under 80% N2 and 20% CO2 gas atmosphere."}, "quote_basis":
    "Literal UTF-8 raw-response substring; decoded object independently equals exact
    JSON locator."}, {"evidence_id": "dsm526", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium526.pdf",
    "raw_path": "REVIEW_WORK/batch064/source02-04/dsm526.bin", "raw_sha256": "970d6cccca0169339385018b2f55acaf2d3167714d213119d6b9f7d654090310",
    "locator": "Exact visually checked PDF section", "accessed_at": "2026-10-28T10:58:25.212182Z",
    "quote": "Dissolve ingredients (except bicarbonate and cysteine), adjust pH to
    7.0 with NaOH and\nsparge medium with 80% N2 and 20% CO2 gas mixture for 30 -
    45 min. Add and dissolve\nsolid bicarbonate and cysteine, dispense medium under
    same gas atmosphere into anoxic\nHungate-type tubes or serum vials and autoclave.
    After autoclaving adjust pH of medium\nto 7.6 - 7.8 using a sterile anoxic stock
    solution of Na2CO3 (5% w/v) prepared under 80% N\n2 and 20% CO2 gas atmosphere."}],
    "decision": "evidence_only", "rationale": "Existing main preparation accurately
    preserves initial pH 7.0, 80/20 gas, 30–45 minutes, addition order, autoclaving
    and final pH 7.6–7.8 using 5% w/v carbonate stock. No carbonate dose is printed,
    so it must not become a quantified or variable main ingredient. This is source
    preparation, not organism-specific growth evidence.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.yaml", "field_path": "preparation_steps[0].description",
    "stored_value": "Dissolve ingredients (except bicarbonate and cysteine), adjust
    pH to 7.0 with NaOH and sparge medium with 80% N2 and 20% CO2 gas mixture for
    30 - 45 min. Add and dissolve solid bicarbonate and cysteine, dispense medium
    under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave.
    After autoclaving adjust pH of medium to 7.6 - 7.8 using a sterile anoxic stock
    solution of Na2CO3 (5% w/v) prepared under 80% N2 and 20% CO2 gas atmosphere.",
    "decision": "evidence_only", "rationale": "Existing main preparation accurately
    preserves initial pH 7.0, 80/20 gas, 30–45 minutes, addition order, autoclaving
    and final pH 7.6–7.8 using 5% w/v carbonate stock. No carbonate dose is printed,
    so it must not become a quantified or variable main ingredient. This is source
    preparation, not organism-specific growth evidence."}, {"path": "data/normalized_yaml/bacterial/clostridium_viride_medium.yaml",
    "field_path": "preparation_steps[0].description", "stored_value": "Dissolve ingredients
    (except bicarbonate and cysteine), adjust pH to 7.0 with NaOH and sparge medium
    with 80% N2 and 20% CO2 gas mixture for 30 - 45 min. Add and dissolve solid bicarbonate
    and cysteine, dispense medium under same gas atmosphere into anoxic Hungate-type
    tubes or serum vials and autoclave. After autoclaving adjust pH of medium to 7.6
    - 7.8 using a sterile anoxic stock solution of Na2CO3 (5% w/v) prepared under
    80% N2 and 20% CO2 gas atmosphere.", "decision": "evidence_only", "rationale":
    "Existing main preparation accurately preserves initial pH 7.0, 80/20 gas, 30–45
    minutes, addition order, autoclaving and final pH 7.6–7.8 using 5% w/v carbonate
    stock. No carbonate dose is printed, so it must not become a quantified or variable
    main ingredient. This is source preparation, not organism-specific growth evidence."}]},
    {"quantity_id": "q24", "topic": "Existing VR stock process and numerical fields",
    "source": [{"evidence_id": "api526", "reference": "https://mediadive.dsmz.de/rest/medium/526",
    "raw_path": "REVIEW_WORK/batch064/source02-04/api526.bin", "raw_sha256": "01836967bf3384dfae78e42a3e14a300c515ed714676eb7eef7e856596a1ac89",
    "locator": "$.data.solutions[1].steps[0]", "accessed_at": "2026-10-28T10:58:25.078229Z",
    "quote": "{\n                        \"step\": \"Dissolve mineral salts in 700
    ml water acidified with 2 ml of conc. HCl. Separately dissolve 5.00 g of NTA in
    300 ml water add 10 N NaOH until all the NTA has dissolved and the pH is 7.0.
    While stirring, slowly add the NTA solution to the salt solution. Stir until the
    solution is almost clear. Store cool and dark.\"\n                    }", "exact_decoded_object":
    {"step": "Dissolve mineral salts in 700 ml water acidified with 2 ml of conc.
    HCl. Separately dissolve 5.00 g of NTA in 300 ml water add 10 N NaOH until all
    the NTA has dissolved and the pH is 7.0. While stirring, slowly add the NTA solution
    to the salt solution. Stir until the solution is almost clear. Store cool and
    dark."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object
    independently equals exact JSON locator."}, {"evidence_id": "dsm526", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium526.pdf", "raw_path":
    "REVIEW_WORK/batch064/source02-04/dsm526.bin", "raw_sha256": "970d6cccca0169339385018b2f55acaf2d3167714d213119d6b9f7d654090310",
    "locator": "Exact visually checked PDF section", "accessed_at": "2026-10-28T10:58:25.212182Z",
    "quote": "Dissolve mineral salts in 700 ml water acidified with 2 ml of conc.
    HCl. Separately dissolve\n5.00 g of NTA in 300 ml water add 10 N NaOH until all
    the NTA has dissolved and the pH is\n7.0. While stirring, slowly add the NTA solution
    to the salt solution. Stir until the solution is\nalmost clear. Store cool and
    dark."}], "decision": "evidence_only", "rationale": "The exact stock process is
    already present: 700 mL salt water plus 2 mL concentrated HCl, separately 5 g
    NTA in 300 mL water, 10 N NaOH to pH 7.0, combination and cool/dark storage. Preserve
    this text at the VR stock stage. Concentrated HCl strength and NaOH dose are unspecified;
    input sums plus titrants do not prove a final stock volume.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_VIRIDE_MEDIUM.yaml", "field_path":
    "preparation_steps[1].description", "stored_value": "Dissolve mineral salts in
    700 ml water acidified with 2 ml of conc. HCl. Separately dissolve 5.00 g of NTA
    in 300 ml water add 10 N NaOH until all the NTA has dissolved and the pH is 7.0.
    While stirring, slowly add the NTA solution to the salt solution. Stir until the
    solution is almost clear. Store cool and dark.", "decision": "evidence_only",
    "rationale": "The exact stock process is already present: 700 mL salt water plus
    2 mL concentrated HCl, separately 5 g NTA in 300 mL water, 10 N NaOH to pH 7.0,
    combination and cool/dark storage. Preserve this text at the VR stock stage. Concentrated
    HCl strength and NaOH dose are unspecified; input sums plus titrants do not prove
    a final stock volume."}, {"path": "data/normalized_yaml/bacterial/clostridium_viride_medium.yaml",
    "field_path": "preparation_steps[1].description", "stored_value": "Dissolve mineral
    salts in 700 ml water acidified with 2 ml of conc. HCl. Separately dissolve 5.00
    g of NTA in 300 ml water add 10 N NaOH until all the NTA has dissolved and the
    pH is 7.0. While stirring, slowly add the NTA solution to the salt solution. Stir
    until the solution is almost clear. Store cool and dark.", "decision": "evidence_only",
    "rationale": "The exact stock process is already present: 700 mL salt water plus
    2 mL concentrated HCl, separately 5 g NTA in 300 mL water, 10 N NaOH to pH 7.0,
    combination and cool/dark storage. Preserve this text at the VR stock stage. Concentrated
    HCl strength and NaOH dose are unspecified; input sums plus titrants do not prove
    a final stock volume."}]}]'
- assessment_id: a4
  area: grounding
  topic: Current ontology and MIM correspondence
  outcome: concern
  summary: Every current ontology/MIM slot was checked against raw OLS and exact packaged
    rows. Sodium salt versus neutral dye and nickel hexahydrate versus anhydrous chloride
    are confirmed mismatches. Other listed hydrates retain their source forms; current
    preferred-row REJECTED status is preserved as catalog metadata, not a claim that
    the matching accession is invalid.
  target_ids:
  - CultureMech:001657
  evidence_ids:
  - grounding
- assessment_id: a5
  area: provenance
  topic: History and evidence scope
  outcome: concern
  summary: Complete selected histories, three exact concentration reports and scoped
    plan row were read, plus the full September report only as comparison context.
    The current API digest and 22 raw literal objects match historical bytes. Old
    retrieval times and broad recommendations are not reauthenticated; missing direct
    claim evidence remains unresolved.
  target_ids:
  - CultureMech:001657
  evidence_ids:
  - history
  - scalars
- assessment_id: a6
  area: scope
  topic: Growth and taxonomic evidence
  outcome: unknown
  summary: Generic cultivation applications and bacterial filing are not strain-level
    growth evidence. No organism-specific growth, temperature or atmosphere is inferred
    from names or source catalog identifiers.
  target_ids:
  - CultureMech:001657
  evidence_ids:
  - local-target
- assessment_id: a7
  area: schema
  topic: Canonical diagnostics
  outcome: supported
  summary: All four original canonical diagnostics passed. Reference checks were zero;
    structural and term diagnostics do not establish formulation accuracy.
  target_ids:
  - CultureMech:001657
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-001657-restore-the-vr-trace-stock-stage-and-dose
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Restore the VR trace-stock stage and dose
  description: Eleven trace-stock ingredients are published as direct main-medium
    components at their stock strengths. The source instead defines the separate VR
    solution and adds4 mL per stated recipe batch. Its preparation is already present
    as root step 2 but lacks the stock context. Six explicit provider main g_l values
    remain credited, without resolving conflicting volume metadata by assumption.
  target_ids:
  - CultureMech:001657
  field_paths:
  - ingredients
  - solutions
  - preparation_steps[1].description
  evidence_ids:
  - dsm526
  - api526
  - quantities
  - writer-mediadive
  - writer-merge
  - writer-formulation
  rule_id: custom-source-stock-stage
  native_severity: P2
  normalization_reason: 'Major: full stock strengths are assigned to the receiving-medium
    ingredient list and the stock dose is absent. This custom source-stage rule does
    not assert invalid ontology accessions or a measured final volume.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_viride_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f2
  issue_key: culturemech-001657-reconcile-sodium-resazurin-and-nickel-hydrate-forms
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Reconcile sodium-resazurin and nickel hydrate forms
  description: Ingredient 3 names sodium resazurin but CHEBI:8806 denotes neutral
    resazurin. Ingredient 10 names nickel chloride hexahydrate but CHEBI:34887 denotes
    anhydrous nickel dichloride; current CHEBI:53542 explicitly denotes the hexahydrate.
    Supported amounts and their source stages remain unchanged by this identifier
    assessment.
  target_ids:
  - CultureMech:001657
  field_paths:
  - ingredients[3].term
  - ingredients[10].term
  evidence_ids:
  - dsm526
  - api526
  - chebi8806
  - chebi34887
  - chebi53542
  - grounding
  rule_id: custom-supplied-form-correspondence
  native_severity: P2
  normalization_reason: 'Major: valid resolvable identifiers describe different supplied
    chemical forms. Native P2.2 invalid-CHEBI is not invoked; the mismatch is source-form
    correspondence.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_viride_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f3
  issue_key: culturemech-001657-link-existing-supported-claims-and-preserve-historical-scope
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Link existing supported claims and preserve historical scope
  description: Neither local layer provides claim-level evidence for its amounts,
    pH and preparation. The current response exactly authenticates 22 historical literal
    objects and the old response digest, but not the old access event or every historical
    interpretation. The September comparison report describes a different selected
    record; its per-final-liter assumption and absent-preparation conclusions are
    not adopted here.
  target_ids:
  - CultureMech:001657
  field_paths:
  - evidence
  - references
  - curation_history
  evidence_ids:
  - history
  - historical-reader
  - historical-plan-rows
  - dsm526
  - api526
  rule_id: custom-claim-linkage-and-history-scope
  native_severity: P3
  normalization_reason: 'Minor: missing linkage and derivative-report scope limit
    traceability without establishing an additional source recipe error. Native P4.4
    is inapplicable to the multi-event history.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_viride_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
actions:
- action_id: action1
  description: In the maintained owner, restore the exact VR stock composition and
    separate 4 mL recipe-batch addition, removing the eleven misplaced stock-only
    main ingredients. Retain the supported main numerical values with provider/primary
    basis clearly separated, and retain existing stock preparation at its proper stage
    before regeneration.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:001657
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_viride_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action2
  description: Verify the exact sodium-salt identifier or retain its grounding explicitly
    unresolved; reconcile nickel with the independently verified hexahydrate term
    and current mapping evidence. Preserve the supported source amounts and stock
    stages, and never substitute anhydrous masses or invent a salt accession.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:001657
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_viride_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action3
  description: Add exact root evidence linking supported ingredient, stock, pH and
    preparation claims to the current source and its stage. Preserve original events
    byte-for-byte; append new verified context rather than rewriting history. Keep
    the comparison-only report explicitly scoped and do not copy its unrelated defects
    into this record.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:001657
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_viride_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
limitations:
- Primary water quantities are inputs rather than explicit final-makeup instructions.
  API main volume 1004 mL and its declared g_l are retained as separate provider facts,
  without silently recalculating rates or claiming measured final concentrations.
- The source does not quantify the final carbonate-stock dose, NaOH titration volume
  or concentration of concentrated HCl. None is inferred from typical practice or
  summed solvent inputs.
- The historical aminovalericum/KOMODO report is outside selected ownership. Its missing
  preparation, extra carbonate and aerobic/identity findings are not transferred to
  this already documented DSM owner.
- No strain-level growth, taxonomic assignment or culture performance is inferred
  from the recipe name or generic application. Current ontology/catalog/code facts
  are not proof of historical validity or execution.
notes:
- Fresh review; historical lost snapshots were not reconstructed. All inspected source
  files remain unchanged.
- No formal review validation/save, Git mutation or publication was performed by this
  author.
```
