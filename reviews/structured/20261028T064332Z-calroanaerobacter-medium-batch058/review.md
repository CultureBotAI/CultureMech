# Calroanaerobacter medium: batch quantities and nested stock scope

- Review: 20261028T064332Z-calroanaerobacter-medium-batch058
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T06:07:45.569258Z
- Finished UTC: 2026-10-28T06:43:32.084231Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

TOGO M1107/JCM1042 identity and four native checks are supported. Three major findings concern quantity dimensions/bases, stock stages and missing preparation; one minor finding concerns claim provenance. Exact primary JCM1042 recipe remains unavailable; primary stock definitions and current database recipe are inspected.

## Scope And Provenance

One entire selected generated record and sole maintained owner;40 local concentration fields,45 scoped TOGO items and43 corroborating API recipe rows; exact existing chemical IDs, history and current writer. Separate MediaDive counterpart and solution5101 are limited comparison context.

Selection: Batch058 item10; Python-sorted uncovered paths from successful native lists; covered503 of6325 at selection; base9ea7ff33d354e37b791df96a880005153e446ce3.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:007626 | data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml | generated | CALROANAEROBACTER MEDIUM |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:007626 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:007626 | Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                REVIEW_WORK/batch058/record10/strict.tsv |
| validate-terms | passed | True | CultureMech:007626 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:007626 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| Manual embedded history assessment | passed | False | CultureMech:007626 | All embedded history read. June primary heptahydrate and nine secondary-link repairs are credited; no timestamps repaired or events appended. Standalone history-tree validator does not validate these embedded entries. |

## Scientific And Domain Assessments

### Exact source and maintained ownership

identity: supported. Targets: CultureMech:007626.

Selected CM007626 is the TOGO M1107/JCM1042 medium; sole owner and current database cross-reference are supported.

The source spelling Calroanaerobacter is retained without inferring taxonomy or growth. The similarly named CM002227 and solution5101 are context only. No DOI, PMID, strain accession or target-organism claim is asserted by the selected record. iModulonDB is not applicable to this medium formulation.

### All existing quantities and referenced recipe rows

evidence: concern. Targets: CultureMech:007626.

40 local fields assessed:8 unsupported rate denominators and32 conflicts;45 scoped TOGO rows and43 MediaDive recipe rows retained.

{"existing_field_count": 40, "counts": {"unsupported": 8, "conflict": 32}, "record_field_counts": {"data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml": 20, "data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml": 20}, "quantities": [{"record_path": "data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "ingredient": "Sodium pyruvate", "existing": {"value": "5", "unit": "G_PER_L"}, "decision": "unsupported", "source_evidence": ["togo1107-api-q-0-0"], "source_locator": "$.components[0].items[0]", "source_row": {"component_name": "Sodium pyruvate", "volume": 5, "unit": "g", "gmo_id": "GMO_001055"}, "source_stage": "main solution 1", "explanation": "Source mass matches the local number, but it is an amount in the listed main batch. One litre of seawater plus5 ml vitamins does not establish a final litre. G_PER_L denominator is unverified; preserve mass and batch context.", "calculation": "none; no final-volume assumption", "proposed_amount": "none asserted"}, {"record_path": "data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "ingredient": "PIPES", "existing": {"value": "3.46", "unit": "G_PER_L"}, "decision": "unsupported", "source_evidence": ["togo1107-api-q-0-1"], "source_locator": "$.components[0].items[1]", "source_row": {"component_name": "PIPES", "volume": 3.46, "unit": "g", "gmo_id": "GMO_001223"}, "source_stage": "main solution 1", "explanation": "Source mass matches the local number, but it is an amount in the listed main batch. One litre of seawater plus5 ml vitamins does not establish a final litre. G_PER_L denominator is unverified; preserve mass and batch context.", "calculation": "none; no final-volume assumption", "proposed_amount": "none asserted"}, {"record_path": "data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "ingredient": "Yeast extract (BD-Difco)", "existing": {"value": "2", "unit": "G_PER_L"}, "decision": "unsupported", "source_evidence": ["togo1107-api-q-0-2"], "source_locator": "$.components[0].items[2]", "source_row": {"component_name": "Yeast extract (BD-Difco)", "volume": 2, "unit": "g", "gmo_id": "GMO_001018"}, "source_stage": "main solution 1", "explanation": "Source mass matches the local number, but it is an amount in the listed main batch. One litre of seawater plus5 ml vitamins does not establish a final litre. G_PER_L denominator is unverified; preserve mass and batch context.", "calculation": "none; no final-volume assumption", "proposed_amount": "none asserted"}, {"record_path": "data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "ingredient": "Tryptone (BD-Difco)", "existing": {"value": "2", "unit": "G_PER_L"}, "decision": "unsupported", "source_evidence": ["togo1107-api-q-0-3"], "source_locator": "$.components[0].items[3]", "source_row": {"component_name": "Tryptone (BD-Difco)", "volume": 2, "unit": "g", "gmo_id": "GMO_001043"}, "source_stage": "main solution 1", "explanation": "Source mass matches the local number, but it is an amount in the listed main batch. One litre of seawater plus5 ml vitamins does not establish a final litre. G_PER_L denominator is unverified; preserve mass and batch context.", "calculation": "none; no final-volume assumption", "proposed_amount": "none asserted"}, {"record_path": "data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "ingredient": "Artificial seawater (see below)", "existing": {"value": "1", "unit": "G_PER_L"}, "decision": "conflict", "source_evidence": ["togo1107-api-q-0-5"], "source_locator": "$.components[0].items[5]", "source_row": {"component_name": "Artificial seawater (see below)", "volume": 1, "unit": "L", "reference_media_id": "M1107"}, "source_stage": "main solution 1", "explanation": "Source specifies1 L of prepared artificial seawater added to the main batch, not1 G_PER_L ingredient. Restore a solution addition and its internal stock stages.", "calculation": "none; no final-volume assumption", "proposed_amount": "none asserted"}, {"record_path": "data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml", "field_path": "ingredients[5].concentration", "ingredient": "N2", "existing": {"value": "variable", "unit": "VARIABLE"}, "decision": "conflict", "source_evidence": ["togo1107-api-q-0-6"], "source_locator": "$.components[0].items[6]", "source_row": {"component_name": "N2", "gmo_id": "GMO_002261"}, "source_stage": "main solution 1", "explanation": "Source N2 is an unquantified gas atmosphere, supported by preparation prose. VARIABLE is not a measured solute concentration. Keep gas/headspace context without inventing amount, pressure or molarity.", "calculation": "none; no final-volume assumption", "proposed_amount": "none asserted"}, {"record_path": "data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml", "field_path": "ingredients[6].concentration", "ingredient": "Distilled water", "existing": {"value": "1", "unit": "G_PER_L"}, "decision": "conflict", "source_evidence": ["togo1107-api-q-1-0"], "source_locator": "$.components[1].items[0]", "source_row": {"component_name": "Distilled water", "volume": 1, "unit": "L", "gmo_id": "GMO_001001"}, "source_stage": "Artificial seawater", "explanation": "Source specifies1 L of distilled water used in the artificial-seawater stock, not1 G_PER_L direct solute or an explicit final-volume make-up.", "calculation": "none; no final-volume assumption", "proposed_amount": "none asserted"}, {"record_path": "data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml", "field_path": "ingredients[7].concentration", "ingredient": "MgSO4・7H2O", "existing": {"value": "6", "unit": "G_PER_L"}, "decision": "conflict", "source_evidence": ["togo1107-api-q-1-1"], "source_locator": "$.components[1].items[1]", "source_row": {"component_name": "MgSO4・7H2O", "volume": 6, "unit": "g", "gmo_id": "GMO_001002"}, "source_stage": "Artificial seawater", "explanation": "Source mass belongs to artificial-seawater preparation, not a direct main-medium concentration. Preserve exact salt/hydrate and mass in that stock; do not infer stock or final-medium rate from water input.", "calculation": "none; no final-volume assumption", "proposed_amount": "none asserted"}, {"record_path": "data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml", "field_path": "ingredients[8].concentration", "ingredient": "NaCl", "existing": {"value": "22", "unit": "G_PER_L"}, "decision": "conflict", "source_evidence": ["togo1107-api-q-1-2"], "source_locator": "$.components[1].items[2]", "source_row": {"component_name": "NaCl", "volume": 22, "unit": "g", "gmo_id": "GMO_001004"}, "source_stage": "Artificial seawater", "explanation": "Source mass belongs to artificial-seawater preparation, not a direct main-medium concentration. Preserve exact salt/hydrate and mass in that stock; do not infer stock or final-medium rate from water input.", "calculation": "none; no final-volume assumption", "proposed_amount": "none asserted"}, {"record_path": "data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml", "field_path": "ingredients[9].concentration", "ingredient": "CaCl2・2H2O", "existing": {"value": "0.3", "unit": "G_PER_L"}, "decision": "conflict", "source_evidence": ["togo1107-api-q-1-3"], "source_locator": "$.components[1].items[3]", "source_row": {"component_name": "CaCl2・2H2O", "volume": 0.3, "unit": "g", "gmo_id": "GMO_001005"}, "source_stage": "Artificial seawater", "explanation": "Source mass belongs to artificial-seawater preparation, not a direct main-medium concentration. Preserve exact salt/hydrate and mass in that stock; do not infer stock or final-medium rate from water input.", "calculation": "none; no final-volume assumption", "proposed_amount": "none asserted"}, {"record_path": "data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml", "field_path": "ingredients[10].concentration", "ingredient": "KH2PO4", "existing": {"value": "0.42", "unit": "G_PER_L"}, "decision": "conflict", "source_evidence": ["togo1107-api-q-1-4"], "source_locator": "$.components[1].items[4]", "source_row": {"component_name": "KH2PO4", "volume": 0.42, "unit": "g", "gmo_id": "GMO_001006"}, "source_stage": "Artificial seawater", "explanation": "Source mass belongs to artificial-seawater preparation, not a direct main-medium concentration. Preserve exact salt/hydrate and mass in that stock; do not infer stock or final-medium rate from water input.", "calculation": "none; no final-volume assumption", "proposed_amount": "none asserted"}, {"record_path": "data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml", "field_path": "ingredients[11].concentration", "ingredient": "MgCl2・6H2O", "existing": {"value": "3", "unit": "G_PER_L"}, "decision": "conflict", "source_evidence": ["togo1107-api-q-1-5"], "source_locator": "$.components[1].items[5]", "source_row": {"component_name": "MgCl2・6H2O", "volume": 3, "unit": "g", "gmo_id": "GMO_001013"}, "source_stage": "Artificial seawater", "explanation": "Source mass belongs to artificial-seawater preparation, not a direct main-medium concentration. Preserve exact salt/hydrate and mass in that stock; do not infer stock or final-medium rate from water input.", "calculation": "none; no final-volume assumption", "proposed_amount": "none asserted"}, {"record_path": "data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml", "field_path": "ingredients[12].concentration", "ingredient": "KCl", "existing": {"value": "0.5", "unit": "G_PER_L"}, "decision": "conflict", "source_evidence": ["togo1107-api-q-1-6"], "source_locator": "$.components[1].items[6]", "source_row": {"component_name": "KCl", "volume": 0.5, "unit": "g", "gmo_id": "GMO_001017"}, "source_stage": "Artificial seawater", "explanation": "Source mass belongs to artificial-seawater preparation, not a direct main-medium concentration. Preserve exact salt/hydrate and mass in that stock; do not infer stock or final-medium rate from water input.", "calculation": "none; no final-volume assumption", "proposed_amount": "none asserted"}, {"record_path": "data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml", "field_path": "ingredients[13].concentration", "ingredient": "NaHCO3", "existing": {"value": "0.2", "unit": "G_PER_L"}, "decision": "conflict", "source_evidence": ["togo1107-api-q-1-7"], "source_locator": "$.components[1].items[7]", "source_row": {"component_name": "NaHCO3", "volume": 0.2, "unit": "g", "gmo_id": "GMO_001019"}, "source_stage": "Artificial seawater", "explanation": "Source mass belongs to artificial-seawater preparation, not a direct main-medium concentration. Preserve exact salt/hydrate and mass in that stock; do not infer stock or final-medium rate from water input.", "calculation": "none; no final-volume assumption", "proposed_amount": "none asserted"}, {"record_path": "data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml", "field_path": "ingredients[14].concentration", "ingredient": "(NH4)2SO4", "existing": {"value": "1", "unit": "G_PER_L"}, "decision": "conflict", "source_evidence": ["togo1107-api-q-1-8"], "source_locator": "$.components[1].items[8]", "source_row": {"component_name": "(NH4)2SO4", "volume": 1, "unit": "g", "gmo_id": "GMO_001030"}, "source_stage": "Artificial seawater", "explanation": "Source mass belongs to artificial-seawater preparation, not a direct main-medium concentration. Preserve exact salt/hydrate and mass in that stock; do not infer stock or final-medium rate from water input.", "calculation": "none; no final-volume assumption", "proposed_amount": "none asserted"}, {"record_path": "data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml", "field_path": "ingredients[15].concentration", "ingredient": "NaBr", "existing": {"value": "0.05", "unit": "G_PER_L"}, "decision": "conflict", "source_evidence": ["togo1107-api-q-1-9"], "source_locator": "$.components[1].items[9]", "source_row": {"component_name": "NaBr", "volume": 0.05, "unit": "g", "gmo_id": "GMO_001073"}, "source_stage": "Artificial seawater", "explanation": "Source mass belongs to artificial-seawater preparation, not a direct main-medium concentration. Preserve exact salt/hydrate and mass in that stock; do not infer stock or final-medium rate from water input.", "calculation": "none; no final-volume assumption", "proposed_amount": "none asserted"}, {"record_path": "data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml", "field_path": "ingredients[16].concentration", "ingredient": "SrCl2・6H2O", "existing": {"value": "0.02", "unit": "G_PER_L"}, "decision": "conflict", "source_evidence": ["togo1107-api-q-1-10"], "source_locator": "$.components[1].items[10]", "source_row": {"component_name": "SrCl2・6H2O", "volume": 0.02, "unit": "g", "gmo_id": "GMO_001085"}, "source_stage": "Artificial seawater", "explanation": "Source mass belongs to artificial-seawater preparation, not a direct main-medium concentration. Preserve exact salt/hydrate and mass in that stock; do not infer stock or final-medium rate from water input.", "calculation": "none; no final-volume assumption", "proposed_amount": "none asserted"}, {"record_path": "data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml", "field_path": "ingredients[17].concentration", "ingredient": "Ammonium Fe(III) citrate", "existing": {"value": "0.01", "unit": "G_PER_L"}, "decision": "conflict", "source_evidence": ["togo1107-api-q-1-11"], "source_locator": "$.components[1].items[11]", "source_row": {"component_name": "Ammonium Fe(III) citrate", "volume": 0.01, "unit": "g", "gmo_id": "GMO_001147"}, "source_stage": "Artificial seawater", "explanation": "Source mass belongs to artificial-seawater preparation, not a direct main-medium concentration. Preserve exact salt/hydrate and mass in that stock; do not infer stock or final-medium rate from water input.", "calculation": "none; no final-volume assumption", "proposed_amount": "none asserted"}, {"record_path": "data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml", "field_path": "solutions[0].concentration", "ingredient": "Trace vitamins (see Medium [M190])", "existing": {"value": "5", "unit": "G_PER_L"}, "decision": "conflict", "source_evidence": ["togo1107-api-q-0-4"], "source_locator": "$.components[0].items[4]", "source_row": {"component_name": "Trace vitamins (see Medium [M190])", "volume": 5, "unit": "ml", "reference_media_id": "M190"}, "explanation": "Source5 ml vitamin-stock addition belongs to the main batch. G_PER_L is the wrong dimension; final-volume basis for ML_PER_L is also unproved. Restore the batch dose and complete dependency definition.", "calculation": "none; no density or final-volume assumption", "proposed_amount": "none asserted"}, {"record_path": "data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml", "field_path": "solutions[1].concentration", "ingredient": "Trace minerals (see Medium [M142])", "existing": {"value": "5", "unit": "G_PER_L"}, "decision": "conflict", "source_evidence": ["togo1107-api-q-1-12"], "source_locator": "$.components[1].items[12]", "source_row": {"component_name": "Trace minerals (see Medium [M142])", "volume": 5, "unit": "ml", "reference_media_id": "M142"}, "explanation": "Source5 ml trace-mineral addition belongs inside the artificial-seawater batch. G_PER_L is the wrong dimension; final-volume basis for ML_PER_L is also unproved. Restore the batch dose and complete dependency definition.", "calculation": "none; no density or final-volume assumption", "proposed_amount": "none asserted"}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml", "field_path": "ingredients[0].concentration", "ingredient": "Sodium pyruvate", "existing": {"value": "5", "unit": "G_PER_L"}, "decision": "unsupported", "source_evidence": ["togo1107-api-q-0-0"], "source_locator": "$.components[0].items[0]", "source_row": {"component_name": "Sodium pyruvate", "volume": 5, "unit": "g", "gmo_id": "GMO_001055"}, "source_stage": "main solution 1", "explanation": "Source mass matches the local number, but it is an amount in the listed main batch. One litre of seawater plus5 ml vitamins does not establish a final litre. G_PER_L denominator is unverified; preserve mass and batch context.", "calculation": "none; no final-volume assumption", "proposed_amount": "none asserted"}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml", "field_path": "ingredients[1].concentration", "ingredient": "PIPES", "existing": {"value": "3.46", "unit": "G_PER_L"}, "decision": "unsupported", "source_evidence": ["togo1107-api-q-0-1"], "source_locator": "$.components[0].items[1]", "source_row": {"component_name": "PIPES", "volume": 3.46, "unit": "g", "gmo_id": "GMO_001223"}, "source_stage": "main solution 1", "explanation": "Source mass matches the local number, but it is an amount in the listed main batch. One litre of seawater plus5 ml vitamins does not establish a final litre. G_PER_L denominator is unverified; preserve mass and batch context.", "calculation": "none; no final-volume assumption", "proposed_amount": "none asserted"}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml", "field_path": "ingredients[2].concentration", "ingredient": "Yeast extract (BD-Difco)", "existing": {"value": "2", "unit": "G_PER_L"}, "decision": "unsupported", "source_evidence": ["togo1107-api-q-0-2"], "source_locator": "$.components[0].items[2]", "source_row": {"component_name": "Yeast extract (BD-Difco)", "volume": 2, "unit": "g", "gmo_id": "GMO_001018"}, "source_stage": "main solution 1", "explanation": "Source mass matches the local number, but it is an amount in the listed main batch. One litre of seawater plus5 ml vitamins does not establish a final litre. G_PER_L denominator is unverified; preserve mass and batch context.", "calculation": "none; no final-volume assumption", "proposed_amount": "none asserted"}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml", "field_path": "ingredients[3].concentration", "ingredient": "Tryptone (BD-Difco)", "existing": {"value": "2", "unit": "G_PER_L"}, "decision": "unsupported", "source_evidence": ["togo1107-api-q-0-3"], "source_locator": "$.components[0].items[3]", "source_row": {"component_name": "Tryptone (BD-Difco)", "volume": 2, "unit": "g", "gmo_id": "GMO_001043"}, "source_stage": "main solution 1", "explanation": "Source mass matches the local number, but it is an amount in the listed main batch. One litre of seawater plus5 ml vitamins does not establish a final litre. G_PER_L denominator is unverified; preserve mass and batch context.", "calculation": "none; no final-volume assumption", "proposed_amount": "none asserted"}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml", "field_path": "ingredients[4].concentration", "ingredient": "Artificial seawater (see below)", "existing": {"value": "1", "unit": "G_PER_L"}, "decision": "conflict", "source_evidence": ["togo1107-api-q-0-5"], "source_locator": "$.components[0].items[5]", "source_row": {"component_name": "Artificial seawater (see below)", "volume": 1, "unit": "L", "reference_media_id": "M1107"}, "source_stage": "main solution 1", "explanation": "Source specifies1 L of prepared artificial seawater added to the main batch, not1 G_PER_L ingredient. Restore a solution addition and its internal stock stages.", "calculation": "none; no final-volume assumption", "proposed_amount": "none asserted"}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml", "field_path": "ingredients[5].concentration", "ingredient": "N2", "existing": {"value": "variable", "unit": "VARIABLE"}, "decision": "conflict", "source_evidence": ["togo1107-api-q-0-6"], "source_locator": "$.components[0].items[6]", "source_row": {"component_name": "N2", "gmo_id": "GMO_002261"}, "source_stage": "main solution 1", "explanation": "Source N2 is an unquantified gas atmosphere, supported by preparation prose. VARIABLE is not a measured solute concentration. Keep gas/headspace context without inventing amount, pressure or molarity.", "calculation": "none; no final-volume assumption", "proposed_amount": "none asserted"}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml", "field_path": "ingredients[6].concentration", "ingredient": "Distilled water", "existing": {"value": "1", "unit": "G_PER_L"}, "decision": "conflict", "source_evidence": ["togo1107-api-q-1-0"], "source_locator": "$.components[1].items[0]", "source_row": {"component_name": "Distilled water", "volume": 1, "unit": "L", "gmo_id": "GMO_001001"}, "source_stage": "Artificial seawater", "explanation": "Source specifies1 L of distilled water used in the artificial-seawater stock, not1 G_PER_L direct solute or an explicit final-volume make-up.", "calculation": "none; no final-volume assumption", "proposed_amount": "none asserted"}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml", "field_path": "ingredients[7].concentration", "ingredient": "MgSO4・7H2O", "existing": {"value": "6", "unit": "G_PER_L"}, "decision": "conflict", "source_evidence": ["togo1107-api-q-1-1"], "source_locator": "$.components[1].items[1]", "source_row": {"component_name": "MgSO4・7H2O", "volume": 6, "unit": "g", "gmo_id": "GMO_001002"}, "source_stage": "Artificial seawater", "explanation": "Source mass belongs to artificial-seawater preparation, not a direct main-medium concentration. Preserve exact salt/hydrate and mass in that stock; do not infer stock or final-medium rate from water input.", "calculation": "none; no final-volume assumption", "proposed_amount": "none asserted"}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml", "field_path": "ingredients[8].concentration", "ingredient": "NaCl", "existing": {"value": "22", "unit": "G_PER_L"}, "decision": "conflict", "source_evidence": ["togo1107-api-q-1-2"], "source_locator": "$.components[1].items[2]", "source_row": {"component_name": "NaCl", "volume": 22, "unit": "g", "gmo_id": "GMO_001004"}, "source_stage": "Artificial seawater", "explanation": "Source mass belongs to artificial-seawater preparation, not a direct main-medium concentration. Preserve exact salt/hydrate and mass in that stock; do not infer stock or final-medium rate from water input.", "calculation": "none; no final-volume assumption", "proposed_amount": "none asserted"}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml", "field_path": "ingredients[9].concentration", "ingredient": "CaCl2・2H2O", "existing": {"value": "0.3", "unit": "G_PER_L"}, "decision": "conflict", "source_evidence": ["togo1107-api-q-1-3"], "source_locator": "$.components[1].items[3]", "source_row": {"component_name": "CaCl2・2H2O", "volume": 0.3, "unit": "g", "gmo_id": "GMO_001005"}, "source_stage": "Artificial seawater", "explanation": "Source mass belongs to artificial-seawater preparation, not a direct main-medium concentration. Preserve exact salt/hydrate and mass in that stock; do not infer stock or final-medium rate from water input.", "calculation": "none; no final-volume assumption", "proposed_amount": "none asserted"}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml", "field_path": "ingredients[10].concentration", "ingredient": "KH2PO4", "existing": {"value": "0.42", "unit": "G_PER_L"}, "decision": "conflict", "source_evidence": ["togo1107-api-q-1-4"], "source_locator": "$.components[1].items[4]", "source_row": {"component_name": "KH2PO4", "volume": 0.42, "unit": "g", "gmo_id": "GMO_001006"}, "source_stage": "Artificial seawater", "explanation": "Source mass belongs to artificial-seawater preparation, not a direct main-medium concentration. Preserve exact salt/hydrate and mass in that stock; do not infer stock or final-medium rate from water input.", "calculation": "none; no final-volume assumption", "proposed_amount": "none asserted"}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml", "field_path": "ingredients[11].concentration", "ingredient": "MgCl2・6H2O", "existing": {"value": "3", "unit": "G_PER_L"}, "decision": "conflict", "source_evidence": ["togo1107-api-q-1-5"], "source_locator": "$.components[1].items[5]", "source_row": {"component_name": "MgCl2・6H2O", "volume": 3, "unit": "g", "gmo_id": "GMO_001013"}, "source_stage": "Artificial seawater", "explanation": "Source mass belongs to artificial-seawater preparation, not a direct main-medium concentration. Preserve exact salt/hydrate and mass in that stock; do not infer stock or final-medium rate from water input.", "calculation": "none; no final-volume assumption", "proposed_amount": "none asserted"}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml", "field_path": "ingredients[12].concentration", "ingredient": "KCl", "existing": {"value": "0.5", "unit": "G_PER_L"}, "decision": "conflict", "source_evidence": ["togo1107-api-q-1-6"], "source_locator": "$.components[1].items[6]", "source_row": {"component_name": "KCl", "volume": 0.5, "unit": "g", "gmo_id": "GMO_001017"}, "source_stage": "Artificial seawater", "explanation": "Source mass belongs to artificial-seawater preparation, not a direct main-medium concentration. Preserve exact salt/hydrate and mass in that stock; do not infer stock or final-medium rate from water input.", "calculation": "none; no final-volume assumption", "proposed_amount": "none asserted"}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml", "field_path": "ingredients[13].concentration", "ingredient": "NaHCO3", "existing": {"value": "0.2", "unit": "G_PER_L"}, "decision": "conflict", "source_evidence": ["togo1107-api-q-1-7"], "source_locator": "$.components[1].items[7]", "source_row": {"component_name": "NaHCO3", "volume": 0.2, "unit": "g", "gmo_id": "GMO_001019"}, "source_stage": "Artificial seawater", "explanation": "Source mass belongs to artificial-seawater preparation, not a direct main-medium concentration. Preserve exact salt/hydrate and mass in that stock; do not infer stock or final-medium rate from water input.", "calculation": "none; no final-volume assumption", "proposed_amount": "none asserted"}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml", "field_path": "ingredients[14].concentration", "ingredient": "(NH4)2SO4", "existing": {"value": "1", "unit": "G_PER_L"}, "decision": "conflict", "source_evidence": ["togo1107-api-q-1-8"], "source_locator": "$.components[1].items[8]", "source_row": {"component_name": "(NH4)2SO4", "volume": 1, "unit": "g", "gmo_id": "GMO_001030"}, "source_stage": "Artificial seawater", "explanation": "Source mass belongs to artificial-seawater preparation, not a direct main-medium concentration. Preserve exact salt/hydrate and mass in that stock; do not infer stock or final-medium rate from water input.", "calculation": "none; no final-volume assumption", "proposed_amount": "none asserted"}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml", "field_path": "ingredients[15].concentration", "ingredient": "NaBr", "existing": {"value": "0.05", "unit": "G_PER_L"}, "decision": "conflict", "source_evidence": ["togo1107-api-q-1-9"], "source_locator": "$.components[1].items[9]", "source_row": {"component_name": "NaBr", "volume": 0.05, "unit": "g", "gmo_id": "GMO_001073"}, "source_stage": "Artificial seawater", "explanation": "Source mass belongs to artificial-seawater preparation, not a direct main-medium concentration. Preserve exact salt/hydrate and mass in that stock; do not infer stock or final-medium rate from water input.", "calculation": "none; no final-volume assumption", "proposed_amount": "none asserted"}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml", "field_path": "ingredients[16].concentration", "ingredient": "SrCl2・6H2O", "existing": {"value": "0.02", "unit": "G_PER_L"}, "decision": "conflict", "source_evidence": ["togo1107-api-q-1-10"], "source_locator": "$.components[1].items[10]", "source_row": {"component_name": "SrCl2・6H2O", "volume": 0.02, "unit": "g", "gmo_id": "GMO_001085"}, "source_stage": "Artificial seawater", "explanation": "Source mass belongs to artificial-seawater preparation, not a direct main-medium concentration. Preserve exact salt/hydrate and mass in that stock; do not infer stock or final-medium rate from water input.", "calculation": "none; no final-volume assumption", "proposed_amount": "none asserted"}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml", "field_path": "ingredients[17].concentration", "ingredient": "Ammonium Fe(III) citrate", "existing": {"value": "0.01", "unit": "G_PER_L"}, "decision": "conflict", "source_evidence": ["togo1107-api-q-1-11"], "source_locator": "$.components[1].items[11]", "source_row": {"component_name": "Ammonium Fe(III) citrate", "volume": 0.01, "unit": "g", "gmo_id": "GMO_001147"}, "source_stage": "Artificial seawater", "explanation": "Source mass belongs to artificial-seawater preparation, not a direct main-medium concentration. Preserve exact salt/hydrate and mass in that stock; do not infer stock or final-medium rate from water input.", "calculation": "none; no final-volume assumption", "proposed_amount": "none asserted"}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml", "field_path": "solutions[0].concentration", "ingredient": "Trace vitamins (see Medium [M190])", "existing": {"value": "5", "unit": "G_PER_L"}, "decision": "conflict", "source_evidence": ["togo1107-api-q-0-4"], "source_locator": "$.components[0].items[4]", "source_row": {"component_name": "Trace vitamins (see Medium [M190])", "volume": 5, "unit": "ml", "reference_media_id": "M190"}, "explanation": "Source5 ml vitamin-stock addition belongs to the main batch. G_PER_L is the wrong dimension; final-volume basis for ML_PER_L is also unproved. Restore the batch dose and complete dependency definition.", "calculation": "none; no density or final-volume assumption", "proposed_amount": "none asserted"}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml", "field_path": "solutions[1].concentration", "ingredient": "Trace minerals (see Medium [M142])", "existing": {"value": "5", "unit": "G_PER_L"}, "decision": "conflict", "source_evidence": ["togo1107-api-q-1-12"], "source_locator": "$.components[1].items[12]", "source_row": {"component_name": "Trace minerals (see Medium [M142])", "volume": 5, "unit": "ml", "reference_media_id": "M142"}, "explanation": "Source5 ml trace-mineral addition belongs inside the artificial-seawater batch. G_PER_L is the wrong dimension; final-volume basis for ML_PER_L is also unproved. Restore the batch dose and complete dependency definition.", "calculation": "none; no density or final-volume assumption", "proposed_amount": "none asserted"}], "source_rows": [{"evidence_id": "togo1107-api-q-0-0", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107", "locator": "$.components[0].items[0]", "stage": "main solution 1", "source_row": {"component_name": "Sodium pyruvate", "volume": 5, "unit": "g", "gmo_id": "GMO_001055"}, "decision": "evidence_only", "calculation": "none; source batch amount/input retained, no final-medium rate inferred"}, {"evidence_id": "togo1107-api-q-0-1", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107", "locator": "$.components[0].items[1]", "stage": "main solution 1", "source_row": {"component_name": "PIPES", "volume": 3.46, "unit": "g", "gmo_id": "GMO_001223"}, "decision": "evidence_only", "calculation": "none; source batch amount/input retained, no final-medium rate inferred"}, {"evidence_id": "togo1107-api-q-0-2", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107", "locator": "$.components[0].items[2]", "stage": "main solution 1", "source_row": {"component_name": "Yeast extract (BD-Difco)", "volume": 2, "unit": "g", "gmo_id": "GMO_001018"}, "decision": "evidence_only", "calculation": "none; source batch amount/input retained, no final-medium rate inferred"}, {"evidence_id": "togo1107-api-q-0-3", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107", "locator": "$.components[0].items[3]", "stage": "main solution 1", "source_row": {"component_name": "Tryptone (BD-Difco)", "volume": 2, "unit": "g", "gmo_id": "GMO_001043"}, "decision": "evidence_only", "calculation": "none; source batch amount/input retained, no final-medium rate inferred"}, {"evidence_id": "togo1107-api-q-0-4", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107", "locator": "$.components[0].items[4]", "stage": "main solution 1", "source_row": {"component_name": "Trace vitamins (see Medium [M190])", "volume": 5, "unit": "ml", "reference_media_id": "M190"}, "decision": "evidence_only", "calculation": "none; source batch amount/input retained, no final-medium rate inferred"}, {"evidence_id": "togo1107-api-q-0-5", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107", "locator": "$.components[0].items[5]", "stage": "main solution 1", "source_row": {"component_name": "Artificial seawater (see below)", "volume": 1, "unit": "L", "reference_media_id": "M1107"}, "decision": "evidence_only", "calculation": "none; source batch amount/input retained, no final-medium rate inferred"}, {"evidence_id": "togo1107-api-q-0-6", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107", "locator": "$.components[0].items[6]", "stage": "main solution 1", "source_row": {"component_name": "N2", "gmo_id": "GMO_002261"}, "decision": "not_quantified", "calculation": "none; source batch amount/input retained, no final-medium rate inferred"}, {"evidence_id": "togo1107-api-q-1-0", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107", "locator": "$.components[1].items[0]", "stage": "Artificial seawater", "source_row": {"component_name": "Distilled water", "volume": 1, "unit": "L", "gmo_id": "GMO_001001"}, "decision": "evidence_only", "calculation": "none; source batch amount/input retained, no final-medium rate inferred"}, {"evidence_id": "togo1107-api-q-1-1", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107", "locator": "$.components[1].items[1]", "stage": "Artificial seawater", "source_row": {"component_name": "MgSO4・7H2O", "volume": 6, "unit": "g", "gmo_id": "GMO_001002"}, "decision": "evidence_only", "calculation": "none; source batch amount/input retained, no final-medium rate inferred"}, {"evidence_id": "togo1107-api-q-1-2", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107", "locator": "$.components[1].items[2]", "stage": "Artificial seawater", "source_row": {"component_name": "NaCl", "volume": 22, "unit": "g", "gmo_id": "GMO_001004"}, "decision": "evidence_only", "calculation": "none; source batch amount/input retained, no final-medium rate inferred"}, {"evidence_id": "togo1107-api-q-1-3", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107", "locator": "$.components[1].items[3]", "stage": "Artificial seawater", "source_row": {"component_name": "CaCl2・2H2O", "volume": 0.3, "unit": "g", "gmo_id": "GMO_001005"}, "decision": "evidence_only", "calculation": "none; source batch amount/input retained, no final-medium rate inferred"}, {"evidence_id": "togo1107-api-q-1-4", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107", "locator": "$.components[1].items[4]", "stage": "Artificial seawater", "source_row": {"component_name": "KH2PO4", "volume": 0.42, "unit": "g", "gmo_id": "GMO_001006"}, "decision": "evidence_only", "calculation": "none; source batch amount/input retained, no final-medium rate inferred"}, {"evidence_id": "togo1107-api-q-1-5", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107", "locator": "$.components[1].items[5]", "stage": "Artificial seawater", "source_row": {"component_name": "MgCl2・6H2O", "volume": 3, "unit": "g", "gmo_id": "GMO_001013"}, "decision": "evidence_only", "calculation": "none; source batch amount/input retained, no final-medium rate inferred"}, {"evidence_id": "togo1107-api-q-1-6", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107", "locator": "$.components[1].items[6]", "stage": "Artificial seawater", "source_row": {"component_name": "KCl", "volume": 0.5, "unit": "g", "gmo_id": "GMO_001017"}, "decision": "evidence_only", "calculation": "none; source batch amount/input retained, no final-medium rate inferred"}, {"evidence_id": "togo1107-api-q-1-7", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107", "locator": "$.components[1].items[7]", "stage": "Artificial seawater", "source_row": {"component_name": "NaHCO3", "volume": 0.2, "unit": "g", "gmo_id": "GMO_001019"}, "decision": "evidence_only", "calculation": "none; source batch amount/input retained, no final-medium rate inferred"}, {"evidence_id": "togo1107-api-q-1-8", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107", "locator": "$.components[1].items[8]", "stage": "Artificial seawater", "source_row": {"component_name": "(NH4)2SO4", "volume": 1, "unit": "g", "gmo_id": "GMO_001030"}, "decision": "evidence_only", "calculation": "none; source batch amount/input retained, no final-medium rate inferred"}, {"evidence_id": "togo1107-api-q-1-9", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107", "locator": "$.components[1].items[9]", "stage": "Artificial seawater", "source_row": {"component_name": "NaBr", "volume": 0.05, "unit": "g", "gmo_id": "GMO_001073"}, "decision": "evidence_only", "calculation": "none; source batch amount/input retained, no final-medium rate inferred"}, {"evidence_id": "togo1107-api-q-1-10", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107", "locator": "$.components[1].items[10]", "stage": "Artificial seawater", "source_row": {"component_name": "SrCl2・6H2O", "volume": 0.02, "unit": "g", "gmo_id": "GMO_001085"}, "decision": "evidence_only", "calculation": "none; source batch amount/input retained, no final-medium rate inferred"}, {"evidence_id": "togo1107-api-q-1-11", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107", "locator": "$.components[1].items[11]", "stage": "Artificial seawater", "source_row": {"component_name": "Ammonium Fe(III) citrate", "volume": 0.01, "unit": "g", "gmo_id": "GMO_001147"}, "decision": "evidence_only", "calculation": "none; source batch amount/input retained, no final-medium rate inferred"}, {"evidence_id": "togo1107-api-q-1-12", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107", "locator": "$.components[1].items[12]", "stage": "Artificial seawater", "source_row": {"component_name": "Trace minerals (see Medium [M142])", "volume": 5, "unit": "ml", "reference_media_id": "M142"}, "decision": "evidence_only", "calculation": "none; source batch amount/input retained, no final-medium rate inferred"}, {"evidence_id": "togo142-api-q-2-0", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "locator": "$.components[2].items[0]", "stage": "Trace minerals", "source_row": {"component_name": "Distilled water", "volume": 1, "unit": "L", "gmo_id": "GMO_001001"}, "decision": "evidence_only", "calculation": "none; source batch amount/input retained, no final-medium rate inferred"}, {"evidence_id": "togo142-api-q-2-1", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "locator": "$.components[2].items[1]", "stage": "Trace minerals", "source_row": {"component_name": "MgSO4・7H2O", "volume": 3, "unit": "g", "gmo_id": "GMO_001002"}, "decision": "evidence_only", "calculation": "none; source batch amount/input retained, no final-medium rate inferred"}, {"evidence_id": "togo142-api-q-2-2", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "locator": "$.components[2].items[2]", "stage": "Trace minerals", "source_row": {"component_name": "NaCl", "volume": 1, "unit": "g", "gmo_id": "GMO_001004"}, "decision": "evidence_only", "calculation": "none; source batch amount/input retained, no final-medium rate inferred"}, {"evidence_id": "togo142-api-q-2-3", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "locator": "$.components[2].items[3]", "stage": "Trace minerals", "source_row": {"component_name": "CaCl2・2H2O", "volume": 0.1, "unit": "g", "gmo_id": "GMO_001005"}, "decision": "evidence_only", "calculation": "none; source batch amount/input retained, no final-medium rate inferred"}, {"evidence_id": "togo142-api-q-2-4", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "locator": "$.components[2].items[4]", "stage": "Trace minerals", "source_row": {"component_name": "Na2MoO4・2H2O", "volume": 0.01, "unit": "g", "gmo_id": "GMO_001011"}, "decision": "evidence_only", "calculation": "none; source batch amount/input retained, no final-medium rate inferred"}, {"evidence_id": "togo142-api-q-2-5", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "locator": "$.components[2].items[5]", "stage": "Trace minerals", "source_row": {"component_name": "H3BO3", "volume": 0.01, "unit": "g", "gmo_id": "GMO_001015"}, "decision": "evidence_only", "calculation": "none; source batch amount/input retained, no final-medium rate inferred"}, {"evidence_id": "togo142-api-q-2-6", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "locator": "$.components[2].items[6]", "stage": "Trace minerals", "source_row": {"component_name": "FeSO4・7H2O", "volume": 0.1, "unit": "g", "gmo_id": "GMO_001016"}, "decision": "evidence_only", "calculation": "none; source batch amount/input retained, no final-medium rate inferred"}, {"evidence_id": "togo142-api-q-2-7", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "locator": "$.components[2].items[7]", "stage": "Trace minerals", "source_row": {"component_name": "ZnSO4・7H2O", "volume": 0.1, "unit": "g", "gmo_id": "GMO_001023"}, "decision": "evidence_only", "calculation": "none; source batch amount/input retained, no final-medium rate inferred"}, {"evidence_id": "togo142-api-q-2-8", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "locator": "$.components[2].items[8]", "stage": "Trace minerals", "source_row": {"component_name": "CuSO4・5H2O", "volume": 0.01, "unit": "g", "gmo_id": "GMO_001039"}, "decision": "evidence_only", "calculation": "none; source batch amount/input retained, no final-medium rate inferred"}, {"evidence_id": "togo142-api-q-2-9", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "locator": "$.components[2].items[9]", "stage": "Trace minerals", "source_row": {"component_name": "CoSO4・7H2O", "volume": 0.1, "unit": "g", "gmo_id": "GMO_001050"}, "decision": "evidence_only", "calculation": "none; source batch amount/input retained, no final-medium rate inferred"}, {"evidence_id": "togo142-api-q-2-10", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "locator": "$.components[2].items[10]", "stage": "Trace minerals", "source_row": {"component_name": "Nitrilotriacetic acid", "volume": 1.5, "unit": "g", "gmo_id": "GMO_001053"}, "decision": "evidence_only", "calculation": "none; source batch amount/input retained, no final-medium rate inferred"}, {"evidence_id": "togo142-api-q-2-11", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "locator": "$.components[2].items[11]", "stage": "Trace minerals", "source_row": {"component_name": "MnSO4・xH2O", "volume": 0.5, "unit": "g", "gmo_id": "GMO_001065"}, "decision": "evidence_only", "calculation": "none; source batch amount/input retained, no final-medium rate inferred"}, {"evidence_id": "togo142-api-q-2-12", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "locator": "$.components[2].items[12]", "stage": "Trace minerals", "source_row": {"component_name": "AlK(SO4)2", "volume": 0.01, "unit": "g", "gmo_id": "GMO_001088"}, "decision": "evidence_only", "calculation": "none; source batch amount/input retained, no final-medium rate inferred"}, {"evidence_id": "togo142-api-q-2-13", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "locator": "$.components[2].items[13]", "stage": "Trace minerals", "source_row": {"component_name": "KOH solution", "gmo_id": "GMO_001903"}, "decision": "not_quantified", "calculation": "none; source batch amount/input retained, no final-medium rate inferred"}, {"evidence_id": "togo190-api-q-1-0", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "locator": "$.components[1].items[0]", "stage": "Trace vitamins", "source_row": {"component_name": "Distilled water", "volume": 1, "unit": "L", "gmo_id": "GMO_001001"}, "decision": "evidence_only", "calculation": "none; source batch amount/input retained, no final-medium rate inferred"}, {"evidence_id": "togo190-api-q-1-1", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "locator": "$.components[1].items[1]", "stage": "Trace vitamins", "source_row": {"component_name": "Biotin", "volume": 2, "unit": "mg", "gmo_id": "GMO_001025"}, "decision": "evidence_only", "calculation": "none; source batch amount/input retained, no final-medium rate inferred"}, {"evidence_id": "togo190-api-q-1-2", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "locator": "$.components[1].items[2]", "stage": "Trace vitamins", "source_row": {"component_name": "p--Aminobenzoic acid", "volume": 5, "unit": "mg", "gmo_id": "GMO_001026"}, "decision": "evidence_only", "calculation": "none; source batch amount/input retained, no final-medium rate inferred"}, {"evidence_id": "togo190-api-q-1-3", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "locator": "$.components[1].items[3]", "stage": "Trace vitamins", "source_row": {"component_name": "Thiamine・HCl", "volume": 5, "unit": "mg", "gmo_id": "GMO_001027"}, "decision": "evidence_only", "calculation": "none; source batch amount/input retained, no final-medium rate inferred"}, {"evidence_id": "togo190-api-q-1-4", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "locator": "$.components[1].items[4]", "stage": "Trace vitamins", "source_row": {"component_name": "Calcium pantothenate", "volume": 5, "unit": "mg", "gmo_id": "GMO_001028"}, "decision": "evidence_only", "calculation": "none; source batch amount/input retained, no final-medium rate inferred"}, {"evidence_id": "togo190-api-q-1-5", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "locator": "$.components[1].items[5]", "stage": "Trace vitamins", "source_row": {"component_name": "Pyridoxine・HCl", "volume": 10, "unit": "mg", "gmo_id": "GMO_001029"}, "decision": "evidence_only", "calculation": "none; source batch amount/input retained, no final-medium rate inferred"}, {"evidence_id": "togo190-api-q-1-6", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "locator": "$.components[1].items[6]", "stage": "Trace vitamins", "source_row": {"component_name": "Folic acid", "volume": 2, "unit": "mg", "gmo_id": "GMO_001033"}, "decision": "evidence_only", "calculation": "none; source batch amount/input retained, no final-medium rate inferred"}, {"evidence_id": "togo190-api-q-1-7", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "locator": "$.components[1].items[7]", "stage": "Trace vitamins", "source_row": {"component_name": "Vitamin B12", "volume": 0.1, "unit": "mg", "gmo_id": "GMO_001034"}, "decision": "evidence_only", "calculation": "none; source batch amount/input retained, no final-medium rate inferred"}, {"evidence_id": "togo190-api-q-1-8", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "locator": "$.components[1].items[8]", "stage": "Trace vitamins", "source_row": {"component_name": "Riboflavin", "volume": 5, "unit": "mg", "gmo_id": "GMO_001037"}, "decision": "evidence_only", "calculation": "none; source batch amount/input retained, no final-medium rate inferred"}, {"evidence_id": "togo190-api-q-1-9", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "locator": "$.components[1].items[9]", "stage": "Trace vitamins", "source_row": {"component_name": "Nicotinic acid", "volume": 5, "unit": "mg", "gmo_id": "GMO_001038"}, "decision": "evidence_only", "calculation": "none; source batch amount/input retained, no final-medium rate inferred"}, {"evidence_id": "togo190-api-q-1-10", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "locator": "$.components[1].items[10]", "stage": "Trace vitamins", "source_row": {"component_name": "Lipoic acid", "volume": 5, "unit": "mg", "gmo_id": "GMO_001699"}, "decision": "evidence_only", "calculation": "none; source batch amount/input retained, no final-medium rate inferred"}], "corroborating_mediadive_rows": [{"solution_id": 5101, "solution_name": "Main sol. J1042", "provider_volume_ml": 1005, "locator": "$.data.solutions[0].recipe[0]", "source_row": {"recipe_order": 1, "compound": "Yeast extract", "compound_id": 16, "attribute": "BD-Difco", "amount": 2, "unit": "g", "g_l": 1.99005, "optional": 0}}, {"solution_id": 5101, "solution_name": "Main sol. J1042", "provider_volume_ml": 1005, "locator": "$.data.solutions[0].recipe[1]", "source_row": {"recipe_order": 2, "compound": "Tryptone", "compound_id": 71, "attribute": "BD-Difco", "amount": 2, "unit": "g", "g_l": 1.99005, "mmol_l": 27.9973, "optional": 0}}, {"solution_id": 5101, "solution_name": "Main sol. J1042", "provider_volume_ml": 1005, "locator": "$.data.solutions[0].recipe[2]", "source_row": {"recipe_order": 3, "compound": "Sodium pyruvate", "compound_id": 438, "amount": 5, "unit": "g", "g_l": 4.97512, "mmol_l": 45.212, "optional": 0}}, {"solution_id": 5101, "solution_name": "Main sol. J1042", "provider_volume_ml": 1005, "locator": "$.data.solutions[0].recipe[3]", "source_row": {"recipe_order": 4, "compound": "PIPES", "compound_id": 398, "amount": 3.46, "unit": "g", "g_l": 3.44279, "mmol_l": 11.3849, "optional": 0}}, {"solution_id": 5101, "solution_name": "Main sol. J1042", "provider_volume_ml": 1005, "locator": "$.data.solutions[0].recipe[4]", "source_row": {"recipe_order": 5, "solution": "Trace vitamins", "solution_id": 3861, "amount": 5, "unit": "ml", "optional": 0}}, {"solution_id": 5101, "solution_name": "Main sol. J1042", "provider_volume_ml": 1005, "locator": "$.data.solutions[0].recipe[5]", "source_row": {"recipe_order": 6, "solution": "Artificial seawater", "solution_id": 5102, "amount": 1000, "unit": "ml", "optional": 0}}, {"solution_id": 5102, "solution_name": "Artificial seawater", "provider_volume_ml": 1005, "locator": "$.data.solutions[1].recipe[0]", "source_row": {"recipe_order": 1, "compound": "NaCl", "compound_id": 43, "amount": 22, "unit": "g", "g_l": 21.8905, "mmol_l": 374.582, "optional": 0}}, {"solution_id": 5102, "solution_name": "Artificial seawater", "provider_volume_ml": 1005, "locator": "$.data.solutions[1].recipe[1]", "source_row": {"recipe_order": 2, "compound": "MgCl2 x 6 H2O", "compound_id": 79, "amount": 3, "unit": "g", "g_l": 2.98507, "mmol_l": 14.6829, "optional": 0}}, {"solution_id": 5102, "solution_name": "Artificial seawater", "provider_volume_ml": 1005, "locator": "$.data.solutions[1].recipe[2]", "source_row": {"recipe_order": 3, "compound": "MgSO4 x 7 H2O", "compound_id": 8, "amount": 6, "unit": "g", "g_l": 5.97015, "mmol_l": 24.222, "optional": 0}}, {"solution_id": 5102, "solution_name": "Artificial seawater", "provider_volume_ml": 1005, "locator": "$.data.solutions[1].recipe[3]", "source_row": {"recipe_order": 4, "compound": "(NH4)2SO4", "compound_id": 27, "amount": 1, "unit": "g", "g_l": 0.995025, "mmol_l": 7.53008, "optional": 0}}, {"solution_id": 5102, "solution_name": "Artificial seawater", "provider_volume_ml": 1005, "locator": "$.data.solutions[1].recipe[4]", "source_row": {"recipe_order": 5, "compound": "NaHCO3", "compound_id": 55, "amount": 0.2, "unit": "g", "g_l": 0.199005, "mmol_l": 2.36891, "optional": 0}}, {"solution_id": 5102, "solution_name": "Artificial seawater", "provider_volume_ml": 1005, "locator": "$.data.solutions[1].recipe[5]", "source_row": {"recipe_order": 6, "compound": "CaCl2 x 2 H2O", "compound_id": 7, "amount": 0.3, "unit": "g", "g_l": 0.298507, "mmol_l": 2.03046, "optional": 0}}, {"solution_id": 5102, "solution_name": "Artificial seawater", "provider_volume_ml": 1005, "locator": "$.data.solutions[1].recipe[6]", "source_row": {"recipe_order": 7, "compound": "KCl", "compound_id": 61, "amount": 0.5, "unit": "g", "g_l": 0.497512, "mmol_l": 6.67354, "optional": 0}}, {"solution_id": 5102, "solution_name": "Artificial seawater", "provider_volume_ml": 1005, "locator": "$.data.solutions[1].recipe[7]", "source_row": {"recipe_order": 8, "compound": "KH2PO4", "compound_id": 11, "amount": 0.42, "unit": "g", "g_l": 0.41791, "mmol_l": 3.07093, "optional": 0}}, {"solution_id": 5102, "solution_name": "Artificial seawater", "provider_volume_ml": 1005, "locator": "$.data.solutions[1].recipe[8]", "source_row": {"recipe_order": 9, "compound": "NaBr", "compound_id": 353, "amount": 0.05, "unit": "g", "g_l": 0.0497512, "mmol_l": 0.483538, "optional": 0}}, {"solution_id": 5102, "solution_name": "Artificial seawater", "provider_volume_ml": 1005, "locator": "$.data.solutions[1].recipe[9]", "source_row": {"recipe_order": 10, "compound": "SrCl2 x 6 H2O", "compound_id": 176, "amount": 0.02, "unit": "g", "g_l": 0.0199005, "mmol_l": 0.0746408, "optional": 0}}, {"solution_id": 5102, "solution_name": "Artificial seawater", "provider_volume_ml": 1005, "locator": "$.data.solutions[1].recipe[10]", "source_row": {"recipe_order": 11, "compound": "Ammonium ferric citrate", "compound_id": 2007, "amount": 0.01, "unit": "g", "g_l": 0.00995025, "optional": 0}}, {"solution_id": 5102, "solution_name": "Artificial seawater", "provider_volume_ml": 1005, "locator": "$.data.solutions[1].recipe[11]", "source_row": {"recipe_order": 12, "solution": "Trace minerals", "solution_id": 3804, "amount": 5, "unit": "ml", "optional": 0}}, {"solution_id": 5102, "solution_name": "Artificial seawater", "provider_volume_ml": 1005, "locator": "$.data.solutions[1].recipe[12]", "source_row": {"recipe_order": 13, "compound": "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional": 0}}, {"solution_id": 3861, "solution_name": "Trace vitamins", "provider_volume_ml": 1000, "locator": "$.data.solutions[2].recipe[0]", "source_row": {"recipe_order": 1, "compound": "Biotin", "compound_id": 46, "amount": 2, "unit": "mg", "g_l": 0.002, "mmol_l": 0.00818632, "optional": 0}}, {"solution_id": 3861, "solution_name": "Trace vitamins", "provider_volume_ml": 1000, "locator": "$.data.solutions[2].recipe[1]", "source_row": {"recipe_order": 2, "compound": "Folic acid", "compound_id": 138, "amount": 2, "unit": "mg", "g_l": 0.002, "mmol_l": 0.00453104, "optional": 0}}, {"solution_id": 3861, "solution_name": "Trace vitamins", "provider_volume_ml": 1000, "locator": "$.data.solutions[2].recipe[2]", "source_row": {"recipe_order": 3, "compound": "Pyridoxine hydrochloride", "compound_id": 519, "amount": 10, "unit": "mg", "g_l": 0.01, "mmol_l": 0.0486287, "optional": 0}}, {"solution_id": 3861, "solution_name": "Trace vitamins", "provider_volume_ml": 1000, "locator": "$.data.solutions[2].recipe[3]", "source_row": {"recipe_order": 4, "compound": "Thiamine HCl", "compound_id": 1207, "amount": 5, "unit": "mg", "g_l": 0.005, "mmol_l": 0.0148236, "optional": 0}}, {"solution_id": 3861, "solution_name": "Trace vitamins", "provider_volume_ml": 1000, "locator": "$.data.solutions[2].recipe[4]", "source_row": {"recipe_order": 5, "compound": "Riboflavin", "compound_id": 136, "amount": 5, "unit": "mg", "g_l": 0.005, "mmol_l": 0.0132837, "optional": 0}}, {"solution_id": 3861, "solution_name": "Trace vitamins", "provider_volume_ml": 1000, "locator": "$.data.solutions[2].recipe[5]", "source_row": {"recipe_order": 6, "compound": "Nicotinic acid", "compound_id": 139, "amount": 5, "unit": "mg", "g_l": 0.005, "mmol_l": 0.0406141, "optional": 0}}, {"solution_id": 3861, "solution_name": "Trace vitamins", "provider_volume_ml": 1000, "locator": "$.data.solutions[2].recipe[6]", "source_row": {"recipe_order": 7, "compound": "Calcium pantothenate", "compound_id": 518, "amount": 5, "unit": "mg", "g_l": 0.005, "mmol_l": 0.0104925, "optional": 0}}, {"solution_id": 3861, "solution_name": "Trace vitamins", "provider_volume_ml": 1000, "locator": "$.data.solutions[2].recipe[7]", "source_row": {"recipe_order": 8, "compound": "Vitamin B12", "compound_id": 18, "amount": 0.1, "unit": "mg", "g_l": 0.0001, "mmol_l": 7.3779e-05, "optional": 0}}, {"solution_id": 3861, "solution_name": "Trace vitamins", "provider_volume_ml": 1000, "locator": "$.data.solutions[2].recipe[8]", "source_row": {"recipe_order": 9, "compound": "p-Aminobenzoic acid", "compound_id": 47, "amount": 5, "unit": "mg", "g_l": 0.005, "mmol_l": 0.0364591, "optional": 0}}, {"solution_id": 3861, "solution_name": "Trace vitamins", "provider_volume_ml": 1000, "locator": "$.data.solutions[2].recipe[9]", "source_row": {"recipe_order": 10, "compound": "Lipoic acid", "compound_id": 368, "amount": 5, "unit": "mg", "g_l": 0.005, "mmol_l": 0.024233, "optional": 0}}, {"solution_id": 3861, "solution_name": "Trace vitamins", "provider_volume_ml": 1000, "locator": "$.data.solutions[2].recipe[10]", "source_row": {"recipe_order": 11, "compound": "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional": 0}}, {"solution_id": 3804, "solution_name": "Trace minerals", "provider_volume_ml": 1000, "locator": "$.data.solutions[3].recipe[0]", "source_row": {"recipe_order": 1, "compound": "Nitrilotriacetic acid", "compound_id": 189, "amount": 1.5, "unit": "g", "g_l": 1.5, "mmol_l": 7.84765, "optional": 0}}, {"solution_id": 3804, "solution_name": "Trace minerals", "provider_volume_ml": 1000, "locator": "$.data.solutions[3].recipe[1]", "source_row": {"recipe_order": 2, "compound": "MgSO4 x 7 H2O", "compound_id": 8, "amount": 3, "unit": "g", "g_l": 3, "mmol_l": 12.1716, "optional": 0}}, {"solution_id": 3804, "solution_name": "Trace minerals", "provider_volume_ml": 1000, "locator": "$.data.solutions[3].recipe[2]", "source_row": {"recipe_order": 3, "compound": "MnSO4 x n H2O", "compound_id": 1000, "amount": 0.5, "unit": "g", "g_l": 0.5, "optional": 0}}, {"solution_id": 3804, "solution_name": "Trace minerals", "provider_volume_ml": 1000, "locator": "$.data.solutions[3].recipe[3]", "source_row": {"recipe_order": 4, "compound": "NaCl", "compound_id": 43, "amount": 1, "unit": "g", "g_l": 1, "mmol_l": 17.1116, "optional": 0}}, {"solution_id": 3804, "solution_name": "Trace minerals", "provider_volume_ml": 1000, "locator": "$.data.solutions[3].recipe[4]", "source_row": {"recipe_order": 5, "compound": "FeSO4 x 7 H2O", "compound_id": 12, "amount": 0.1, "unit": "g", "g_l": 0.1, "mmol_l": 0.359693, "optional": 0}}, {"solution_id": 3804, "solution_name": "Trace minerals", "provider_volume_ml": 1000, "locator": "$.data.solutions[3].recipe[5]", "source_row": {"recipe_order": 6, "compound": "CoSO4 x 7 H2O", "compound_id": 198, "amount": 0.1, "unit": "g", "g_l": 0.1, "mmol_l": 0.645178, "optional": 0}}, {"solution_id": 3804, "solution_name": "Trace minerals", "provider_volume_ml": 1000, "locator": "$.data.solutions[3].recipe[6]", "source_row": {"recipe_order": 7, "compound": "CaCl2 x 2 H2O", "compound_id": 7, "amount": 0.1, "unit": "g", "g_l": 0.1, "mmol_l": 0.680203, "optional": 0}}, {"solution_id": 3804, "solution_name": "Trace minerals", "provider_volume_ml": 1000, "locator": "$.data.solutions[3].recipe[7]", "source_row": {"recipe_order": 8, "compound": "ZnSO4 x 7 H2O", "compound_id": 35, "amount": 0.1, "unit": "g", "g_l": 0.1, "mmol_l": 0.347752, "optional": 0}}, {"solution_id": 3804, "solution_name": "Trace minerals", "provider_volume_ml": 1000, "locator": "$.data.solutions[3].recipe[8]", "source_row": {"recipe_order": 9, "compound": "CuSO4 x 5 H2O", "compound_id": 121, "amount": 0.01, "unit": "g", "g_l": 0.01, "mmol_l": 0.0400503, "optional": 0}}, {"solution_id": 3804, "solution_name": "Trace minerals", "provider_volume_ml": 1000, "locator": "$.data.solutions[3].recipe[9]", "source_row": {"recipe_order": 10, "compound": "AlK(SO4)2", "compound_id": 1015, "amount": 0.01, "unit": "g", "g_l": 0.01, "mmol_l": 0.0387289, "optional": 0}}, {"solution_id": 3804, "solution_name": "Trace minerals", "provider_volume_ml": 1000, "locator": "$.data.solutions[3].recipe[10]", "source_row": {"recipe_order": 11, "compound": "H3BO3", "compound_id": 37, "amount": 0.01, "unit": "g", "g_l": 0.01, "mmol_l": 0.161708, "optional": 0}}, {"solution_id": 3804, "solution_name": "Trace minerals", "provider_volume_ml": 1000, "locator": "$.data.solutions[3].recipe[11]", "source_row": {"recipe_order": 12, "compound": "Na2MoO4 x 2 H2O", "compound_id": 9, "amount": 0.01, "unit": "g", "g_l": 0.01, "mmol_l": 0.0413309, "optional": 0}}, {"solution_id": 3804, "solution_name": "Trace minerals", "provider_volume_ml": 1000, "locator": "$.data.solutions[3].recipe[12]", "source_row": {"recipe_order": 13, "compound": "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional": 0}}], "source_only_notes": ["Trace minerals contains12 solutes plus water1 L and unquantified KOH; retain pH6.5 dissolution then7.0 adjustment at this stock stage.", "Trace vitamins contains10 constituents plus water1 L; generic calcium pantothenate, B12 and lipoic-acid forms do not justify more specific stereochemical or vitamer claims.", "M1107 main pH7.0, N2 atmosphere, butyl rubber stoppers and autoclaving are supported. No incubation temperature, duration or strain-growth claim was extracted.", "M190-specific vitamin filtration underN2 is a dependency-context instruction; resolve its compatibility with M1107 autoclave prose before transferring it.", "Exclude the M142 parent recipe and10 ml receiving dose, M190 parent10 ml vitamin dose, parent pH6.8/N2-CO2, and M190 separate mineral formulation.", "MediaDive43 recipe rows are preserved as reported database context; g_l and mmol_l are not automatically independently verified final concentrations."]}

### Main medium, seawater and two stock definitions

representation: concern. Targets: CultureMech:007626.

Eleven seawater solutes are flattened into main ingredients; trace minerals is attached at the wrong receiving level and both references lack composition.

Main batch has four solute masses, vitamin-stock5 ml and prepared seawater1 L plus N2 handling. Seawater has11 solute masses, water1 L and trace-mineral stock5 ml. The mineral and vitamin tables define12 and10 solutes respectively. Do not sum same-name substances across stages or substitute JCM197’s different mineral stock. The local Unknown solution name defaults do not erase the meaningful preferred terms.

### Preparation, pH and condition boundaries

completeness: concern. Targets: CultureMech:007626.

Selected record and owner omit the available main preparation and pH7.0; gas is left as a VARIABLE ingredient.

Retain source order: pH7, distribute underN2, butyl rubber stoppers, autoclave. Main source gives no temperature/time. General121°C15 min notices on dependency pages are not automatically authority for unavailable JCM1042. Stock-mineral pH6.5→7 is separate. Vitamin filtration is contextual to M190 and needs explicit applicability review. LIQUID/COMPLEX/UNDEFINED align with the ungelling yeast/tryptone formulation; optional role and organism fields are not invented.

### Exact existing chemical identities and MIM linkage

grounding: supported. Targets: CultureMech:007626.

All14 distinct asserted CHEBI identifiers have current matching nonobsolete labels; nine existing secondary links agree with maintained resolver output.

[{"field": "ingredients[0]", "label": "Sodium pyruvate", "primary": {"id": "CHEBI:50144", "label": "sodium pyruvate"}, "secondary": {"id": "CHEBI:50144", "label": "sodium pyruvate"}, "legacy": null, "decision": {"query_label": "Sodium pyruvate", "identifier": "CHEBI:50144", "ontology_id": "CHEBI:50144", "mim_preferred_term": "Na-pyruvate", "matched_label": "Sodium Pyruvate", "match_type": "synonym", "mapping_status": "MAPPED", "ambiguity": "unique", "resolution_source": "mim_exact", "local_identifier": "CHEBI:50144", "source_compound_id": null, "reason": "trusted MIM label-index answer"}}, {"field": "ingredients[1]", "label": "PIPES", "primary": {"id": "CHEBI:39033", "label": "PIPES"}, "secondary": {"id": "CHEBI:39033", "label": "PIPES"}, "legacy": null, "decision": {"query_label": "PIPES", "identifier": "CHEBI:39033", "ontology_id": "CHEBI:39033", "mim_preferred_term": "PIPES", "matched_label": "PIPES", "match_type": "preferred_term", "mapping_status": "MAPPED", "ambiguity": "unique", "resolution_source": "mim_exact", "local_identifier": "CHEBI:39033", "source_compound_id": null, "reason": "trusted MIM label-index answer"}}, {"field": "ingredients[2]", "label": "Yeast extract (BD-Difco)", "primary": null, "secondary": null, "legacy": null, "decision": {"query_label": "Yeast extract (BD-Difco)", "identifier": "FOODON:03315426", "ontology_id": "FOODON:03315426", "mim_preferred_term": "Yeast extract", "matched_label": "Yeast extract (BD-Difco)", "match_type": "synonym", "mapping_status": "MAPPED", "ambiguity": "unique", "resolution_source": "mim_exact", "local_identifier": null, "source_compound_id": null, "reason": "trusted MIM label-index answer"}}, {"field": "ingredients[3]", "label": "Tryptone (BD-Difco)", "primary": null, "secondary": null, "legacy": null, "decision": {"query_label": "Tryptone (BD-Difco)", "identifier": "MICRO:0000182", "ontology_id": "MICRO:0000182", "mim_preferred_term": "Tryptone", "matched_label": "Tryptone (BD-Difco)", "match_type": "synonym", "mapping_status": "MAPPED", "ambiguity": "unique", "resolution_source": "mim_exact", "local_identifier": null, "source_compound_id": null, "reason": "trusted MIM label-index answer"}}, {"field": "ingredients[4]", "label": "Artificial seawater (see below)", "primary": null, "secondary": null, "legacy": null, "decision": {"query_label": "Artificial seawater (see below)", "identifier": "MICRO:0001715", "ontology_id": "MICRO:0001715", "mim_preferred_term": "Artificial seawater", "matched_label": "Artificial seawater (see below)", "match_type": "synonym", "mapping_status": "MAPPED", "ambiguity": "unique", "resolution_source": "mim_exact", "local_identifier": null, "source_compound_id": null, "reason": "trusted MIM label-index answer"}}, {"field": "ingredients[5]", "label": "N2", "primary": {"id": "CHEBI:17997", "label": "dinitrogen"}, "secondary": null, "legacy": null, "decision": {"query_label": "N2", "identifier": "CHEBI:17997", "ontology_id": "CHEBI:17997", "mim_preferred_term": "Nitrogen gas", "matched_label": "N2", "match_type": "synonym", "mapping_status": "MAPPED", "ambiguity": "unique", "resolution_source": "mim_exact", "local_identifier": "CHEBI:17997", "source_compound_id": null, "reason": "trusted MIM label-index answer"}}, {"field": "ingredients[6]", "label": "Distilled water", "primary": {"id": "CHEBI:15377", "label": "water"}, "secondary": {"id": "CHEBI:15377", "label": "water"}, "legacy": null, "decision": {"query_label": "Distilled water", "identifier": "CHEBI:15377", "ontology_id": "CHEBI:15377", "mim_preferred_term": "Distilled water", "matched_label": "Distilled water", "match_type": "preferred_term", "mapping_status": "MAPPED", "ambiguity": "unique", "resolution_source": "mim_exact", "local_identifier": "CHEBI:15377", "source_compound_id": null, "reason": "trusted MIM label-index answer"}}, {"field": "ingredients[7]", "label": "MgSO4・7H2O", "primary": {"id": "CHEBI:31795", "label": "magnesium sulfate heptahydrate"}, "secondary": null, "legacy": null, "decision": {"query_label": "MgSO4・7H2O", "identifier": "CHEBI:31795", "ontology_id": null, "mim_preferred_term": null, "matched_label": null, "match_type": null, "mapping_status": null, "ambiguity": null, "resolution_source": "local_fallback", "local_identifier": "CHEBI:31795", "source_compound_id": null, "reason": "label not found in pinned MIM index; retained local identity"}}, {"field": "ingredients[8]", "label": "NaCl", "primary": {"id": "CHEBI:26710", "label": "sodium chloride"}, "secondary": {"id": "CHEBI:26710", "label": "sodium chloride"}, "legacy": null, "decision": {"query_label": "NaCl", "identifier": "CHEBI:26710", "ontology_id": "CHEBI:26710", "mim_preferred_term": "NaCl", "matched_label": "NaCl", "match_type": "preferred_term", "mapping_status": "MAPPED", "ambiguity": "unique", "resolution_source": "mim_exact", "local_identifier": "CHEBI:26710", "source_compound_id": null, "reason": "trusted MIM label-index answer"}}, {"field": "ingredients[9]", "label": "CaCl2・2H2O", "primary": {"id": "CHEBI:86158", "label": "calcium chloride dihydrate"}, "secondary": null, "legacy": null, "decision": {"query_label": "CaCl2・2H2O", "identifier": "CHEBI:86158", "ontology_id": null, "mim_preferred_term": null, "matched_label": null, "match_type": null, "mapping_status": null, "ambiguity": null, "resolution_source": "local_fallback", "local_identifier": "CHEBI:86158", "source_compound_id": null, "reason": "label not found in pinned MIM index; retained local identity"}}, {"field": "ingredients[10]", "label": "KH2PO4", "primary": {"id": "CHEBI:63036", "label": "potassium dihydrogen phosphate"}, "secondary": {"id": "CHEBI:63036", "label": "potassium dihydrogen phosphate"}, "legacy": null, "decision": {"query_label": "KH2PO4", "identifier": "CHEBI:63036", "ontology_id": "CHEBI:63036", "mim_preferred_term": "KH2PO4", "matched_label": "KH2PO4", "match_type": "preferred_term", "mapping_status": "MAPPED", "ambiguity": "unique", "resolution_source": "mim_exact", "local_identifier": "CHEBI:63036", "source_compound_id": null, "reason": "trusted MIM label-index answer"}}, {"field": "ingredients[11]", "label": "MgCl2・6H2O", "primary": {"id": "CHEBI:86345", "label": "magnesium dichloride hexahydrate"}, "secondary": null, "legacy": null, "decision": {"query_label": "MgCl2・6H2O", "identifier": "CHEBI:86345", "ontology_id": "CHEBI:86345", "mim_preferred_term": "MgCl2 x 6 H2O", "matched_label": "MgCl2・6H2O", "match_type": "synonym", "mapping_status": "MAPPED", "ambiguity": "unique", "resolution_source": "mim_exact", "local_identifier": "CHEBI:86345", "source_compound_id": null, "reason": "trusted MIM label-index answer"}}, {"field": "ingredients[12]", "label": "KCl", "primary": {"id": "CHEBI:32588", "label": "potassium chloride"}, "secondary": {"id": "CHEBI:32588", "label": "potassium chloride"}, "legacy": null, "decision": {"query_label": "KCl", "identifier": "CHEBI:32588", "ontology_id": "CHEBI:32588", "mim_preferred_term": "KCl", "matched_label": "KCl", "match_type": "preferred_term", "mapping_status": "MAPPED", "ambiguity": "unique", "resolution_source": "mim_exact", "local_identifier": "CHEBI:32588", "source_compound_id": null, "reason": "trusted MIM label-index answer"}}, {"field": "ingredients[13]", "label": "NaHCO3", "primary": {"id": "CHEBI:32139", "label": "sodium hydrogencarbonate"}, "secondary": {"id": "CHEBI:32139", "label": "sodium hydrogencarbonate"}, "legacy": null, "decision": {"query_label": "NaHCO3", "identifier": "CHEBI:32139", "ontology_id": "CHEBI:32139", "mim_preferred_term": "NaHCO3", "matched_label": "NaHCO3", "match_type": "preferred_term", "mapping_status": "MAPPED", "ambiguity": "unique", "resolution_source": "mim_exact", "local_identifier": "CHEBI:32139", "source_compound_id": null, "reason": "trusted MIM label-index answer"}}, {"field": "ingredients[14]", "label": "(NH4)2SO4", "primary": {"id": "CHEBI:62946", "label": "ammonium sulfate"}, "secondary": {"id": "CHEBI:62946", "label": "ammonium sulfate"}, "legacy": null, "decision": {"query_label": "(NH4)2SO4", "identifier": "CHEBI:62946", "ontology_id": "CHEBI:62946", "mim_preferred_term": "(NH4)2SO4", "matched_label": "(NH4)2SO4", "match_type": "preferred_term", "mapping_status": "MAPPED", "ambiguity": "unique", "resolution_source": "mim_exact", "local_identifier": "CHEBI:62946", "source_compound_id": null, "reason": "trusted MIM label-index answer"}}, {"field": "ingredients[15]", "label": "NaBr", "primary": {"id": "CHEBI:63004", "label": "sodium bromide"}, "secondary": {"id": "CHEBI:63004", "label": "sodium bromide"}, "legacy": null, "decision": {"query_label": "NaBr", "identifier": "CHEBI:63004", "ontology_id": "CHEBI:63004", "mim_preferred_term": "NaBr", "matched_label": "NaBr", "match_type": "preferred_term", "mapping_status": "MAPPED", "ambiguity": "unique", "resolution_source": "mim_exact", "local_identifier": "CHEBI:63004", "source_compound_id": null, "reason": "trusted MIM label-index answer"}}, {"field": "ingredients[16]", "label": "SrCl2・6H2O", "primary": {"id": "CHEBI:36385", "label": "strontium dichloride hexahydrate"}, "secondary": null, "legacy": null, "decision": {"query_label": "SrCl2・6H2O", "identifier": "CHEBI:36385", "ontology_id": "CHEBI:36385", "mim_preferred_term": "SrCl2 x 6 H2O", "matched_label": "SrCl2・6H2O", "match_type": "synonym", "mapping_status": "MAPPED", "ambiguity": "unique", "resolution_source": "mim_exact", "local_identifier": "CHEBI:36385", "source_compound_id": null, "reason": "trusted MIM label-index answer"}}, {"field": "ingredients[17]", "label": "Ammonium Fe(III) citrate", "primary": null, "secondary": null, "legacy": null, "decision": {"query_label": "Ammonium Fe(III) citrate", "identifier": null, "ontology_id": null, "mim_preferred_term": null, "matched_label": null, "match_type": null, "mapping_status": null, "ambiguity": null, "resolution_source": "not_found", "local_identifier": null, "source_compound_id": null, "reason": "label not found in pinned MIM index and no usable local identity"}}]
Primary hydrate repairs are credited. MgSO4・7H2O and CaCl2・2H2O use local fallbacks because these exact written labels are not in the pinned index; fallback does not invalidate their separately verified CHEBI identities. Ammonium Fe(III) citrate remains unresolved. FOODON/MICRO resolver outputs for mixtures are observations, not externally verified new grounding proposals. PIPES authority object is sparse; no additional chemical-form precision is claimed.

### Current writer and historical evidence assessment

provenance: concern. Targets: CultureMech:007626.

Current importer preview improves stock separation but still leaves name-resolution, denominator and pH extraction gaps.

Pure-method preview emits four main solutes plus unquantifiedN2 and two stock additions. Artificial seawater (see below) fails exact matching to Artificial seawater, yielding empty composition. Raw5 ml becomes5 ML_PER_L despite unproved final volume. _extract_ph reads a top-level field while current meta.ph=7.0, returning empty conditions. Preparation prose is now retained by current extractor, but old owner/target lack it. Current improvements are credited without treating regeneration alone as sufficient. All45 October historical source-object/literal joins match the fresh J1042 API; both existing solution5101 claims match fresh bytes and digest. These joins do not authenticate historical retrieval times. Earlier claims that API main rates are underconcentrated or that raw batch masses automatically mean per-litre values are not adopted. Sibling NaCl/MgSO4/CaCl2 sums mix separate solution bases; sibling identity alone is no authority to merge. No historical review is treated as structured coverage or silently closed.

## Findings

### F1: Liquid batch inputs use mass units and other rate bases are unproved

major / open / confirmed; issue key: CM007626-quantity-dimension-basis.

Two1 L liquid inputs and two5 ml stock doses are G_PER_L in both records. The four main masses also lack an explicit final-litre basis. Preserve exact batch amounts and distinguish database-reported normalized values from independent final-volume evidence.

### F2: Seawater and referenced stocks lose their preparation stages

major / open / confirmed; issue key: CM007626-stock-topology.

Eleven seawater solutes are direct main ingredients, the trace-mineral dose sits at medium level, and both referenced definitions are empty. Current importer separates primary items but cannot match the see-below suffix to the local stock section.

### F3: Main preparation and pH are missing while nitrogen is a variable solute

major / open / confirmed; issue key: CM007626-preparation-gas-ph.

Recoverable main pH7.0, N2 distribution, butyl stoppers and autoclave instructions are absent. Preserve gas handling and separate stock pH steps. Current pH extractor misses meta.ph; review vitamin-specific dependency handling before transfer.

### F4: Selected recipe lacks scoped claim evidence and primary source remains unavailable

minor / open / confirmed; issue key: CM007626-claim-provenance.

TOGO and MediaDive support bounded formula claims, and primary JCM pages support the two dependency definitions. The exact JCM1042 recipe is unavailable. Attach honest scoped provenance and retain prior history; do not label fallback data as directly inspected JCM1042.

## Recommended Actions And Acceptance Checks

### A1

Curate explicit batch amounts and correct quantity dimensions; repair source-transform denominator handling.

- Account for all40 local quantity fields and45 scoped source rows.
- Retain main vitamin5 ml, main seawater1 L, seawater water1 L and internal mineral5 ml as distinct inputs.
- Require explicit final-volume evidence before asserting per-litre rates; retain provider-reported API rates only with their declared solution basis.
- Do not use density, additive liquid volumes or historical recommendations to invent final concentrations; run the four native recipe checks.

### A2

Restore seawater and exact referenced mineral/vitamin definitions with distinct receiving stages.

- Account for11 seawater solutes,12 trace-mineral solutes and10 vitamins, plus their water and unquantified adjustment inputs.
- Resolve see-below local section naming without merging unrelated sections; preserve exact hydrate/generic-form distinctions.
- Do not import parent receiving doses, unrelated parent formulations or JCM197’s different mineral stock.
- Use supported schema representation; if nested batch doses cannot be represented losslessly, document the exact schema gap rather than flatten.

### A3

Restore main preparation and correctly extract source pH while separating gas and stock instructions.

- Retain pH7.0, N2 atmosphere, butyl rubber stoppers and autoclaving without invented time/temperature.
- Keep mineral pH6.5 then7.0 stock-scoped; assess vitamin filtration applicability explicitly.
- Keep N2 unquantified and preparation-scoped; do not invent solute concentration, pressure, incubation or growth.
- Test current payload meta.ph path and local-section behavior after an authorized writer fix; run schema, strict, terms and references.

### A4

Attach claim-level provenance, preserve append-only history and regenerate only from curated maintained inputs.

- Use ingredient evidence for supported ingredient claims and root evidence scoped to solution/preparation field paths.
- Distinguish current fallback recipe sources, directly inspected dependency primary sources and unavailable exact JCM1042; preserve real capture times.
- Retain June corrections and all earlier history without rewriting or guessing values; record new curation only under separate authorization.
- Respect formulation compatibility before any sibling reconciliation; run just verify-merges and just audit-merge-freshness after authorized regeneration.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| target | data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml; entire file | context_only | Entire generated record read:18 ingredient descriptors,2 empty named stock descriptors, source identifiers and13 history entries. |
| owner | data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml; entire file | context_only | Entire sole maintained TOGO owner read; generated scientific content retains the same18 ingredients and2 stock descriptors. |
| counterpart | data/normalized_yaml/bacterial/calroanaerobacter_medium.yaml; entire file | context_only | Entire separate CM002227 MediaDive record read as comparison context;34 direct descriptors include flattened stock constituents and three cross-stage sums. It is not an owner of the selected target. |
| solution5101-local | data/normalized_yaml/bacterial/mediadive_5101_Main_sol_J1042.yaml; entire file | context_only | Entire scoped main-solution record read. Its two pyruvate/PIPES source claims match fresh source objects and raw digest; its incomplete_composition flag remains appropriate. It is not an owner of this target. |
| registry | data/culturemech_id_registry.tsv; rows7624,2226,14011 | context_only | Exact CM007626,CM002227 andCM014013 maintained paths resolve. |
| importer | src/culturemech/import/togo_importer.py; _ingredient_from_item; _assembled_solution_sections; _extract_primary_components; _solution_from_item; _local_batch_volume_ml; _extract_preparation_steps; _extract_ph; convert | context_only | Current pure-method preview preserves primary versus stock layers but still assumes rate units, fails exact local stock-name match with see-below suffix and reads pH from the wrong payload level. |
| generator | src/culturemech/merge/merger.py; merge_group | context_only | Generated records are regenerated from maintained normalized inputs; do not hand-edit target. |
| formulation | src/culturemech/merge/formulation.py; formulation_content; merge_formulation_evidence | context_only | Scientific formulation and preparation must be compatible before any sibling union; common source identity alone does not justify merging. |
| schema | src/culturemech/schema/culturemech.yaml; MediaRecipe; IngredientDescriptor; SolutionDescriptor; PreparationStep; evidence | context_only | Use ingredient evidence and scoped root evidence for solution/preparation claims. SolutionDescriptor and PreparationStep have no nested evidence slot. |
| mim-index | src/culturemech/data/mediaingredientmech/label_index.csv; 18 exact preferred-label resolver decisions | context_only | Packaged maintained resolver used, retaining fallback and not-found outcomes. |
| mim-metadata | src/culturemech/data/mediaingredientmech/label_index.metadata.json; entire file | context_only | Pinned packaged snapshot provenance verified by maintained resolver load. |
| togo1107-api | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107; $.meta; $.components; $.comments | supports | Current TOGO M1107 explicitly identifies JCM_M1042; complete two-section recipe and main preparation read. Publication date not supplied; TOGO is the database author. Discovery used the existing source accession. |
| mediadiveJ1042 | https://mediadive.dsmz.de/rest/medium/J1042; $.data.medium; $.data.solutions[0:4] | supports | Full current MediaDive J1042 object read: main5101,seawater5102,vitamins3861,minerals3804. Provider-declared volume and g_l are solution-scoped; they are not independently measured final volumes. |
| togo142-api | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142; $.meta; $.components[2]; associated comments | supports | M142 identifies JCM151. Only its Trace minerals definition and associated dissolution/pH instructions are dependencies of M1107. Parent medium is excluded. |
| togo190-api | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190; $.meta; $.components[1]; vitamin-specific comment | supports | M190 identifies JCM197. Only its Trace vitamins definition is a dependency; vitamin-specific filtration/N2 handling is scoped to this source context and not automatically an override of M1107 autoclaving. |
| jcm151 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151; Trace minerals table and immediately following paragraph | supports | Current complete JCM151 page read; Trace minerals table confirms12 solutes,1 L water input and pH6.5 then7.0. JCM is author; copyright2026 is not a publication date. Unrelated parent medium, salt base, sulfur and sulfide instructions are excluded. |
| jcm197 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197; Trace vitamins table; vitamin-specific clause in main preparation | supports | Current complete JCM197 page read; Trace vitamins confirms10 vitamin masses and1 L water input. Parent formulation and different Trace mineral solution are excluded. JCM is author; publication date not supplied. |
| solution5101 | https://mediadive.dsmz.de/rest/solution/5101; $.data.volume; $.data.recipe[2:4] | supports | Fresh exact solution5101 bytes authenticate both existing scoped pyruvate/PIPES snippets and source digest. This credits those two claims, not the completeness of this separate record. |
| jcm1042 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1042; exact requested URL response | context_only | Exact primary JCM1042 CGI request returned HTTP200 with Nothing found. Recipe content remains unavailable. |
| jcm1042-pdf | https://www.jcm.riken.jp/media/no1042.pdf; exact requested URL response | context_only | Standard historical no1042.pdf candidate returned HTTP404 with an HTML error body; it is not a captured PDF. |
| togo1107 | https://togomedium.org/medium/M1107; exact requested URL response | context_only | TOGO browser page returned a JavaScript shell; usable recipe text was instead obtained from the structured API. |
| togo1107-api-q-0-0 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107; $.components[0].items[0] | supports | main solution 1: source amount=5 g; chemical form, water input, gas or adjustment role retained at this section only. |
| togo1107-api-q-0-1 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107; $.components[0].items[1] | supports | main solution 1: source amount=3.46 g; chemical form, water input, gas or adjustment role retained at this section only. |
| togo1107-api-q-0-2 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107; $.components[0].items[2] | supports | main solution 1: source amount=2 g; chemical form, water input, gas or adjustment role retained at this section only. |
| togo1107-api-q-0-3 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107; $.components[0].items[3] | supports | main solution 1: source amount=2 g; chemical form, water input, gas or adjustment role retained at this section only. |
| togo1107-api-q-0-4 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107; $.components[0].items[4] | supports | main solution 1: source amount=5 ml; chemical form, water input, gas or adjustment role retained at this section only. |
| togo1107-api-q-0-5 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107; $.components[0].items[5] | supports | main solution 1: source amount=1 L; chemical form, water input, gas or adjustment role retained at this section only. |
| togo1107-api-q-0-6 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107; $.components[0].items[6] | supports | main solution 1: source amount=None None; chemical form, water input, gas or adjustment role retained at this section only. |
| togo1107-api-q-1-0 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107; $.components[1].items[0] | supports | Artificial seawater: source amount=1 L; chemical form, water input, gas or adjustment role retained at this section only. |
| togo1107-api-q-1-1 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107; $.components[1].items[1] | supports | Artificial seawater: source amount=6 g; chemical form, water input, gas or adjustment role retained at this section only. |
| togo1107-api-q-1-2 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107; $.components[1].items[2] | supports | Artificial seawater: source amount=22 g; chemical form, water input, gas or adjustment role retained at this section only. |
| togo1107-api-q-1-3 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107; $.components[1].items[3] | supports | Artificial seawater: source amount=0.3 g; chemical form, water input, gas or adjustment role retained at this section only. |
| togo1107-api-q-1-4 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107; $.components[1].items[4] | supports | Artificial seawater: source amount=0.42 g; chemical form, water input, gas or adjustment role retained at this section only. |
| togo1107-api-q-1-5 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107; $.components[1].items[5] | supports | Artificial seawater: source amount=3 g; chemical form, water input, gas or adjustment role retained at this section only. |
| togo1107-api-q-1-6 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107; $.components[1].items[6] | supports | Artificial seawater: source amount=0.5 g; chemical form, water input, gas or adjustment role retained at this section only. |
| togo1107-api-q-1-7 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107; $.components[1].items[7] | supports | Artificial seawater: source amount=0.2 g; chemical form, water input, gas or adjustment role retained at this section only. |
| togo1107-api-q-1-8 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107; $.components[1].items[8] | supports | Artificial seawater: source amount=1 g; chemical form, water input, gas or adjustment role retained at this section only. |
| togo1107-api-q-1-9 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107; $.components[1].items[9] | supports | Artificial seawater: source amount=0.05 g; chemical form, water input, gas or adjustment role retained at this section only. |
| togo1107-api-q-1-10 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107; $.components[1].items[10] | supports | Artificial seawater: source amount=0.02 g; chemical form, water input, gas or adjustment role retained at this section only. |
| togo1107-api-q-1-11 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107; $.components[1].items[11] | supports | Artificial seawater: source amount=0.01 g; chemical form, water input, gas or adjustment role retained at this section only. |
| togo1107-api-q-1-12 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107; $.components[1].items[12] | supports | Artificial seawater: source amount=5 ml; chemical form, water input, gas or adjustment role retained at this section only. |
| togo142-api-q-2-0 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142; $.components[2].items[0] | supports | Trace minerals: source amount=1 L; chemical form, water input, gas or adjustment role retained at this section only. |
| togo142-api-q-2-1 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142; $.components[2].items[1] | supports | Trace minerals: source amount=3 g; chemical form, water input, gas or adjustment role retained at this section only. |
| togo142-api-q-2-2 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142; $.components[2].items[2] | supports | Trace minerals: source amount=1 g; chemical form, water input, gas or adjustment role retained at this section only. |
| togo142-api-q-2-3 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142; $.components[2].items[3] | supports | Trace minerals: source amount=0.1 g; chemical form, water input, gas or adjustment role retained at this section only. |
| togo142-api-q-2-4 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142; $.components[2].items[4] | supports | Trace minerals: source amount=0.01 g; chemical form, water input, gas or adjustment role retained at this section only. |
| togo142-api-q-2-5 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142; $.components[2].items[5] | supports | Trace minerals: source amount=0.01 g; chemical form, water input, gas or adjustment role retained at this section only. |
| togo142-api-q-2-6 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142; $.components[2].items[6] | supports | Trace minerals: source amount=0.1 g; chemical form, water input, gas or adjustment role retained at this section only. |
| togo142-api-q-2-7 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142; $.components[2].items[7] | supports | Trace minerals: source amount=0.1 g; chemical form, water input, gas or adjustment role retained at this section only. |
| togo142-api-q-2-8 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142; $.components[2].items[8] | supports | Trace minerals: source amount=0.01 g; chemical form, water input, gas or adjustment role retained at this section only. |
| togo142-api-q-2-9 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142; $.components[2].items[9] | supports | Trace minerals: source amount=0.1 g; chemical form, water input, gas or adjustment role retained at this section only. |
| togo142-api-q-2-10 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142; $.components[2].items[10] | supports | Trace minerals: source amount=1.5 g; chemical form, water input, gas or adjustment role retained at this section only. |
| togo142-api-q-2-11 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142; $.components[2].items[11] | supports | Trace minerals: source amount=0.5 g; chemical form, water input, gas or adjustment role retained at this section only. |
| togo142-api-q-2-12 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142; $.components[2].items[12] | supports | Trace minerals: source amount=0.01 g; chemical form, water input, gas or adjustment role retained at this section only. |
| togo142-api-q-2-13 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142; $.components[2].items[13] | supports | Trace minerals: source amount=None None; chemical form, water input, gas or adjustment role retained at this section only. |
| togo190-api-q-1-0 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190; $.components[1].items[0] | supports | Trace vitamins: source amount=1 L; chemical form, water input, gas or adjustment role retained at this section only. |
| togo190-api-q-1-1 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190; $.components[1].items[1] | supports | Trace vitamins: source amount=2 mg; chemical form, water input, gas or adjustment role retained at this section only. |
| togo190-api-q-1-2 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190; $.components[1].items[2] | supports | Trace vitamins: source amount=5 mg; chemical form, water input, gas or adjustment role retained at this section only. |
| togo190-api-q-1-3 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190; $.components[1].items[3] | supports | Trace vitamins: source amount=5 mg; chemical form, water input, gas or adjustment role retained at this section only. |
| togo190-api-q-1-4 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190; $.components[1].items[4] | supports | Trace vitamins: source amount=5 mg; chemical form, water input, gas or adjustment role retained at this section only. |
| togo190-api-q-1-5 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190; $.components[1].items[5] | supports | Trace vitamins: source amount=10 mg; chemical form, water input, gas or adjustment role retained at this section only. |
| togo190-api-q-1-6 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190; $.components[1].items[6] | supports | Trace vitamins: source amount=2 mg; chemical form, water input, gas or adjustment role retained at this section only. |
| togo190-api-q-1-7 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190; $.components[1].items[7] | supports | Trace vitamins: source amount=0.1 mg; chemical form, water input, gas or adjustment role retained at this section only. |
| togo190-api-q-1-8 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190; $.components[1].items[8] | supports | Trace vitamins: source amount=5 mg; chemical form, water input, gas or adjustment role retained at this section only. |
| togo190-api-q-1-9 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190; $.components[1].items[9] | supports | Trace vitamins: source amount=5 mg; chemical form, water input, gas or adjustment role retained at this section only. |
| togo190-api-q-1-10 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190; $.components[1].items[10] | supports | Trace vitamins: source amount=5 mg; chemical form, water input, gas or adjustment role retained at this section only. |
| chebi-15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; exact IRI term object | supports | CHEBI:15377 label=water; obsolete=False; supplied-form assessment uses the exact term object, not resolver agreement alone. |
| chebi-17997 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997; exact IRI term object | supports | CHEBI:17997 label=dinitrogen; obsolete=False; supplied-form assessment uses the exact term object, not resolver agreement alone. |
| chebi-26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; exact IRI term object | supports | CHEBI:26710 label=sodium chloride; obsolete=False; supplied-form assessment uses the exact term object, not resolver agreement alone. |
| chebi-31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; exact IRI term object | supports | CHEBI:31795 label=magnesium sulfate heptahydrate; obsolete=False; supplied-form assessment uses the exact term object, not resolver agreement alone. |
| chebi-32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; exact IRI term object | supports | CHEBI:32139 label=sodium hydrogencarbonate; obsolete=False; supplied-form assessment uses the exact term object, not resolver agreement alone. |
| chebi-32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; exact IRI term object | supports | CHEBI:32588 label=potassium chloride; obsolete=False; supplied-form assessment uses the exact term object, not resolver agreement alone. |
| chebi-36385 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_36385; exact IRI term object | supports | CHEBI:36385 label=strontium dichloride hexahydrate; obsolete=False; supplied-form assessment uses the exact term object, not resolver agreement alone. |
| chebi-39033 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_39033; exact IRI term object | supports | CHEBI:39033 label=PIPES; obsolete=False; supplied-form assessment uses the exact term object, not resolver agreement alone. |
| chebi-50144 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_50144; exact IRI term object | supports | CHEBI:50144 label=sodium pyruvate; obsolete=False; supplied-form assessment uses the exact term object, not resolver agreement alone. |
| chebi-62946 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946; exact IRI term object | supports | CHEBI:62946 label=ammonium sulfate; obsolete=False; supplied-form assessment uses the exact term object, not resolver agreement alone. |
| chebi-63004 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63004; exact IRI term object | supports | CHEBI:63004 label=sodium bromide; obsolete=False; supplied-form assessment uses the exact term object, not resolver agreement alone. |
| chebi-63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; exact IRI term object | supports | CHEBI:63036 label=potassium dihydrogen phosphate; obsolete=False; supplied-form assessment uses the exact term object, not resolver agreement alone. |
| chebi-86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; exact IRI term object | supports | CHEBI:86158 label=calcium chloride dihydrate; obsolete=False; supplied-form assessment uses the exact term object, not resolver agreement alone. |
| chebi-86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; exact IRI term object | supports | CHEBI:86345 label=magnesium dichloride hexahydrate; obsolete=False; supplied-form assessment uses the exact term object, not resolver agreement alone. |
| historical-1 | reports/ingredient_concentration_curation/20261007-mediadive-media-3000-3319/records/bacterial/calroanaerobacter_medium.yaml.md; entire file | context_only | Historical context read completely, with repeated tables compared losslessly. Not native coverage. Earlier final-litre recommendations and blanket stock conflicts are reassessed against current scoped source amounts. |
| historical-2 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.md; entire file | context_only | Historical context read completely, with repeated tables compared losslessly. Not native coverage. Earlier final-litre recommendations and blanket stock conflicts are reassessed against current scoped source amounts. |
| historical-3 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/calroanaerobacter_medium__375948ba.md; entire file | context_only | Historical context read completely, with repeated tables compared losslessly. Not native coverage. Earlier final-litre recommendations and blanket stock conflicts are reassessed against current scoped source amounts. |
| historical-4 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.md; entire file | context_only | Historical context read completely, with repeated tables compared losslessly. Not native coverage. Earlier final-litre recommendations and blanket stock conflicts are reassessed against current scoped source amounts. |
| historical-5 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/calroanaerobacter_medium.md; entire file | context_only | Historical context read completely, with repeated tables compared losslessly. Not native coverage. Earlier final-litre recommendations and blanket stock conflicts are reassessed against current scoped source amounts. |
| historical-6 | reports/yaml_record_review/20260922T025827Z-CALROANAEROBACTER_MEDIUM.md; entire file | context_only | Historical context read completely, with repeated tables compared losslessly. Not native coverage. Earlier final-litre recommendations and blanket stock conflicts are reassessed against current scoped source amounts. |
| historical-7 | reports/yaml_record_review/20260922T025936Z-calroanaerobacter_medium__375948ba.md; entire file | context_only | Historical context read completely, with repeated tables compared losslessly. Not native coverage. Earlier final-litre recommendations and blanket stock conflicts are reassessed against current scoped source amounts. |
| diagnostics | REVIEW_WORK/batch058/record10/diagnostics.json; entire file | context_only | Read-only maintained resolver and importer previews,47 exact source-object/literal joins, registry and ignored-inclusive local search. |
| ownership-search | REVIEW_WORK/batch058/record10/diagnostics.json; ownership_search.argv/stdout | context_only | Exact maintained source/counterpart and report leads found. No claim to have read every queue/archive hit. |
| validate-schema | REVIEW_WORK/batch058/record10/validate-schema-result.json; full argv/stdout/stderr | context_only | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | REVIEW_WORK/batch058/record10/validate-strict-result.json; full argv/stdout/stderr | context_only | Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                REVIEW_WORK/batch058/record10/strict.tsv |
| validate-terms | REVIEW_WORK/batch058/record10/validate-terms-result.json; full argv/stdout/stderr | context_only | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | REVIEW_WORK/batch058/record10/validate-references-result.json; full argv/stdout/stderr | context_only | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |

## Limits And Additional Notes

- Exact JCM1042 CGI returns Nothing found and historical PDF candidate returns404. Current TOGO/MediaDive recipe evidence is explicitly secondary; JCM151/197 primary evidence is scoped to referenced stocks.
- No final mixed volume, density, molarity or stock contribution was inferred from input liquid volumes. Database g_l and mmol_l fields are retained as reported context, not blanket chemical or arithmetic endorsement.
- All14 asserted CHEBI identities were checked. New FOODON/MICRO resolver outputs for mixtures were not independently verified and are not new grounding proposals; ammonium ferric citrate remains unresolved.
- Canonical checks target only the selected generated record; owners/context files were read. Schema validity is not scientific accuracy. Full-corpus ID/product/merge gates and experiments were not rerun for this review-only addition.
- The source provides no strain-specific growth or incubation evidence. Source spelling alone is not an organism identification; vitamin dependency handling requires explicit applicability review.
- All scientific records remain unchanged; original native inspect source hashes and four check streams are retained.
- Seven historical reports were read with complete prose and source-row comparison;45 historical API objects and2 existing solution claims authenticate against fresh bytes. Historical access times are not independently authenticated.
- No prior structured finding is closed. Primary-source access limits remain explicit despite successful deterministic checks.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T064332Z-calroanaerobacter-medium-batch058
kind: record
repository: CultureBotAI/CultureMech
title: 'Calroanaerobacter medium: batch quantities and nested stock scope'
started_at: '2026-10-28T06:07:45.569258Z'
finished_at: '2026-10-28T06:43:32.084231Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  independence: independent
  independence_basis: Reviewer did not author or modify the assessed scientific records;
    exact source/input review without experimental validation.
skill: review-yaml-record
completion: partial
verdict: needs_curation
scientific_review: true
summary: TOGO M1107/JCM1042 identity and four native checks are supported. Three major
  findings concern quantity dimensions/bases, stock stages and missing preparation;
  one minor finding concerns claim provenance. Exact primary JCM1042 recipe remains
  unavailable; primary stock definitions and current database recipe are inspected.
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
  - path: AGENTS.md
    sha256: 72737a531548de8636bcf70b972e71a7630a0e579215b6ded392d88d1b51a4fc
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
  - path: data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml
    sha256: 173478ce1519f36741eff6c926a307c8a5095e67e306e73f9a6a9017a37f3d1e
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml
    sha256: bde8b700b19a68dfb5f2f3518418ff9ae8942a9f20f9790cc0d55134fe458a15
    role: context
  - path: data/normalized_yaml/bacterial/calroanaerobacter_medium.yaml
    sha256: 38951047083adfc56aecc7553be541d685957e591a05832cb357b991b26e9a91
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_5101_Main_sol_J1042.yaml
    sha256: 446db5da8e2051fe3de99b2fc237d90b525fc76aa9be20441da6d4a1e73e2323
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-3000-3319/records/bacterial/calroanaerobacter_medium.yaml.md
    sha256: ffffbf7f19bdf3381f29e73baa536f5d951ab6f75b20b6cb670db79b5e0abcf5
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.md
    sha256: 037fb7d4630684ddc05c87ccd579fe643a15f0b7ef3ae3ef74fbf32d52b6cdcb
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/calroanaerobacter_medium__375948ba.md
    sha256: 18d73dd6b5f71b1e171c08b78f105ab0e3cf3581c00f8c040ea533cef1d648ea
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.md
    sha256: 94fdeee68e2b717c45c832adbaf7f2786039e4f1e572fca49b0ec05188c0739b
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/calroanaerobacter_medium.md
    sha256: 73dbd5c625347aebfcf7cd852fd1b25856af3c53f1342b56e120fa49b99252f8
    role: context
  - path: reports/yaml_record_review/20260922T025827Z-CALROANAEROBACTER_MEDIUM.md
    sha256: 1f3722c06153cc1e26ab51a97edc3c8b2e7a17032d2cf69d797d1da0dc4f6f62
    role: context
  - path: reports/yaml_record_review/20260922T025936Z-calroanaerobacter_medium__375948ba.md
    sha256: b90f3c1a08321ea6e9ffb5abb53c96fd6c17c993ee277ed5b73491675b4471e4
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
  - path: scripts/promote_komodo_volume_candidates.py
    sha256: 2423b7e2e04011b31d21eac939714a2db4380f033a69094325dc567e44929cd2
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/resolve_komodo_compositions.py
    sha256: f45bc52a8efaa66c9a93c109a40c7d2763ac9f49c9009d92a4c0a0a41b7c28da
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
  - path: src/culturemech/merge/merge_recipes.py
    sha256: ce00a4b4e0bc2fa9a63e8b33f4a591cb20984569e125d395af40f5b7e84766a7
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
  description: One entire selected generated record and sole maintained owner;40 local
    concentration fields,45 scoped TOGO items and43 corroborating API recipe rows;
    exact existing chemical IDs, history and current writer. Separate MediaDive counterpart
    and solution5101 are limited comparison context.
  selection: Batch058 item10; Python-sorted uncovered paths from successful native
    lists; covered503 of6325 at selection; base9ea7ff33d354e37b791df96a880005153e446ce3.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:007626
  exclusions:
  - target: Other media, parent recipe formulations and organism/strain growth
    reason: Dependency references transfer only the named stock definitions; other
      target records and experimental claims are outside this review.
targets:
- target_id: CultureMech:007626
  path: data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml
  label: CALROANAEROBACTER MEDIUM
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml
    role: maintained normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merger.py
    role: generated merge implementation
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:007626
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml
    --out REVIEW_WORK/batch058/record10/strict.tsv --workers 1
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         REVIEW_WORK/batch058/record10/strict.tsv"
  target_ids:
  - CultureMech:007626
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:007626
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:007626
  evidence_ids:
  - validate-references
- check_id: embedded-history
  name: Manual embedded history assessment
  required: false
  status: passed
  summary: All embedded history read. June primary heptahydrate and nine secondary-link
    repairs are credited; no timestamps repaired or events appended. Standalone history-tree
    validator does not validate these embedded entries.
  target_ids:
  - CultureMech:007626
  evidence_ids:
  - target
  - owner
evidence:
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml
  accessed_at: '2026-10-28T06:19:10.753399Z'
  support: context_only
  summary: Entire generated record read:18 ingredient descriptors,2 empty named stock
    descriptors, source identifiers and13 history entries.
  locator: entire file
  snapshot_sha256: 173478ce1519f36741eff6c926a307c8a5095e67e306e73f9a6a9017a37f3d1e
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml
  accessed_at: '2026-10-28T06:19:10.753399Z'
  support: context_only
  summary: Entire sole maintained TOGO owner read; generated scientific content retains
    the same18 ingredients and2 stock descriptors.
  locator: entire file
  snapshot_sha256: bde8b700b19a68dfb5f2f3518418ff9ae8942a9f20f9790cc0d55134fe458a15
- evidence_id: counterpart
  kind: record_content
  reference: data/normalized_yaml/bacterial/calroanaerobacter_medium.yaml
  accessed_at: '2026-10-28T06:19:10.753399Z'
  support: context_only
  summary: Entire separate CM002227 MediaDive record read as comparison context;34
    direct descriptors include flattened stock constituents and three cross-stage
    sums. It is not an owner of the selected target.
  locator: entire file
  snapshot_sha256: 38951047083adfc56aecc7553be541d685957e591a05832cb357b991b26e9a91
- evidence_id: solution5101-local
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_5101_Main_sol_J1042.yaml
  accessed_at: '2026-10-28T06:19:10.753399Z'
  support: context_only
  summary: Entire scoped main-solution record read. Its two pyruvate/PIPES source
    claims match fresh source objects and raw digest; its incomplete_composition flag
    remains appropriate. It is not an owner of this target.
  locator: entire file
  snapshot_sha256: 446db5da8e2051fe3de99b2fc237d90b525fc76aa9be20441da6d4a1e73e2323
- evidence_id: registry
  kind: record_content
  reference: data/culturemech_id_registry.tsv
  accessed_at: '2026-10-28T06:19:10.753399Z'
  support: context_only
  summary: Exact CM007626,CM002227 andCM014013 maintained paths resolve.
  locator: rows7624,2226,14011
  snapshot_sha256: 0d059720f5c474b63daff8d5010fc56942a5a3ac30761ee75ce9e84801d555a5
- evidence_id: importer
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  accessed_at: '2026-10-28T06:19:10.753399Z'
  support: context_only
  summary: Current pure-method preview preserves primary versus stock layers but still
    assumes rate units, fails exact local stock-name match with see-below suffix and
    reads pH from the wrong payload level.
  locator: _ingredient_from_item; _assembled_solution_sections; _extract_primary_components;
    _solution_from_item; _local_batch_volume_ml; _extract_preparation_steps; _extract_ph;
    convert
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: generator
  kind: record_content
  reference: src/culturemech/merge/merger.py
  accessed_at: '2026-10-28T06:19:10.753399Z'
  support: context_only
  summary: Generated records are regenerated from maintained normalized inputs; do
    not hand-edit target.
  locator: merge_group
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  accessed_at: '2026-10-28T06:19:10.753399Z'
  support: context_only
  summary: Scientific formulation and preparation must be compatible before any sibling
    union; common source identity alone does not justify merging.
  locator: formulation_content; merge_formulation_evidence
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: schema
  kind: record_content
  reference: src/culturemech/schema/culturemech.yaml
  accessed_at: '2026-10-28T06:19:10.753399Z'
  support: context_only
  summary: Use ingredient evidence and scoped root evidence for solution/preparation
    claims. SolutionDescriptor and PreparationStep have no nested evidence slot.
  locator: MediaRecipe; IngredientDescriptor; SolutionDescriptor; PreparationStep;
    evidence
  snapshot_sha256: 8551fa65e4e96f36847368641282948cffd393356648fd9fb6947831ab985fae
- evidence_id: mim-index
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  accessed_at: '2026-10-28T06:19:10.753399Z'
  support: context_only
  summary: Packaged maintained resolver used, retaining fallback and not-found outcomes.
  locator: 18 exact preferred-label resolver decisions
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-metadata
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  accessed_at: '2026-10-28T06:19:10.753399Z'
  support: context_only
  summary: Pinned packaged snapshot provenance verified by maintained resolver load.
  locator: entire file
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: togo1107-api
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107
  accessed_at: '2026-10-28T06:09:09.926734Z'
  support: supports
  summary: Current TOGO M1107 explicitly identifies JCM_M1042; complete two-section
    recipe and main preparation read. Publication date not supplied; TOGO is the database
    author. Discovery used the existing source accession.
  locator: $.meta; $.components; $.comments
  snapshot_sha256: a1ec3b432c2b60e3c3d92d73a6022246c4ad248683e4ce6e12cf039cef41bc09
- evidence_id: mediadiveJ1042
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J1042
  accessed_at: '2026-10-28T06:08:19.204710Z'
  support: supports
  summary: 'Full current MediaDive J1042 object read: main5101,seawater5102,vitamins3861,minerals3804.
    Provider-declared volume and g_l are solution-scoped; they are not independently
    measured final volumes.'
  locator: $.data.medium; $.data.solutions[0:4]
  snapshot_sha256: 08b1cbdcf629df497b0169ae985a5c6726e0dd35f84846d7b13bcfcb845ca90c
- evidence_id: togo142-api
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142
  accessed_at: '2026-10-28T06:09:37.082631Z'
  support: supports
  summary: M142 identifies JCM151. Only its Trace minerals definition and associated
    dissolution/pH instructions are dependencies of M1107. Parent medium is excluded.
  locator: $.meta; $.components[2]; associated comments
  snapshot_sha256: 610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33
- evidence_id: togo190-api
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190
  accessed_at: '2026-10-28T06:09:37.097083Z'
  support: supports
  summary: M190 identifies JCM197. Only its Trace vitamins definition is a dependency;
    vitamin-specific filtration/N2 handling is scoped to this source context and not
    automatically an override of M1107 autoclaving.
  locator: $.meta; $.components[1]; vitamin-specific comment
  snapshot_sha256: 61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528
- evidence_id: jcm151
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151
  accessed_at: '2026-10-28T06:09:49.581499Z'
  support: supports
  summary: Current complete JCM151 page read; Trace minerals table confirms12 solutes,1
    L water input and pH6.5 then7.0. JCM is author; copyright2026 is not a publication
    date. Unrelated parent medium, salt base, sulfur and sulfide instructions are
    excluded.
  locator: Trace minerals table and immediately following paragraph
  snapshot_sha256: 6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7
- evidence_id: jcm197
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197
  accessed_at: '2026-10-28T06:09:49.579312Z'
  support: supports
  summary: Current complete JCM197 page read; Trace vitamins confirms10 vitamin masses
    and1 L water input. Parent formulation and different Trace mineral solution are
    excluded. JCM is author; publication date not supplied.
  locator: Trace vitamins table; vitamin-specific clause in main preparation
  snapshot_sha256: 39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532
- evidence_id: solution5101
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/5101
  accessed_at: '2026-10-28T06:11:15.878758Z'
  support: supports
  summary: Fresh exact solution5101 bytes authenticate both existing scoped pyruvate/PIPES
    snippets and source digest. This credits those two claims, not the completeness
    of this separate record.
  locator: $.data.volume; $.data.recipe[2:4]
  snapshot_sha256: d379cc547f2ee1766a7bde160262b290376b833539433223ff8c490701fa2fab
- evidence_id: jcm1042
  kind: search
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1042
  accessed_at: '2026-10-28T06:08:19.407046Z'
  support: context_only
  summary: Exact primary JCM1042 CGI request returned HTTP200 with Nothing found.
    Recipe content remains unavailable.
  locator: exact requested URL response
  snapshot_sha256: 86a4befca853383b9751aaad787a21309218d1894e0f783fcd0c3f312ac24152
  search_scope: One exact accession-bound request. No claim of global source absence;
    fallback recipe evidence is separately attributed.
- evidence_id: jcm1042-pdf
  kind: search
  reference: https://www.jcm.riken.jp/media/no1042.pdf
  accessed_at: '2026-10-28T06:09:09.543100Z'
  support: context_only
  summary: Standard historical no1042.pdf candidate returned HTTP404 with an HTML
    error body; it is not a captured PDF.
  locator: exact requested URL response
  snapshot_sha256: 81328808599f42cf0913bb061fee2ee27ca61954b0eaae5647371a6667c73ac5
  search_scope: One exact accession-bound request. No claim of global source absence;
    fallback recipe evidence is separately attributed.
- evidence_id: togo1107
  kind: search
  reference: https://togomedium.org/medium/M1107
  accessed_at: '2026-10-28T06:08:19.010202Z'
  support: context_only
  summary: TOGO browser page returned a JavaScript shell; usable recipe text was instead
    obtained from the structured API.
  locator: exact requested URL response
  snapshot_sha256: 78669d85db93e40276577aaf5073aa0bc2420fe5b7be6212de5619e445da93aa
  search_scope: One exact accession-bound request. No claim of global source absence;
    fallback recipe evidence is separately attributed.
- evidence_id: togo1107-api-q-0-0
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107
  accessed_at: '2026-10-28T06:09:09.926734Z'
  support: supports
  summary: 'main solution 1: source amount=5 g; chemical form, water input, gas or
    adjustment role retained at this section only.'
  locator: $.components[0].items[0]
  snapshot_sha256: a1ec3b432c2b60e3c3d92d73a6022246c4ad248683e4ce6e12cf039cef41bc09
  quote: '"component_name": "Sodium pyruvate"'
- evidence_id: togo1107-api-q-0-1
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107
  accessed_at: '2026-10-28T06:09:09.926734Z'
  support: supports
  summary: 'main solution 1: source amount=3.46 g; chemical form, water input, gas
    or adjustment role retained at this section only.'
  locator: $.components[0].items[1]
  snapshot_sha256: a1ec3b432c2b60e3c3d92d73a6022246c4ad248683e4ce6e12cf039cef41bc09
  quote: '"component_name": "PIPES"'
- evidence_id: togo1107-api-q-0-2
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107
  accessed_at: '2026-10-28T06:09:09.926734Z'
  support: supports
  summary: 'main solution 1: source amount=2 g; chemical form, water input, gas or
    adjustment role retained at this section only.'
  locator: $.components[0].items[2]
  snapshot_sha256: a1ec3b432c2b60e3c3d92d73a6022246c4ad248683e4ce6e12cf039cef41bc09
  quote: '"component_name": "Yeast extract (BD-Difco)"'
- evidence_id: togo1107-api-q-0-3
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107
  accessed_at: '2026-10-28T06:09:09.926734Z'
  support: supports
  summary: 'main solution 1: source amount=2 g; chemical form, water input, gas or
    adjustment role retained at this section only.'
  locator: $.components[0].items[3]
  snapshot_sha256: a1ec3b432c2b60e3c3d92d73a6022246c4ad248683e4ce6e12cf039cef41bc09
  quote: '"component_name": "Tryptone (BD-Difco)"'
- evidence_id: togo1107-api-q-0-4
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107
  accessed_at: '2026-10-28T06:09:09.926734Z'
  support: supports
  summary: 'main solution 1: source amount=5 ml; chemical form, water input, gas or
    adjustment role retained at this section only.'
  locator: $.components[0].items[4]
  snapshot_sha256: a1ec3b432c2b60e3c3d92d73a6022246c4ad248683e4ce6e12cf039cef41bc09
  quote: '"component_name": "Trace vitamins (see Medium [M190])"'
- evidence_id: togo1107-api-q-0-5
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107
  accessed_at: '2026-10-28T06:09:09.926734Z'
  support: supports
  summary: 'main solution 1: source amount=1 L; chemical form, water input, gas or
    adjustment role retained at this section only.'
  locator: $.components[0].items[5]
  snapshot_sha256: a1ec3b432c2b60e3c3d92d73a6022246c4ad248683e4ce6e12cf039cef41bc09
  quote: '"component_name": "Artificial seawater (see below)"'
- evidence_id: togo1107-api-q-0-6
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107
  accessed_at: '2026-10-28T06:09:09.926734Z'
  support: supports
  summary: 'main solution 1: source amount=None None; chemical form, water input,
    gas or adjustment role retained at this section only.'
  locator: $.components[0].items[6]
  snapshot_sha256: a1ec3b432c2b60e3c3d92d73a6022246c4ad248683e4ce6e12cf039cef41bc09
  quote: '"component_name": "N2"'
- evidence_id: togo1107-api-q-1-0
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107
  accessed_at: '2026-10-28T06:09:09.926734Z'
  support: supports
  summary: 'Artificial seawater: source amount=1 L; chemical form, water input, gas
    or adjustment role retained at this section only.'
  locator: $.components[1].items[0]
  snapshot_sha256: a1ec3b432c2b60e3c3d92d73a6022246c4ad248683e4ce6e12cf039cef41bc09
  quote: '"component_name": "Distilled water"'
- evidence_id: togo1107-api-q-1-1
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107
  accessed_at: '2026-10-28T06:09:09.926734Z'
  support: supports
  summary: 'Artificial seawater: source amount=6 g; chemical form, water input, gas
    or adjustment role retained at this section only.'
  locator: $.components[1].items[1]
  snapshot_sha256: a1ec3b432c2b60e3c3d92d73a6022246c4ad248683e4ce6e12cf039cef41bc09
  quote: '"component_name": "MgSO4・7H2O"'
- evidence_id: togo1107-api-q-1-2
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107
  accessed_at: '2026-10-28T06:09:09.926734Z'
  support: supports
  summary: 'Artificial seawater: source amount=22 g; chemical form, water input, gas
    or adjustment role retained at this section only.'
  locator: $.components[1].items[2]
  snapshot_sha256: a1ec3b432c2b60e3c3d92d73a6022246c4ad248683e4ce6e12cf039cef41bc09
  quote: '"component_name": "NaCl"'
- evidence_id: togo1107-api-q-1-3
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107
  accessed_at: '2026-10-28T06:09:09.926734Z'
  support: supports
  summary: 'Artificial seawater: source amount=0.3 g; chemical form, water input,
    gas or adjustment role retained at this section only.'
  locator: $.components[1].items[3]
  snapshot_sha256: a1ec3b432c2b60e3c3d92d73a6022246c4ad248683e4ce6e12cf039cef41bc09
  quote: '"component_name": "CaCl2・2H2O"'
- evidence_id: togo1107-api-q-1-4
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107
  accessed_at: '2026-10-28T06:09:09.926734Z'
  support: supports
  summary: 'Artificial seawater: source amount=0.42 g; chemical form, water input,
    gas or adjustment role retained at this section only.'
  locator: $.components[1].items[4]
  snapshot_sha256: a1ec3b432c2b60e3c3d92d73a6022246c4ad248683e4ce6e12cf039cef41bc09
  quote: '"component_name": "KH2PO4"'
- evidence_id: togo1107-api-q-1-5
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107
  accessed_at: '2026-10-28T06:09:09.926734Z'
  support: supports
  summary: 'Artificial seawater: source amount=3 g; chemical form, water input, gas
    or adjustment role retained at this section only.'
  locator: $.components[1].items[5]
  snapshot_sha256: a1ec3b432c2b60e3c3d92d73a6022246c4ad248683e4ce6e12cf039cef41bc09
  quote: '"component_name": "MgCl2・6H2O"'
- evidence_id: togo1107-api-q-1-6
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107
  accessed_at: '2026-10-28T06:09:09.926734Z'
  support: supports
  summary: 'Artificial seawater: source amount=0.5 g; chemical form, water input,
    gas or adjustment role retained at this section only.'
  locator: $.components[1].items[6]
  snapshot_sha256: a1ec3b432c2b60e3c3d92d73a6022246c4ad248683e4ce6e12cf039cef41bc09
  quote: '"component_name": "KCl"'
- evidence_id: togo1107-api-q-1-7
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107
  accessed_at: '2026-10-28T06:09:09.926734Z'
  support: supports
  summary: 'Artificial seawater: source amount=0.2 g; chemical form, water input,
    gas or adjustment role retained at this section only.'
  locator: $.components[1].items[7]
  snapshot_sha256: a1ec3b432c2b60e3c3d92d73a6022246c4ad248683e4ce6e12cf039cef41bc09
  quote: '"component_name": "NaHCO3"'
- evidence_id: togo1107-api-q-1-8
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107
  accessed_at: '2026-10-28T06:09:09.926734Z'
  support: supports
  summary: 'Artificial seawater: source amount=1 g; chemical form, water input, gas
    or adjustment role retained at this section only.'
  locator: $.components[1].items[8]
  snapshot_sha256: a1ec3b432c2b60e3c3d92d73a6022246c4ad248683e4ce6e12cf039cef41bc09
  quote: '"component_name": "(NH4)2SO4"'
- evidence_id: togo1107-api-q-1-9
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107
  accessed_at: '2026-10-28T06:09:09.926734Z'
  support: supports
  summary: 'Artificial seawater: source amount=0.05 g; chemical form, water input,
    gas or adjustment role retained at this section only.'
  locator: $.components[1].items[9]
  snapshot_sha256: a1ec3b432c2b60e3c3d92d73a6022246c4ad248683e4ce6e12cf039cef41bc09
  quote: '"component_name": "NaBr"'
- evidence_id: togo1107-api-q-1-10
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107
  accessed_at: '2026-10-28T06:09:09.926734Z'
  support: supports
  summary: 'Artificial seawater: source amount=0.02 g; chemical form, water input,
    gas or adjustment role retained at this section only.'
  locator: $.components[1].items[10]
  snapshot_sha256: a1ec3b432c2b60e3c3d92d73a6022246c4ad248683e4ce6e12cf039cef41bc09
  quote: '"component_name": "SrCl2・6H2O"'
- evidence_id: togo1107-api-q-1-11
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107
  accessed_at: '2026-10-28T06:09:09.926734Z'
  support: supports
  summary: 'Artificial seawater: source amount=0.01 g; chemical form, water input,
    gas or adjustment role retained at this section only.'
  locator: $.components[1].items[11]
  snapshot_sha256: a1ec3b432c2b60e3c3d92d73a6022246c4ad248683e4ce6e12cf039cef41bc09
  quote: '"component_name": "Ammonium Fe(III) citrate"'
- evidence_id: togo1107-api-q-1-12
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107
  accessed_at: '2026-10-28T06:09:09.926734Z'
  support: supports
  summary: 'Artificial seawater: source amount=5 ml; chemical form, water input, gas
    or adjustment role retained at this section only.'
  locator: $.components[1].items[12]
  snapshot_sha256: a1ec3b432c2b60e3c3d92d73a6022246c4ad248683e4ce6e12cf039cef41bc09
  quote: '"component_name": "Trace minerals (see Medium [M142])"'
- evidence_id: togo142-api-q-2-0
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142
  accessed_at: '2026-10-28T06:09:37.082631Z'
  support: supports
  summary: 'Trace minerals: source amount=1 L; chemical form, water input, gas or
    adjustment role retained at this section only.'
  locator: $.components[2].items[0]
  snapshot_sha256: 610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33
  quote: '"component_name": "Distilled water"'
- evidence_id: togo142-api-q-2-1
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142
  accessed_at: '2026-10-28T06:09:37.082631Z'
  support: supports
  summary: 'Trace minerals: source amount=3 g; chemical form, water input, gas or
    adjustment role retained at this section only.'
  locator: $.components[2].items[1]
  snapshot_sha256: 610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33
  quote: '"component_name": "MgSO4・7H2O"'
- evidence_id: togo142-api-q-2-2
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142
  accessed_at: '2026-10-28T06:09:37.082631Z'
  support: supports
  summary: 'Trace minerals: source amount=1 g; chemical form, water input, gas or
    adjustment role retained at this section only.'
  locator: $.components[2].items[2]
  snapshot_sha256: 610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33
  quote: '"component_name": "NaCl"'
- evidence_id: togo142-api-q-2-3
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142
  accessed_at: '2026-10-28T06:09:37.082631Z'
  support: supports
  summary: 'Trace minerals: source amount=0.1 g; chemical form, water input, gas or
    adjustment role retained at this section only.'
  locator: $.components[2].items[3]
  snapshot_sha256: 610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33
  quote: '"component_name": "CaCl2・2H2O"'
- evidence_id: togo142-api-q-2-4
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142
  accessed_at: '2026-10-28T06:09:37.082631Z'
  support: supports
  summary: 'Trace minerals: source amount=0.01 g; chemical form, water input, gas
    or adjustment role retained at this section only.'
  locator: $.components[2].items[4]
  snapshot_sha256: 610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33
  quote: '"component_name": "Na2MoO4・2H2O"'
- evidence_id: togo142-api-q-2-5
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142
  accessed_at: '2026-10-28T06:09:37.082631Z'
  support: supports
  summary: 'Trace minerals: source amount=0.01 g; chemical form, water input, gas
    or adjustment role retained at this section only.'
  locator: $.components[2].items[5]
  snapshot_sha256: 610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33
  quote: '"component_name": "H3BO3"'
- evidence_id: togo142-api-q-2-6
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142
  accessed_at: '2026-10-28T06:09:37.082631Z'
  support: supports
  summary: 'Trace minerals: source amount=0.1 g; chemical form, water input, gas or
    adjustment role retained at this section only.'
  locator: $.components[2].items[6]
  snapshot_sha256: 610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33
  quote: '"component_name": "FeSO4・7H2O"'
- evidence_id: togo142-api-q-2-7
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142
  accessed_at: '2026-10-28T06:09:37.082631Z'
  support: supports
  summary: 'Trace minerals: source amount=0.1 g; chemical form, water input, gas or
    adjustment role retained at this section only.'
  locator: $.components[2].items[7]
  snapshot_sha256: 610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33
  quote: '"component_name": "ZnSO4・7H2O"'
- evidence_id: togo142-api-q-2-8
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142
  accessed_at: '2026-10-28T06:09:37.082631Z'
  support: supports
  summary: 'Trace minerals: source amount=0.01 g; chemical form, water input, gas
    or adjustment role retained at this section only.'
  locator: $.components[2].items[8]
  snapshot_sha256: 610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33
  quote: '"component_name": "CuSO4・5H2O"'
- evidence_id: togo142-api-q-2-9
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142
  accessed_at: '2026-10-28T06:09:37.082631Z'
  support: supports
  summary: 'Trace minerals: source amount=0.1 g; chemical form, water input, gas or
    adjustment role retained at this section only.'
  locator: $.components[2].items[9]
  snapshot_sha256: 610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33
  quote: '"component_name": "CoSO4・7H2O"'
- evidence_id: togo142-api-q-2-10
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142
  accessed_at: '2026-10-28T06:09:37.082631Z'
  support: supports
  summary: 'Trace minerals: source amount=1.5 g; chemical form, water input, gas or
    adjustment role retained at this section only.'
  locator: $.components[2].items[10]
  snapshot_sha256: 610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33
  quote: '"component_name": "Nitrilotriacetic acid"'
- evidence_id: togo142-api-q-2-11
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142
  accessed_at: '2026-10-28T06:09:37.082631Z'
  support: supports
  summary: 'Trace minerals: source amount=0.5 g; chemical form, water input, gas or
    adjustment role retained at this section only.'
  locator: $.components[2].items[11]
  snapshot_sha256: 610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33
  quote: '"component_name": "MnSO4・xH2O"'
- evidence_id: togo142-api-q-2-12
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142
  accessed_at: '2026-10-28T06:09:37.082631Z'
  support: supports
  summary: 'Trace minerals: source amount=0.01 g; chemical form, water input, gas
    or adjustment role retained at this section only.'
  locator: $.components[2].items[12]
  snapshot_sha256: 610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33
  quote: '"component_name": "AlK(SO4)2"'
- evidence_id: togo142-api-q-2-13
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142
  accessed_at: '2026-10-28T06:09:37.082631Z'
  support: supports
  summary: 'Trace minerals: source amount=None None; chemical form, water input, gas
    or adjustment role retained at this section only.'
  locator: $.components[2].items[13]
  snapshot_sha256: 610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33
  quote: '"component_name": "KOH solution"'
- evidence_id: togo190-api-q-1-0
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190
  accessed_at: '2026-10-28T06:09:37.097083Z'
  support: supports
  summary: 'Trace vitamins: source amount=1 L; chemical form, water input, gas or
    adjustment role retained at this section only.'
  locator: $.components[1].items[0]
  snapshot_sha256: 61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528
  quote: '"component_name": "Distilled water"'
- evidence_id: togo190-api-q-1-1
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190
  accessed_at: '2026-10-28T06:09:37.097083Z'
  support: supports
  summary: 'Trace vitamins: source amount=2 mg; chemical form, water input, gas or
    adjustment role retained at this section only.'
  locator: $.components[1].items[1]
  snapshot_sha256: 61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528
  quote: '"component_name": "Biotin"'
- evidence_id: togo190-api-q-1-2
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190
  accessed_at: '2026-10-28T06:09:37.097083Z'
  support: supports
  summary: 'Trace vitamins: source amount=5 mg; chemical form, water input, gas or
    adjustment role retained at this section only.'
  locator: $.components[1].items[2]
  snapshot_sha256: 61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528
  quote: '"component_name": "p--Aminobenzoic acid"'
- evidence_id: togo190-api-q-1-3
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190
  accessed_at: '2026-10-28T06:09:37.097083Z'
  support: supports
  summary: 'Trace vitamins: source amount=5 mg; chemical form, water input, gas or
    adjustment role retained at this section only.'
  locator: $.components[1].items[3]
  snapshot_sha256: 61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528
  quote: '"component_name": "Thiamine・HCl"'
- evidence_id: togo190-api-q-1-4
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190
  accessed_at: '2026-10-28T06:09:37.097083Z'
  support: supports
  summary: 'Trace vitamins: source amount=5 mg; chemical form, water input, gas or
    adjustment role retained at this section only.'
  locator: $.components[1].items[4]
  snapshot_sha256: 61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528
  quote: '"component_name": "Calcium pantothenate"'
- evidence_id: togo190-api-q-1-5
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190
  accessed_at: '2026-10-28T06:09:37.097083Z'
  support: supports
  summary: 'Trace vitamins: source amount=10 mg; chemical form, water input, gas or
    adjustment role retained at this section only.'
  locator: $.components[1].items[5]
  snapshot_sha256: 61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528
  quote: '"component_name": "Pyridoxine・HCl"'
- evidence_id: togo190-api-q-1-6
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190
  accessed_at: '2026-10-28T06:09:37.097083Z'
  support: supports
  summary: 'Trace vitamins: source amount=2 mg; chemical form, water input, gas or
    adjustment role retained at this section only.'
  locator: $.components[1].items[6]
  snapshot_sha256: 61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528
  quote: '"component_name": "Folic acid"'
- evidence_id: togo190-api-q-1-7
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190
  accessed_at: '2026-10-28T06:09:37.097083Z'
  support: supports
  summary: 'Trace vitamins: source amount=0.1 mg; chemical form, water input, gas
    or adjustment role retained at this section only.'
  locator: $.components[1].items[7]
  snapshot_sha256: 61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528
  quote: '"component_name": "Vitamin B12"'
- evidence_id: togo190-api-q-1-8
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190
  accessed_at: '2026-10-28T06:09:37.097083Z'
  support: supports
  summary: 'Trace vitamins: source amount=5 mg; chemical form, water input, gas or
    adjustment role retained at this section only.'
  locator: $.components[1].items[8]
  snapshot_sha256: 61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528
  quote: '"component_name": "Riboflavin"'
- evidence_id: togo190-api-q-1-9
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190
  accessed_at: '2026-10-28T06:09:37.097083Z'
  support: supports
  summary: 'Trace vitamins: source amount=5 mg; chemical form, water input, gas or
    adjustment role retained at this section only.'
  locator: $.components[1].items[9]
  snapshot_sha256: 61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528
  quote: '"component_name": "Nicotinic acid"'
- evidence_id: togo190-api-q-1-10
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190
  accessed_at: '2026-10-28T06:09:37.097083Z'
  support: supports
  summary: 'Trace vitamins: source amount=5 mg; chemical form, water input, gas or
    adjustment role retained at this section only.'
  locator: $.components[1].items[10]
  snapshot_sha256: 61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528
  quote: '"component_name": "Lipoic acid"'
- evidence_id: chebi-15377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  accessed_at: '2026-10-28T06:08:19.144164Z'
  support: supports
  summary: CHEBI:15377 label=water; obsolete=False; supplied-form assessment uses
    the exact term object, not resolver agreement alone.
  locator: exact IRI term object
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: chebi-17997
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997
  accessed_at: '2026-10-28T06:08:19.137329Z'
  support: supports
  summary: CHEBI:17997 label=dinitrogen; obsolete=False; supplied-form assessment
    uses the exact term object, not resolver agreement alone.
  locator: exact IRI term object
  snapshot_sha256: ea4b3f90994884c49607689e3f3939cfec804c7d17905bbeecfc0ef7f80ead43
- evidence_id: chebi-26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  accessed_at: '2026-10-28T06:08:19.139435Z'
  support: supports
  summary: CHEBI:26710 label=sodium chloride; obsolete=False; supplied-form assessment
    uses the exact term object, not resolver agreement alone.
  locator: exact IRI term object
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi-31795
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  accessed_at: '2026-10-28T06:08:19.615915Z'
  support: supports
  summary: CHEBI:31795 label=magnesium sulfate heptahydrate; obsolete=False; supplied-form
    assessment uses the exact term object, not resolver agreement alone.
  locator: exact IRI term object
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
- evidence_id: chebi-32139
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139
  accessed_at: '2026-10-28T06:08:19.729304Z'
  support: supports
  summary: CHEBI:32139 label=sodium hydrogencarbonate; obsolete=False; supplied-form
    assessment uses the exact term object, not resolver agreement alone.
  locator: exact IRI term object
  snapshot_sha256: 2a41873aa455dc8563a47d36add836fffb6fb758ce7a2d1c28295e77646315fe
- evidence_id: chebi-32588
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588
  accessed_at: '2026-10-28T06:08:19.751940Z'
  support: supports
  summary: CHEBI:32588 label=potassium chloride; obsolete=False; supplied-form assessment
    uses the exact term object, not resolver agreement alone.
  locator: exact IRI term object
  snapshot_sha256: 536d6e3b5f2a3f1cb36d9c04b1502c4a6f00f4d770cd87b05b481e66ea43a411
- evidence_id: chebi-36385
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_36385
  accessed_at: '2026-10-28T06:08:19.746915Z'
  support: supports
  summary: CHEBI:36385 label=strontium dichloride hexahydrate; obsolete=False; supplied-form
    assessment uses the exact term object, not resolver agreement alone.
  locator: exact IRI term object
  snapshot_sha256: a81397c907aeb36242c9f0a2aa24979df4b9aad2f624e8991ccd87a4ff9428b5
- evidence_id: chebi-39033
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_39033
  accessed_at: '2026-10-28T06:08:19.791057Z'
  support: supports
  summary: CHEBI:39033 label=PIPES; obsolete=False; supplied-form assessment uses
    the exact term object, not resolver agreement alone.
  locator: exact IRI term object
  snapshot_sha256: 2b263114d78572f453bf17a3de28b586d9b58f1120980a5df03292ef7b85d5d9
- evidence_id: chebi-50144
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_50144
  accessed_at: '2026-10-28T06:08:19.987637Z'
  support: supports
  summary: CHEBI:50144 label=sodium pyruvate; obsolete=False; supplied-form assessment
    uses the exact term object, not resolver agreement alone.
  locator: exact IRI term object
  snapshot_sha256: 457ed29adfdea68c420ea0c094d7d75593958fc70f908f6809348e4e12e7e15d
- evidence_id: chebi-62946
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946
  accessed_at: '2026-10-28T06:08:20.218676Z'
  support: supports
  summary: CHEBI:62946 label=ammonium sulfate; obsolete=False; supplied-form assessment
    uses the exact term object, not resolver agreement alone.
  locator: exact IRI term object
  snapshot_sha256: 10c25b481047a1fdfbc201104ecc06b15b32d5e72319beed5133e5d5693bede5
- evidence_id: chebi-63004
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63004
  accessed_at: '2026-10-28T06:08:20.326179Z'
  support: supports
  summary: CHEBI:63004 label=sodium bromide; obsolete=False; supplied-form assessment
    uses the exact term object, not resolver agreement alone.
  locator: exact IRI term object
  snapshot_sha256: 2665f3a4301ab51b67b814a8694bc906c1a13c9b301c85a4416891d3f9412c90
- evidence_id: chebi-63036
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  accessed_at: '2026-10-28T06:08:20.347217Z'
  support: supports
  summary: CHEBI:63036 label=potassium dihydrogen phosphate; obsolete=False; supplied-form
    assessment uses the exact term object, not resolver agreement alone.
  locator: exact IRI term object
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: chebi-86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  accessed_at: '2026-10-28T06:08:20.357209Z'
  support: supports
  summary: CHEBI:86158 label=calcium chloride dihydrate; obsolete=False; supplied-form
    assessment uses the exact term object, not resolver agreement alone.
  locator: exact IRI term object
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi-86345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345
  accessed_at: '2026-10-28T06:08:20.377903Z'
  support: supports
  summary: CHEBI:86345 label=magnesium dichloride hexahydrate; obsolete=False; supplied-form
    assessment uses the exact term object, not resolver agreement alone.
  locator: exact IRI term object
  snapshot_sha256: 08a75ab7c89066e54998e26bfba46e579358aa1a0ee5611430577d7c38e25133
- evidence_id: historical-1
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-3000-3319/records/bacterial/calroanaerobacter_medium.yaml.md
  accessed_at: '2026-10-28T06:19:10.753399Z'
  support: context_only
  summary: Historical context read completely, with repeated tables compared losslessly.
    Not native coverage. Earlier final-litre recommendations and blanket stock conflicts
    are reassessed against current scoped source amounts.
  locator: entire file
  snapshot_sha256: ffffbf7f19bdf3381f29e73baa536f5d951ab6f75b20b6cb670db79b5e0abcf5
- evidence_id: historical-2
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.md
  accessed_at: '2026-10-28T06:19:10.753399Z'
  support: context_only
  summary: Historical context read completely, with repeated tables compared losslessly.
    Not native coverage. Earlier final-litre recommendations and blanket stock conflicts
    are reassessed against current scoped source amounts.
  locator: entire file
  snapshot_sha256: 037fb7d4630684ddc05c87ccd579fe643a15f0b7ef3ae3ef74fbf32d52b6cdcb
- evidence_id: historical-3
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/calroanaerobacter_medium__375948ba.md
  accessed_at: '2026-10-28T06:19:10.753399Z'
  support: context_only
  summary: Historical context read completely, with repeated tables compared losslessly.
    Not native coverage. Earlier final-litre recommendations and blanket stock conflicts
    are reassessed against current scoped source amounts.
  locator: entire file
  snapshot_sha256: 18d73dd6b5f71b1e171c08b78f105ab0e3cf3581c00f8c040ea533cef1d648ea
- evidence_id: historical-4
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.md
  accessed_at: '2026-10-28T06:19:10.753399Z'
  support: context_only
  summary: Historical context read completely, with repeated tables compared losslessly.
    Not native coverage. Earlier final-litre recommendations and blanket stock conflicts
    are reassessed against current scoped source amounts.
  locator: entire file
  snapshot_sha256: 94fdeee68e2b717c45c832adbaf7f2786039e4f1e572fca49b0ec05188c0739b
- evidence_id: historical-5
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/calroanaerobacter_medium.md
  accessed_at: '2026-10-28T06:19:10.753399Z'
  support: context_only
  summary: Historical context read completely, with repeated tables compared losslessly.
    Not native coverage. Earlier final-litre recommendations and blanket stock conflicts
    are reassessed against current scoped source amounts.
  locator: entire file
  snapshot_sha256: 73dbd5c625347aebfcf7cd852fd1b25856af3c53f1342b56e120fa49b99252f8
- evidence_id: historical-6
  kind: prior_review
  reference: reports/yaml_record_review/20260922T025827Z-CALROANAEROBACTER_MEDIUM.md
  accessed_at: '2026-10-28T06:19:10.753399Z'
  support: context_only
  summary: Historical context read completely, with repeated tables compared losslessly.
    Not native coverage. Earlier final-litre recommendations and blanket stock conflicts
    are reassessed against current scoped source amounts.
  locator: entire file
  snapshot_sha256: 1f3722c06153cc1e26ab51a97edc3c8b2e7a17032d2cf69d797d1da0dc4f6f62
- evidence_id: historical-7
  kind: prior_review
  reference: reports/yaml_record_review/20260922T025936Z-calroanaerobacter_medium__375948ba.md
  accessed_at: '2026-10-28T06:19:10.753399Z'
  support: context_only
  summary: Historical context read completely, with repeated tables compared losslessly.
    Not native coverage. Earlier final-litre recommendations and blanket stock conflicts
    are reassessed against current scoped source amounts.
  locator: entire file
  snapshot_sha256: b90f3c1a08321ea6e9ffb5abb53c96fd6c17c993ee277ed5b73491675b4471e4
- evidence_id: diagnostics
  kind: validation
  reference: REVIEW_WORK/batch058/record10/diagnostics.json
  accessed_at: '2026-10-28T06:15:23.821768Z'
  support: context_only
  summary: Read-only maintained resolver and importer previews,47 exact source-object/literal
    joins, registry and ignored-inclusive local search.
  locator: entire file
  snapshot_sha256: b16f33e2c6af3a916f5eeb6913fd7b7a4f70e736dd6fca11418dfeea731f09a7
- evidence_id: ownership-search
  kind: search
  reference: REVIEW_WORK/batch058/record10/diagnostics.json
  accessed_at: '2026-10-28T06:15:23.821768Z'
  support: context_only
  summary: Exact maintained source/counterpart and report leads found. No claim to
    have read every queue/archive hit.
  locator: ownership_search.argv/stdout
  snapshot_sha256: b16f33e2c6af3a916f5eeb6913fd7b7a4f70e736dd6fca11418dfeea731f09a7
  search_scope: rg --no-ignore --hidden -n -l across data/normalized_yaml and reports
    for three exact IDs and both source slugs; ignored and hidden files included.
    Content absence findings are confined to fully inspected records.
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch058/record10/validate-schema-result.json
  accessed_at: '2026-10-28T06:07:47.480592Z'
  support: context_only
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  locator: full argv/stdout/stderr
  snapshot_sha256: 86f1f4392b73df93945ea524689e2abcbfc82a156fa1d3d79a13171bea85de21
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch058/record10/validate-strict-result.json
  accessed_at: '2026-10-28T06:07:48.674665Z'
  support: context_only
  summary: "Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         REVIEW_WORK/batch058/record10/strict.tsv"
  locator: full argv/stdout/stderr
  snapshot_sha256: 5b401e10c6e3c06081327e93b59bfda34617ce2dcbc779604d846fe6c01afb61
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch058/record10/validate-terms-result.json
  accessed_at: '2026-10-28T06:07:50.300243Z'
  support: context_only
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  locator: full argv/stdout/stderr
  snapshot_sha256: 9c4f0447d9fc5e55610fba18f85847405916c862fdb11bfeb0211d0cb7132073
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch058/record10/validate-references-result.json
  accessed_at: '2026-10-28T06:07:51.212338Z'
  support: context_only
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  locator: full argv/stdout/stderr
  snapshot_sha256: ee36861d07c9dea7f8012d73984f111271318cf149681a639e69f9501f8be7fe
assessments:
- assessment_id: identity
  area: identity
  topic: Exact source and maintained ownership
  outcome: supported
  summary: Selected CM007626 is the TOGO M1107/JCM1042 medium; sole owner and current
    database cross-reference are supported.
  target_ids:
  - CultureMech:007626
  evidence_ids:
  - target
  - owner
  - registry
  - togo1107-api
  - mediadiveJ1042
  - jcm1042
  - jcm1042-pdf
  details: The source spelling Calroanaerobacter is retained without inferring taxonomy
    or growth. The similarly named CM002227 and solution5101 are context only. No
    DOI, PMID, strain accession or target-organism claim is asserted by the selected
    record. iModulonDB is not applicable to this medium formulation.
- assessment_id: quantity
  area: evidence
  topic: All existing quantities and referenced recipe rows
  outcome: concern
  summary: 40 local fields assessed:8 unsupported rate denominators and32 conflicts;45
    scoped TOGO rows and43 MediaDive recipe rows retained.
  target_ids:
  - CultureMech:007626
  evidence_ids:
  - target
  - owner
  - togo1107-api
  - mediadiveJ1042
  - jcm151
  - jcm197
  - togo1107-api-q-0-0
  - togo1107-api-q-0-1
  - togo1107-api-q-0-2
  - togo1107-api-q-0-3
  - togo1107-api-q-0-4
  - togo1107-api-q-0-5
  - togo1107-api-q-0-6
  - togo1107-api-q-1-0
  - togo1107-api-q-1-1
  - togo1107-api-q-1-2
  - togo1107-api-q-1-3
  - togo1107-api-q-1-4
  - togo1107-api-q-1-5
  - togo1107-api-q-1-6
  - togo1107-api-q-1-7
  - togo1107-api-q-1-8
  - togo1107-api-q-1-9
  - togo1107-api-q-1-10
  - togo1107-api-q-1-11
  - togo1107-api-q-1-12
  - togo142-api-q-2-0
  - togo142-api-q-2-1
  - togo142-api-q-2-2
  - togo142-api-q-2-3
  - togo142-api-q-2-4
  - togo142-api-q-2-5
  - togo142-api-q-2-6
  - togo142-api-q-2-7
  - togo142-api-q-2-8
  - togo142-api-q-2-9
  - togo142-api-q-2-10
  - togo142-api-q-2-11
  - togo142-api-q-2-12
  - togo142-api-q-2-13
  - togo190-api-q-1-0
  - togo190-api-q-1-1
  - togo190-api-q-1-2
  - togo190-api-q-1-3
  - togo190-api-q-1-4
  - togo190-api-q-1-5
  - togo190-api-q-1-6
  - togo190-api-q-1-7
  - togo190-api-q-1-8
  - togo190-api-q-1-9
  - togo190-api-q-1-10
  details: '{"existing_field_count": 40, "counts": {"unsupported": 8, "conflict":
    32}, "record_field_counts": {"data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml":
    20, "data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml":
    20}, "quantities": [{"record_path": "data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml",
    "field_path": "ingredients[0].concentration", "ingredient": "Sodium pyruvate",
    "existing": {"value": "5", "unit": "G_PER_L"}, "decision": "unsupported", "source_evidence":
    ["togo1107-api-q-0-0"], "source_locator": "$.components[0].items[0]", "source_row":
    {"component_name": "Sodium pyruvate", "volume": 5, "unit": "g", "gmo_id": "GMO_001055"},
    "source_stage": "main solution 1", "explanation": "Source mass matches the local
    number, but it is an amount in the listed main batch. One litre of seawater plus5
    ml vitamins does not establish a final litre. G_PER_L denominator is unverified;
    preserve mass and batch context.", "calculation": "none; no final-volume assumption",
    "proposed_amount": "none asserted"}, {"record_path": "data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml",
    "field_path": "ingredients[1].concentration", "ingredient": "PIPES", "existing":
    {"value": "3.46", "unit": "G_PER_L"}, "decision": "unsupported", "source_evidence":
    ["togo1107-api-q-0-1"], "source_locator": "$.components[0].items[1]", "source_row":
    {"component_name": "PIPES", "volume": 3.46, "unit": "g", "gmo_id": "GMO_001223"},
    "source_stage": "main solution 1", "explanation": "Source mass matches the local
    number, but it is an amount in the listed main batch. One litre of seawater plus5
    ml vitamins does not establish a final litre. G_PER_L denominator is unverified;
    preserve mass and batch context.", "calculation": "none; no final-volume assumption",
    "proposed_amount": "none asserted"}, {"record_path": "data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml",
    "field_path": "ingredients[2].concentration", "ingredient": "Yeast extract (BD-Difco)",
    "existing": {"value": "2", "unit": "G_PER_L"}, "decision": "unsupported", "source_evidence":
    ["togo1107-api-q-0-2"], "source_locator": "$.components[0].items[2]", "source_row":
    {"component_name": "Yeast extract (BD-Difco)", "volume": 2, "unit": "g", "gmo_id":
    "GMO_001018"}, "source_stage": "main solution 1", "explanation": "Source mass
    matches the local number, but it is an amount in the listed main batch. One litre
    of seawater plus5 ml vitamins does not establish a final litre. G_PER_L denominator
    is unverified; preserve mass and batch context.", "calculation": "none; no final-volume
    assumption", "proposed_amount": "none asserted"}, {"record_path": "data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml",
    "field_path": "ingredients[3].concentration", "ingredient": "Tryptone (BD-Difco)",
    "existing": {"value": "2", "unit": "G_PER_L"}, "decision": "unsupported", "source_evidence":
    ["togo1107-api-q-0-3"], "source_locator": "$.components[0].items[3]", "source_row":
    {"component_name": "Tryptone (BD-Difco)", "volume": 2, "unit": "g", "gmo_id":
    "GMO_001043"}, "source_stage": "main solution 1", "explanation": "Source mass
    matches the local number, but it is an amount in the listed main batch. One litre
    of seawater plus5 ml vitamins does not establish a final litre. G_PER_L denominator
    is unverified; preserve mass and batch context.", "calculation": "none; no final-volume
    assumption", "proposed_amount": "none asserted"}, {"record_path": "data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml",
    "field_path": "ingredients[4].concentration", "ingredient": "Artificial seawater
    (see below)", "existing": {"value": "1", "unit": "G_PER_L"}, "decision": "conflict",
    "source_evidence": ["togo1107-api-q-0-5"], "source_locator": "$.components[0].items[5]",
    "source_row": {"component_name": "Artificial seawater (see below)", "volume":
    1, "unit": "L", "reference_media_id": "M1107"}, "source_stage": "main solution
    1", "explanation": "Source specifies1 L of prepared artificial seawater added
    to the main batch, not1 G_PER_L ingredient. Restore a solution addition and its
    internal stock stages.", "calculation": "none; no final-volume assumption", "proposed_amount":
    "none asserted"}, {"record_path": "data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml",
    "field_path": "ingredients[5].concentration", "ingredient": "N2", "existing":
    {"value": "variable", "unit": "VARIABLE"}, "decision": "conflict", "source_evidence":
    ["togo1107-api-q-0-6"], "source_locator": "$.components[0].items[6]", "source_row":
    {"component_name": "N2", "gmo_id": "GMO_002261"}, "source_stage": "main solution
    1", "explanation": "Source N2 is an unquantified gas atmosphere, supported by
    preparation prose. VARIABLE is not a measured solute concentration. Keep gas/headspace
    context without inventing amount, pressure or molarity.", "calculation": "none;
    no final-volume assumption", "proposed_amount": "none asserted"}, {"record_path":
    "data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml", "field_path": "ingredients[6].concentration",
    "ingredient": "Distilled water", "existing": {"value": "1", "unit": "G_PER_L"},
    "decision": "conflict", "source_evidence": ["togo1107-api-q-1-0"], "source_locator":
    "$.components[1].items[0]", "source_row": {"component_name": "Distilled water",
    "volume": 1, "unit": "L", "gmo_id": "GMO_001001"}, "source_stage": "Artificial
    seawater", "explanation": "Source specifies1 L of distilled water used in the
    artificial-seawater stock, not1 G_PER_L direct solute or an explicit final-volume
    make-up.", "calculation": "none; no final-volume assumption", "proposed_amount":
    "none asserted"}, {"record_path": "data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml",
    "field_path": "ingredients[7].concentration", "ingredient": "MgSO4・7H2O", "existing":
    {"value": "6", "unit": "G_PER_L"}, "decision": "conflict", "source_evidence":
    ["togo1107-api-q-1-1"], "source_locator": "$.components[1].items[1]", "source_row":
    {"component_name": "MgSO4・7H2O", "volume": 6, "unit": "g", "gmo_id": "GMO_001002"},
    "source_stage": "Artificial seawater", "explanation": "Source mass belongs to
    artificial-seawater preparation, not a direct main-medium concentration. Preserve
    exact salt/hydrate and mass in that stock; do not infer stock or final-medium
    rate from water input.", "calculation": "none; no final-volume assumption", "proposed_amount":
    "none asserted"}, {"record_path": "data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml",
    "field_path": "ingredients[8].concentration", "ingredient": "NaCl", "existing":
    {"value": "22", "unit": "G_PER_L"}, "decision": "conflict", "source_evidence":
    ["togo1107-api-q-1-2"], "source_locator": "$.components[1].items[2]", "source_row":
    {"component_name": "NaCl", "volume": 22, "unit": "g", "gmo_id": "GMO_001004"},
    "source_stage": "Artificial seawater", "explanation": "Source mass belongs to
    artificial-seawater preparation, not a direct main-medium concentration. Preserve
    exact salt/hydrate and mass in that stock; do not infer stock or final-medium
    rate from water input.", "calculation": "none; no final-volume assumption", "proposed_amount":
    "none asserted"}, {"record_path": "data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml",
    "field_path": "ingredients[9].concentration", "ingredient": "CaCl2・2H2O", "existing":
    {"value": "0.3", "unit": "G_PER_L"}, "decision": "conflict", "source_evidence":
    ["togo1107-api-q-1-3"], "source_locator": "$.components[1].items[3]", "source_row":
    {"component_name": "CaCl2・2H2O", "volume": 0.3, "unit": "g", "gmo_id": "GMO_001005"},
    "source_stage": "Artificial seawater", "explanation": "Source mass belongs to
    artificial-seawater preparation, not a direct main-medium concentration. Preserve
    exact salt/hydrate and mass in that stock; do not infer stock or final-medium
    rate from water input.", "calculation": "none; no final-volume assumption", "proposed_amount":
    "none asserted"}, {"record_path": "data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml",
    "field_path": "ingredients[10].concentration", "ingredient": "KH2PO4", "existing":
    {"value": "0.42", "unit": "G_PER_L"}, "decision": "conflict", "source_evidence":
    ["togo1107-api-q-1-4"], "source_locator": "$.components[1].items[4]", "source_row":
    {"component_name": "KH2PO4", "volume": 0.42, "unit": "g", "gmo_id": "GMO_001006"},
    "source_stage": "Artificial seawater", "explanation": "Source mass belongs to
    artificial-seawater preparation, not a direct main-medium concentration. Preserve
    exact salt/hydrate and mass in that stock; do not infer stock or final-medium
    rate from water input.", "calculation": "none; no final-volume assumption", "proposed_amount":
    "none asserted"}, {"record_path": "data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml",
    "field_path": "ingredients[11].concentration", "ingredient": "MgCl2・6H2O", "existing":
    {"value": "3", "unit": "G_PER_L"}, "decision": "conflict", "source_evidence":
    ["togo1107-api-q-1-5"], "source_locator": "$.components[1].items[5]", "source_row":
    {"component_name": "MgCl2・6H2O", "volume": 3, "unit": "g", "gmo_id": "GMO_001013"},
    "source_stage": "Artificial seawater", "explanation": "Source mass belongs to
    artificial-seawater preparation, not a direct main-medium concentration. Preserve
    exact salt/hydrate and mass in that stock; do not infer stock or final-medium
    rate from water input.", "calculation": "none; no final-volume assumption", "proposed_amount":
    "none asserted"}, {"record_path": "data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml",
    "field_path": "ingredients[12].concentration", "ingredient": "KCl", "existing":
    {"value": "0.5", "unit": "G_PER_L"}, "decision": "conflict", "source_evidence":
    ["togo1107-api-q-1-6"], "source_locator": "$.components[1].items[6]", "source_row":
    {"component_name": "KCl", "volume": 0.5, "unit": "g", "gmo_id": "GMO_001017"},
    "source_stage": "Artificial seawater", "explanation": "Source mass belongs to
    artificial-seawater preparation, not a direct main-medium concentration. Preserve
    exact salt/hydrate and mass in that stock; do not infer stock or final-medium
    rate from water input.", "calculation": "none; no final-volume assumption", "proposed_amount":
    "none asserted"}, {"record_path": "data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml",
    "field_path": "ingredients[13].concentration", "ingredient": "NaHCO3", "existing":
    {"value": "0.2", "unit": "G_PER_L"}, "decision": "conflict", "source_evidence":
    ["togo1107-api-q-1-7"], "source_locator": "$.components[1].items[7]", "source_row":
    {"component_name": "NaHCO3", "volume": 0.2, "unit": "g", "gmo_id": "GMO_001019"},
    "source_stage": "Artificial seawater", "explanation": "Source mass belongs to
    artificial-seawater preparation, not a direct main-medium concentration. Preserve
    exact salt/hydrate and mass in that stock; do not infer stock or final-medium
    rate from water input.", "calculation": "none; no final-volume assumption", "proposed_amount":
    "none asserted"}, {"record_path": "data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml",
    "field_path": "ingredients[14].concentration", "ingredient": "(NH4)2SO4", "existing":
    {"value": "1", "unit": "G_PER_L"}, "decision": "conflict", "source_evidence":
    ["togo1107-api-q-1-8"], "source_locator": "$.components[1].items[8]", "source_row":
    {"component_name": "(NH4)2SO4", "volume": 1, "unit": "g", "gmo_id": "GMO_001030"},
    "source_stage": "Artificial seawater", "explanation": "Source mass belongs to
    artificial-seawater preparation, not a direct main-medium concentration. Preserve
    exact salt/hydrate and mass in that stock; do not infer stock or final-medium
    rate from water input.", "calculation": "none; no final-volume assumption", "proposed_amount":
    "none asserted"}, {"record_path": "data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml",
    "field_path": "ingredients[15].concentration", "ingredient": "NaBr", "existing":
    {"value": "0.05", "unit": "G_PER_L"}, "decision": "conflict", "source_evidence":
    ["togo1107-api-q-1-9"], "source_locator": "$.components[1].items[9]", "source_row":
    {"component_name": "NaBr", "volume": 0.05, "unit": "g", "gmo_id": "GMO_001073"},
    "source_stage": "Artificial seawater", "explanation": "Source mass belongs to
    artificial-seawater preparation, not a direct main-medium concentration. Preserve
    exact salt/hydrate and mass in that stock; do not infer stock or final-medium
    rate from water input.", "calculation": "none; no final-volume assumption", "proposed_amount":
    "none asserted"}, {"record_path": "data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml",
    "field_path": "ingredients[16].concentration", "ingredient": "SrCl2・6H2O", "existing":
    {"value": "0.02", "unit": "G_PER_L"}, "decision": "conflict", "source_evidence":
    ["togo1107-api-q-1-10"], "source_locator": "$.components[1].items[10]", "source_row":
    {"component_name": "SrCl2・6H2O", "volume": 0.02, "unit": "g", "gmo_id": "GMO_001085"},
    "source_stage": "Artificial seawater", "explanation": "Source mass belongs to
    artificial-seawater preparation, not a direct main-medium concentration. Preserve
    exact salt/hydrate and mass in that stock; do not infer stock or final-medium
    rate from water input.", "calculation": "none; no final-volume assumption", "proposed_amount":
    "none asserted"}, {"record_path": "data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml",
    "field_path": "ingredients[17].concentration", "ingredient": "Ammonium Fe(III)
    citrate", "existing": {"value": "0.01", "unit": "G_PER_L"}, "decision": "conflict",
    "source_evidence": ["togo1107-api-q-1-11"], "source_locator": "$.components[1].items[11]",
    "source_row": {"component_name": "Ammonium Fe(III) citrate", "volume": 0.01, "unit":
    "g", "gmo_id": "GMO_001147"}, "source_stage": "Artificial seawater", "explanation":
    "Source mass belongs to artificial-seawater preparation, not a direct main-medium
    concentration. Preserve exact salt/hydrate and mass in that stock; do not infer
    stock or final-medium rate from water input.", "calculation": "none; no final-volume
    assumption", "proposed_amount": "none asserted"}, {"record_path": "data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml",
    "field_path": "solutions[0].concentration", "ingredient": "Trace vitamins (see
    Medium [M190])", "existing": {"value": "5", "unit": "G_PER_L"}, "decision": "conflict",
    "source_evidence": ["togo1107-api-q-0-4"], "source_locator": "$.components[0].items[4]",
    "source_row": {"component_name": "Trace vitamins (see Medium [M190])", "volume":
    5, "unit": "ml", "reference_media_id": "M190"}, "explanation": "Source5 ml vitamin-stock
    addition belongs to the main batch. G_PER_L is the wrong dimension; final-volume
    basis for ML_PER_L is also unproved. Restore the batch dose and complete dependency
    definition.", "calculation": "none; no density or final-volume assumption", "proposed_amount":
    "none asserted"}, {"record_path": "data/merge_yaml/merged/CALROANAEROBACTER_MEDIUM.yaml",
    "field_path": "solutions[1].concentration", "ingredient": "Trace minerals (see
    Medium [M142])", "existing": {"value": "5", "unit": "G_PER_L"}, "decision": "conflict",
    "source_evidence": ["togo1107-api-q-1-12"], "source_locator": "$.components[1].items[12]",
    "source_row": {"component_name": "Trace minerals (see Medium [M142])", "volume":
    5, "unit": "ml", "reference_media_id": "M142"}, "explanation": "Source5 ml trace-mineral
    addition belongs inside the artificial-seawater batch. G_PER_L is the wrong dimension;
    final-volume basis for ML_PER_L is also unproved. Restore the batch dose and complete
    dependency definition.", "calculation": "none; no density or final-volume assumption",
    "proposed_amount": "none asserted"}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml",
    "field_path": "ingredients[0].concentration", "ingredient": "Sodium pyruvate",
    "existing": {"value": "5", "unit": "G_PER_L"}, "decision": "unsupported", "source_evidence":
    ["togo1107-api-q-0-0"], "source_locator": "$.components[0].items[0]", "source_row":
    {"component_name": "Sodium pyruvate", "volume": 5, "unit": "g", "gmo_id": "GMO_001055"},
    "source_stage": "main solution 1", "explanation": "Source mass matches the local
    number, but it is an amount in the listed main batch. One litre of seawater plus5
    ml vitamins does not establish a final litre. G_PER_L denominator is unverified;
    preserve mass and batch context.", "calculation": "none; no final-volume assumption",
    "proposed_amount": "none asserted"}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml",
    "field_path": "ingredients[1].concentration", "ingredient": "PIPES", "existing":
    {"value": "3.46", "unit": "G_PER_L"}, "decision": "unsupported", "source_evidence":
    ["togo1107-api-q-0-1"], "source_locator": "$.components[0].items[1]", "source_row":
    {"component_name": "PIPES", "volume": 3.46, "unit": "g", "gmo_id": "GMO_001223"},
    "source_stage": "main solution 1", "explanation": "Source mass matches the local
    number, but it is an amount in the listed main batch. One litre of seawater plus5
    ml vitamins does not establish a final litre. G_PER_L denominator is unverified;
    preserve mass and batch context.", "calculation": "none; no final-volume assumption",
    "proposed_amount": "none asserted"}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml",
    "field_path": "ingredients[2].concentration", "ingredient": "Yeast extract (BD-Difco)",
    "existing": {"value": "2", "unit": "G_PER_L"}, "decision": "unsupported", "source_evidence":
    ["togo1107-api-q-0-2"], "source_locator": "$.components[0].items[2]", "source_row":
    {"component_name": "Yeast extract (BD-Difco)", "volume": 2, "unit": "g", "gmo_id":
    "GMO_001018"}, "source_stage": "main solution 1", "explanation": "Source mass
    matches the local number, but it is an amount in the listed main batch. One litre
    of seawater plus5 ml vitamins does not establish a final litre. G_PER_L denominator
    is unverified; preserve mass and batch context.", "calculation": "none; no final-volume
    assumption", "proposed_amount": "none asserted"}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml",
    "field_path": "ingredients[3].concentration", "ingredient": "Tryptone (BD-Difco)",
    "existing": {"value": "2", "unit": "G_PER_L"}, "decision": "unsupported", "source_evidence":
    ["togo1107-api-q-0-3"], "source_locator": "$.components[0].items[3]", "source_row":
    {"component_name": "Tryptone (BD-Difco)", "volume": 2, "unit": "g", "gmo_id":
    "GMO_001043"}, "source_stage": "main solution 1", "explanation": "Source mass
    matches the local number, but it is an amount in the listed main batch. One litre
    of seawater plus5 ml vitamins does not establish a final litre. G_PER_L denominator
    is unverified; preserve mass and batch context.", "calculation": "none; no final-volume
    assumption", "proposed_amount": "none asserted"}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml",
    "field_path": "ingredients[4].concentration", "ingredient": "Artificial seawater
    (see below)", "existing": {"value": "1", "unit": "G_PER_L"}, "decision": "conflict",
    "source_evidence": ["togo1107-api-q-0-5"], "source_locator": "$.components[0].items[5]",
    "source_row": {"component_name": "Artificial seawater (see below)", "volume":
    1, "unit": "L", "reference_media_id": "M1107"}, "source_stage": "main solution
    1", "explanation": "Source specifies1 L of prepared artificial seawater added
    to the main batch, not1 G_PER_L ingredient. Restore a solution addition and its
    internal stock stages.", "calculation": "none; no final-volume assumption", "proposed_amount":
    "none asserted"}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml",
    "field_path": "ingredients[5].concentration", "ingredient": "N2", "existing":
    {"value": "variable", "unit": "VARIABLE"}, "decision": "conflict", "source_evidence":
    ["togo1107-api-q-0-6"], "source_locator": "$.components[0].items[6]", "source_row":
    {"component_name": "N2", "gmo_id": "GMO_002261"}, "source_stage": "main solution
    1", "explanation": "Source N2 is an unquantified gas atmosphere, supported by
    preparation prose. VARIABLE is not a measured solute concentration. Keep gas/headspace
    context without inventing amount, pressure or molarity.", "calculation": "none;
    no final-volume assumption", "proposed_amount": "none asserted"}, {"record_path":
    "data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml", "field_path":
    "ingredients[6].concentration", "ingredient": "Distilled water", "existing": {"value":
    "1", "unit": "G_PER_L"}, "decision": "conflict", "source_evidence": ["togo1107-api-q-1-0"],
    "source_locator": "$.components[1].items[0]", "source_row": {"component_name":
    "Distilled water", "volume": 1, "unit": "L", "gmo_id": "GMO_001001"}, "source_stage":
    "Artificial seawater", "explanation": "Source specifies1 L of distilled water
    used in the artificial-seawater stock, not1 G_PER_L direct solute or an explicit
    final-volume make-up.", "calculation": "none; no final-volume assumption", "proposed_amount":
    "none asserted"}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml",
    "field_path": "ingredients[7].concentration", "ingredient": "MgSO4・7H2O", "existing":
    {"value": "6", "unit": "G_PER_L"}, "decision": "conflict", "source_evidence":
    ["togo1107-api-q-1-1"], "source_locator": "$.components[1].items[1]", "source_row":
    {"component_name": "MgSO4・7H2O", "volume": 6, "unit": "g", "gmo_id": "GMO_001002"},
    "source_stage": "Artificial seawater", "explanation": "Source mass belongs to
    artificial-seawater preparation, not a direct main-medium concentration. Preserve
    exact salt/hydrate and mass in that stock; do not infer stock or final-medium
    rate from water input.", "calculation": "none; no final-volume assumption", "proposed_amount":
    "none asserted"}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml",
    "field_path": "ingredients[8].concentration", "ingredient": "NaCl", "existing":
    {"value": "22", "unit": "G_PER_L"}, "decision": "conflict", "source_evidence":
    ["togo1107-api-q-1-2"], "source_locator": "$.components[1].items[2]", "source_row":
    {"component_name": "NaCl", "volume": 22, "unit": "g", "gmo_id": "GMO_001004"},
    "source_stage": "Artificial seawater", "explanation": "Source mass belongs to
    artificial-seawater preparation, not a direct main-medium concentration. Preserve
    exact salt/hydrate and mass in that stock; do not infer stock or final-medium
    rate from water input.", "calculation": "none; no final-volume assumption", "proposed_amount":
    "none asserted"}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml",
    "field_path": "ingredients[9].concentration", "ingredient": "CaCl2・2H2O", "existing":
    {"value": "0.3", "unit": "G_PER_L"}, "decision": "conflict", "source_evidence":
    ["togo1107-api-q-1-3"], "source_locator": "$.components[1].items[3]", "source_row":
    {"component_name": "CaCl2・2H2O", "volume": 0.3, "unit": "g", "gmo_id": "GMO_001005"},
    "source_stage": "Artificial seawater", "explanation": "Source mass belongs to
    artificial-seawater preparation, not a direct main-medium concentration. Preserve
    exact salt/hydrate and mass in that stock; do not infer stock or final-medium
    rate from water input.", "calculation": "none; no final-volume assumption", "proposed_amount":
    "none asserted"}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml",
    "field_path": "ingredients[10].concentration", "ingredient": "KH2PO4", "existing":
    {"value": "0.42", "unit": "G_PER_L"}, "decision": "conflict", "source_evidence":
    ["togo1107-api-q-1-4"], "source_locator": "$.components[1].items[4]", "source_row":
    {"component_name": "KH2PO4", "volume": 0.42, "unit": "g", "gmo_id": "GMO_001006"},
    "source_stage": "Artificial seawater", "explanation": "Source mass belongs to
    artificial-seawater preparation, not a direct main-medium concentration. Preserve
    exact salt/hydrate and mass in that stock; do not infer stock or final-medium
    rate from water input.", "calculation": "none; no final-volume assumption", "proposed_amount":
    "none asserted"}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml",
    "field_path": "ingredients[11].concentration", "ingredient": "MgCl2・6H2O", "existing":
    {"value": "3", "unit": "G_PER_L"}, "decision": "conflict", "source_evidence":
    ["togo1107-api-q-1-5"], "source_locator": "$.components[1].items[5]", "source_row":
    {"component_name": "MgCl2・6H2O", "volume": 3, "unit": "g", "gmo_id": "GMO_001013"},
    "source_stage": "Artificial seawater", "explanation": "Source mass belongs to
    artificial-seawater preparation, not a direct main-medium concentration. Preserve
    exact salt/hydrate and mass in that stock; do not infer stock or final-medium
    rate from water input.", "calculation": "none; no final-volume assumption", "proposed_amount":
    "none asserted"}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml",
    "field_path": "ingredients[12].concentration", "ingredient": "KCl", "existing":
    {"value": "0.5", "unit": "G_PER_L"}, "decision": "conflict", "source_evidence":
    ["togo1107-api-q-1-6"], "source_locator": "$.components[1].items[6]", "source_row":
    {"component_name": "KCl", "volume": 0.5, "unit": "g", "gmo_id": "GMO_001017"},
    "source_stage": "Artificial seawater", "explanation": "Source mass belongs to
    artificial-seawater preparation, not a direct main-medium concentration. Preserve
    exact salt/hydrate and mass in that stock; do not infer stock or final-medium
    rate from water input.", "calculation": "none; no final-volume assumption", "proposed_amount":
    "none asserted"}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml",
    "field_path": "ingredients[13].concentration", "ingredient": "NaHCO3", "existing":
    {"value": "0.2", "unit": "G_PER_L"}, "decision": "conflict", "source_evidence":
    ["togo1107-api-q-1-7"], "source_locator": "$.components[1].items[7]", "source_row":
    {"component_name": "NaHCO3", "volume": 0.2, "unit": "g", "gmo_id": "GMO_001019"},
    "source_stage": "Artificial seawater", "explanation": "Source mass belongs to
    artificial-seawater preparation, not a direct main-medium concentration. Preserve
    exact salt/hydrate and mass in that stock; do not infer stock or final-medium
    rate from water input.", "calculation": "none; no final-volume assumption", "proposed_amount":
    "none asserted"}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml",
    "field_path": "ingredients[14].concentration", "ingredient": "(NH4)2SO4", "existing":
    {"value": "1", "unit": "G_PER_L"}, "decision": "conflict", "source_evidence":
    ["togo1107-api-q-1-8"], "source_locator": "$.components[1].items[8]", "source_row":
    {"component_name": "(NH4)2SO4", "volume": 1, "unit": "g", "gmo_id": "GMO_001030"},
    "source_stage": "Artificial seawater", "explanation": "Source mass belongs to
    artificial-seawater preparation, not a direct main-medium concentration. Preserve
    exact salt/hydrate and mass in that stock; do not infer stock or final-medium
    rate from water input.", "calculation": "none; no final-volume assumption", "proposed_amount":
    "none asserted"}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml",
    "field_path": "ingredients[15].concentration", "ingredient": "NaBr", "existing":
    {"value": "0.05", "unit": "G_PER_L"}, "decision": "conflict", "source_evidence":
    ["togo1107-api-q-1-9"], "source_locator": "$.components[1].items[9]", "source_row":
    {"component_name": "NaBr", "volume": 0.05, "unit": "g", "gmo_id": "GMO_001073"},
    "source_stage": "Artificial seawater", "explanation": "Source mass belongs to
    artificial-seawater preparation, not a direct main-medium concentration. Preserve
    exact salt/hydrate and mass in that stock; do not infer stock or final-medium
    rate from water input.", "calculation": "none; no final-volume assumption", "proposed_amount":
    "none asserted"}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml",
    "field_path": "ingredients[16].concentration", "ingredient": "SrCl2・6H2O", "existing":
    {"value": "0.02", "unit": "G_PER_L"}, "decision": "conflict", "source_evidence":
    ["togo1107-api-q-1-10"], "source_locator": "$.components[1].items[10]", "source_row":
    {"component_name": "SrCl2・6H2O", "volume": 0.02, "unit": "g", "gmo_id": "GMO_001085"},
    "source_stage": "Artificial seawater", "explanation": "Source mass belongs to
    artificial-seawater preparation, not a direct main-medium concentration. Preserve
    exact salt/hydrate and mass in that stock; do not infer stock or final-medium
    rate from water input.", "calculation": "none; no final-volume assumption", "proposed_amount":
    "none asserted"}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml",
    "field_path": "ingredients[17].concentration", "ingredient": "Ammonium Fe(III)
    citrate", "existing": {"value": "0.01", "unit": "G_PER_L"}, "decision": "conflict",
    "source_evidence": ["togo1107-api-q-1-11"], "source_locator": "$.components[1].items[11]",
    "source_row": {"component_name": "Ammonium Fe(III) citrate", "volume": 0.01, "unit":
    "g", "gmo_id": "GMO_001147"}, "source_stage": "Artificial seawater", "explanation":
    "Source mass belongs to artificial-seawater preparation, not a direct main-medium
    concentration. Preserve exact salt/hydrate and mass in that stock; do not infer
    stock or final-medium rate from water input.", "calculation": "none; no final-volume
    assumption", "proposed_amount": "none asserted"}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml",
    "field_path": "solutions[0].concentration", "ingredient": "Trace vitamins (see
    Medium [M190])", "existing": {"value": "5", "unit": "G_PER_L"}, "decision": "conflict",
    "source_evidence": ["togo1107-api-q-0-4"], "source_locator": "$.components[0].items[4]",
    "source_row": {"component_name": "Trace vitamins (see Medium [M190])", "volume":
    5, "unit": "ml", "reference_media_id": "M190"}, "explanation": "Source5 ml vitamin-stock
    addition belongs to the main batch. G_PER_L is the wrong dimension; final-volume
    basis for ML_PER_L is also unproved. Restore the batch dose and complete dependency
    definition.", "calculation": "none; no density or final-volume assumption", "proposed_amount":
    "none asserted"}, {"record_path": "data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml",
    "field_path": "solutions[1].concentration", "ingredient": "Trace minerals (see
    Medium [M142])", "existing": {"value": "5", "unit": "G_PER_L"}, "decision": "conflict",
    "source_evidence": ["togo1107-api-q-1-12"], "source_locator": "$.components[1].items[12]",
    "source_row": {"component_name": "Trace minerals (see Medium [M142])", "volume":
    5, "unit": "ml", "reference_media_id": "M142"}, "explanation": "Source5 ml trace-mineral
    addition belongs inside the artificial-seawater batch. G_PER_L is the wrong dimension;
    final-volume basis for ML_PER_L is also unproved. Restore the batch dose and complete
    dependency definition.", "calculation": "none; no density or final-volume assumption",
    "proposed_amount": "none asserted"}], "source_rows": [{"evidence_id": "togo1107-api-q-0-0",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107",
    "locator": "$.components[0].items[0]", "stage": "main solution 1", "source_row":
    {"component_name": "Sodium pyruvate", "volume": 5, "unit": "g", "gmo_id": "GMO_001055"},
    "decision": "evidence_only", "calculation": "none; source batch amount/input retained,
    no final-medium rate inferred"}, {"evidence_id": "togo1107-api-q-0-1", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107", "locator":
    "$.components[0].items[1]", "stage": "main solution 1", "source_row": {"component_name":
    "PIPES", "volume": 3.46, "unit": "g", "gmo_id": "GMO_001223"}, "decision": "evidence_only",
    "calculation": "none; source batch amount/input retained, no final-medium rate
    inferred"}, {"evidence_id": "togo1107-api-q-0-2", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107",
    "locator": "$.components[0].items[2]", "stage": "main solution 1", "source_row":
    {"component_name": "Yeast extract (BD-Difco)", "volume": 2, "unit": "g", "gmo_id":
    "GMO_001018"}, "decision": "evidence_only", "calculation": "none; source batch
    amount/input retained, no final-medium rate inferred"}, {"evidence_id": "togo1107-api-q-0-3",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107",
    "locator": "$.components[0].items[3]", "stage": "main solution 1", "source_row":
    {"component_name": "Tryptone (BD-Difco)", "volume": 2, "unit": "g", "gmo_id":
    "GMO_001043"}, "decision": "evidence_only", "calculation": "none; source batch
    amount/input retained, no final-medium rate inferred"}, {"evidence_id": "togo1107-api-q-0-4",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107",
    "locator": "$.components[0].items[4]", "stage": "main solution 1", "source_row":
    {"component_name": "Trace vitamins (see Medium [M190])", "volume": 5, "unit":
    "ml", "reference_media_id": "M190"}, "decision": "evidence_only", "calculation":
    "none; source batch amount/input retained, no final-medium rate inferred"}, {"evidence_id":
    "togo1107-api-q-0-5", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107",
    "locator": "$.components[0].items[5]", "stage": "main solution 1", "source_row":
    {"component_name": "Artificial seawater (see below)", "volume": 1, "unit": "L",
    "reference_media_id": "M1107"}, "decision": "evidence_only", "calculation": "none;
    source batch amount/input retained, no final-medium rate inferred"}, {"evidence_id":
    "togo1107-api-q-0-6", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107",
    "locator": "$.components[0].items[6]", "stage": "main solution 1", "source_row":
    {"component_name": "N2", "gmo_id": "GMO_002261"}, "decision": "not_quantified",
    "calculation": "none; source batch amount/input retained, no final-medium rate
    inferred"}, {"evidence_id": "togo1107-api-q-1-0", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107",
    "locator": "$.components[1].items[0]", "stage": "Artificial seawater", "source_row":
    {"component_name": "Distilled water", "volume": 1, "unit": "L", "gmo_id": "GMO_001001"},
    "decision": "evidence_only", "calculation": "none; source batch amount/input retained,
    no final-medium rate inferred"}, {"evidence_id": "togo1107-api-q-1-1", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107", "locator":
    "$.components[1].items[1]", "stage": "Artificial seawater", "source_row": {"component_name":
    "MgSO4・7H2O", "volume": 6, "unit": "g", "gmo_id": "GMO_001002"}, "decision": "evidence_only",
    "calculation": "none; source batch amount/input retained, no final-medium rate
    inferred"}, {"evidence_id": "togo1107-api-q-1-2", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107",
    "locator": "$.components[1].items[2]", "stage": "Artificial seawater", "source_row":
    {"component_name": "NaCl", "volume": 22, "unit": "g", "gmo_id": "GMO_001004"},
    "decision": "evidence_only", "calculation": "none; source batch amount/input retained,
    no final-medium rate inferred"}, {"evidence_id": "togo1107-api-q-1-3", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107", "locator":
    "$.components[1].items[3]", "stage": "Artificial seawater", "source_row": {"component_name":
    "CaCl2・2H2O", "volume": 0.3, "unit": "g", "gmo_id": "GMO_001005"}, "decision":
    "evidence_only", "calculation": "none; source batch amount/input retained, no
    final-medium rate inferred"}, {"evidence_id": "togo1107-api-q-1-4", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107", "locator":
    "$.components[1].items[4]", "stage": "Artificial seawater", "source_row": {"component_name":
    "KH2PO4", "volume": 0.42, "unit": "g", "gmo_id": "GMO_001006"}, "decision": "evidence_only",
    "calculation": "none; source batch amount/input retained, no final-medium rate
    inferred"}, {"evidence_id": "togo1107-api-q-1-5", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107",
    "locator": "$.components[1].items[5]", "stage": "Artificial seawater", "source_row":
    {"component_name": "MgCl2・6H2O", "volume": 3, "unit": "g", "gmo_id": "GMO_001013"},
    "decision": "evidence_only", "calculation": "none; source batch amount/input retained,
    no final-medium rate inferred"}, {"evidence_id": "togo1107-api-q-1-6", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107", "locator":
    "$.components[1].items[6]", "stage": "Artificial seawater", "source_row": {"component_name":
    "KCl", "volume": 0.5, "unit": "g", "gmo_id": "GMO_001017"}, "decision": "evidence_only",
    "calculation": "none; source batch amount/input retained, no final-medium rate
    inferred"}, {"evidence_id": "togo1107-api-q-1-7", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107",
    "locator": "$.components[1].items[7]", "stage": "Artificial seawater", "source_row":
    {"component_name": "NaHCO3", "volume": 0.2, "unit": "g", "gmo_id": "GMO_001019"},
    "decision": "evidence_only", "calculation": "none; source batch amount/input retained,
    no final-medium rate inferred"}, {"evidence_id": "togo1107-api-q-1-8", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107", "locator":
    "$.components[1].items[8]", "stage": "Artificial seawater", "source_row": {"component_name":
    "(NH4)2SO4", "volume": 1, "unit": "g", "gmo_id": "GMO_001030"}, "decision": "evidence_only",
    "calculation": "none; source batch amount/input retained, no final-medium rate
    inferred"}, {"evidence_id": "togo1107-api-q-1-9", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107",
    "locator": "$.components[1].items[9]", "stage": "Artificial seawater", "source_row":
    {"component_name": "NaBr", "volume": 0.05, "unit": "g", "gmo_id": "GMO_001073"},
    "decision": "evidence_only", "calculation": "none; source batch amount/input retained,
    no final-medium rate inferred"}, {"evidence_id": "togo1107-api-q-1-10", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107", "locator":
    "$.components[1].items[10]", "stage": "Artificial seawater", "source_row": {"component_name":
    "SrCl2・6H2O", "volume": 0.02, "unit": "g", "gmo_id": "GMO_001085"}, "decision":
    "evidence_only", "calculation": "none; source batch amount/input retained, no
    final-medium rate inferred"}, {"evidence_id": "togo1107-api-q-1-11", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107", "locator":
    "$.components[1].items[11]", "stage": "Artificial seawater", "source_row": {"component_name":
    "Ammonium Fe(III) citrate", "volume": 0.01, "unit": "g", "gmo_id": "GMO_001147"},
    "decision": "evidence_only", "calculation": "none; source batch amount/input retained,
    no final-medium rate inferred"}, {"evidence_id": "togo1107-api-q-1-12", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1107", "locator":
    "$.components[1].items[12]", "stage": "Artificial seawater", "source_row": {"component_name":
    "Trace minerals (see Medium [M142])", "volume": 5, "unit": "ml", "reference_media_id":
    "M142"}, "decision": "evidence_only", "calculation": "none; source batch amount/input
    retained, no final-medium rate inferred"}, {"evidence_id": "togo142-api-q-2-0",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
    "locator": "$.components[2].items[0]", "stage": "Trace minerals", "source_row":
    {"component_name": "Distilled water", "volume": 1, "unit": "L", "gmo_id": "GMO_001001"},
    "decision": "evidence_only", "calculation": "none; source batch amount/input retained,
    no final-medium rate inferred"}, {"evidence_id": "togo142-api-q-2-1", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "locator":
    "$.components[2].items[1]", "stage": "Trace minerals", "source_row": {"component_name":
    "MgSO4・7H2O", "volume": 3, "unit": "g", "gmo_id": "GMO_001002"}, "decision": "evidence_only",
    "calculation": "none; source batch amount/input retained, no final-medium rate
    inferred"}, {"evidence_id": "togo142-api-q-2-2", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
    "locator": "$.components[2].items[2]", "stage": "Trace minerals", "source_row":
    {"component_name": "NaCl", "volume": 1, "unit": "g", "gmo_id": "GMO_001004"},
    "decision": "evidence_only", "calculation": "none; source batch amount/input retained,
    no final-medium rate inferred"}, {"evidence_id": "togo142-api-q-2-3", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "locator":
    "$.components[2].items[3]", "stage": "Trace minerals", "source_row": {"component_name":
    "CaCl2・2H2O", "volume": 0.1, "unit": "g", "gmo_id": "GMO_001005"}, "decision":
    "evidence_only", "calculation": "none; source batch amount/input retained, no
    final-medium rate inferred"}, {"evidence_id": "togo142-api-q-2-4", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "locator":
    "$.components[2].items[4]", "stage": "Trace minerals", "source_row": {"component_name":
    "Na2MoO4・2H2O", "volume": 0.01, "unit": "g", "gmo_id": "GMO_001011"}, "decision":
    "evidence_only", "calculation": "none; source batch amount/input retained, no
    final-medium rate inferred"}, {"evidence_id": "togo142-api-q-2-5", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "locator":
    "$.components[2].items[5]", "stage": "Trace minerals", "source_row": {"component_name":
    "H3BO3", "volume": 0.01, "unit": "g", "gmo_id": "GMO_001015"}, "decision": "evidence_only",
    "calculation": "none; source batch amount/input retained, no final-medium rate
    inferred"}, {"evidence_id": "togo142-api-q-2-6", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142",
    "locator": "$.components[2].items[6]", "stage": "Trace minerals", "source_row":
    {"component_name": "FeSO4・7H2O", "volume": 0.1, "unit": "g", "gmo_id": "GMO_001016"},
    "decision": "evidence_only", "calculation": "none; source batch amount/input retained,
    no final-medium rate inferred"}, {"evidence_id": "togo142-api-q-2-7", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "locator":
    "$.components[2].items[7]", "stage": "Trace minerals", "source_row": {"component_name":
    "ZnSO4・7H2O", "volume": 0.1, "unit": "g", "gmo_id": "GMO_001023"}, "decision":
    "evidence_only", "calculation": "none; source batch amount/input retained, no
    final-medium rate inferred"}, {"evidence_id": "togo142-api-q-2-8", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "locator":
    "$.components[2].items[8]", "stage": "Trace minerals", "source_row": {"component_name":
    "CuSO4・5H2O", "volume": 0.01, "unit": "g", "gmo_id": "GMO_001039"}, "decision":
    "evidence_only", "calculation": "none; source batch amount/input retained, no
    final-medium rate inferred"}, {"evidence_id": "togo142-api-q-2-9", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "locator":
    "$.components[2].items[9]", "stage": "Trace minerals", "source_row": {"component_name":
    "CoSO4・7H2O", "volume": 0.1, "unit": "g", "gmo_id": "GMO_001050"}, "decision":
    "evidence_only", "calculation": "none; source batch amount/input retained, no
    final-medium rate inferred"}, {"evidence_id": "togo142-api-q-2-10", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "locator":
    "$.components[2].items[10]", "stage": "Trace minerals", "source_row": {"component_name":
    "Nitrilotriacetic acid", "volume": 1.5, "unit": "g", "gmo_id": "GMO_001053"},
    "decision": "evidence_only", "calculation": "none; source batch amount/input retained,
    no final-medium rate inferred"}, {"evidence_id": "togo142-api-q-2-11", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "locator":
    "$.components[2].items[11]", "stage": "Trace minerals", "source_row": {"component_name":
    "MnSO4・xH2O", "volume": 0.5, "unit": "g", "gmo_id": "GMO_001065"}, "decision":
    "evidence_only", "calculation": "none; source batch amount/input retained, no
    final-medium rate inferred"}, {"evidence_id": "togo142-api-q-2-12", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "locator":
    "$.components[2].items[12]", "stage": "Trace minerals", "source_row": {"component_name":
    "AlK(SO4)2", "volume": 0.01, "unit": "g", "gmo_id": "GMO_001088"}, "decision":
    "evidence_only", "calculation": "none; source batch amount/input retained, no
    final-medium rate inferred"}, {"evidence_id": "togo142-api-q-2-13", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142", "locator":
    "$.components[2].items[13]", "stage": "Trace minerals", "source_row": {"component_name":
    "KOH solution", "gmo_id": "GMO_001903"}, "decision": "not_quantified", "calculation":
    "none; source batch amount/input retained, no final-medium rate inferred"}, {"evidence_id":
    "togo190-api-q-1-0", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
    "locator": "$.components[1].items[0]", "stage": "Trace vitamins", "source_row":
    {"component_name": "Distilled water", "volume": 1, "unit": "L", "gmo_id": "GMO_001001"},
    "decision": "evidence_only", "calculation": "none; source batch amount/input retained,
    no final-medium rate inferred"}, {"evidence_id": "togo190-api-q-1-1", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "locator":
    "$.components[1].items[1]", "stage": "Trace vitamins", "source_row": {"component_name":
    "Biotin", "volume": 2, "unit": "mg", "gmo_id": "GMO_001025"}, "decision": "evidence_only",
    "calculation": "none; source batch amount/input retained, no final-medium rate
    inferred"}, {"evidence_id": "togo190-api-q-1-2", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
    "locator": "$.components[1].items[2]", "stage": "Trace vitamins", "source_row":
    {"component_name": "p--Aminobenzoic acid", "volume": 5, "unit": "mg", "gmo_id":
    "GMO_001026"}, "decision": "evidence_only", "calculation": "none; source batch
    amount/input retained, no final-medium rate inferred"}, {"evidence_id": "togo190-api-q-1-3",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
    "locator": "$.components[1].items[3]", "stage": "Trace vitamins", "source_row":
    {"component_name": "Thiamine・HCl", "volume": 5, "unit": "mg", "gmo_id": "GMO_001027"},
    "decision": "evidence_only", "calculation": "none; source batch amount/input retained,
    no final-medium rate inferred"}, {"evidence_id": "togo190-api-q-1-4", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "locator":
    "$.components[1].items[4]", "stage": "Trace vitamins", "source_row": {"component_name":
    "Calcium pantothenate", "volume": 5, "unit": "mg", "gmo_id": "GMO_001028"}, "decision":
    "evidence_only", "calculation": "none; source batch amount/input retained, no
    final-medium rate inferred"}, {"evidence_id": "togo190-api-q-1-5", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "locator":
    "$.components[1].items[5]", "stage": "Trace vitamins", "source_row": {"component_name":
    "Pyridoxine・HCl", "volume": 10, "unit": "mg", "gmo_id": "GMO_001029"}, "decision":
    "evidence_only", "calculation": "none; source batch amount/input retained, no
    final-medium rate inferred"}, {"evidence_id": "togo190-api-q-1-6", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "locator":
    "$.components[1].items[6]", "stage": "Trace vitamins", "source_row": {"component_name":
    "Folic acid", "volume": 2, "unit": "mg", "gmo_id": "GMO_001033"}, "decision":
    "evidence_only", "calculation": "none; source batch amount/input retained, no
    final-medium rate inferred"}, {"evidence_id": "togo190-api-q-1-7", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "locator":
    "$.components[1].items[7]", "stage": "Trace vitamins", "source_row": {"component_name":
    "Vitamin B12", "volume": 0.1, "unit": "mg", "gmo_id": "GMO_001034"}, "decision":
    "evidence_only", "calculation": "none; source batch amount/input retained, no
    final-medium rate inferred"}, {"evidence_id": "togo190-api-q-1-8", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "locator":
    "$.components[1].items[8]", "stage": "Trace vitamins", "source_row": {"component_name":
    "Riboflavin", "volume": 5, "unit": "mg", "gmo_id": "GMO_001037"}, "decision":
    "evidence_only", "calculation": "none; source batch amount/input retained, no
    final-medium rate inferred"}, {"evidence_id": "togo190-api-q-1-9", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "locator":
    "$.components[1].items[9]", "stage": "Trace vitamins", "source_row": {"component_name":
    "Nicotinic acid", "volume": 5, "unit": "mg", "gmo_id": "GMO_001038"}, "decision":
    "evidence_only", "calculation": "none; source batch amount/input retained, no
    final-medium rate inferred"}, {"evidence_id": "togo190-api-q-1-10", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "locator":
    "$.components[1].items[10]", "stage": "Trace vitamins", "source_row": {"component_name":
    "Lipoic acid", "volume": 5, "unit": "mg", "gmo_id": "GMO_001699"}, "decision":
    "evidence_only", "calculation": "none; source batch amount/input retained, no
    final-medium rate inferred"}], "corroborating_mediadive_rows": [{"solution_id":
    5101, "solution_name": "Main sol. J1042", "provider_volume_ml": 1005, "locator":
    "$.data.solutions[0].recipe[0]", "source_row": {"recipe_order": 1, "compound":
    "Yeast extract", "compound_id": 16, "attribute": "BD-Difco", "amount": 2, "unit":
    "g", "g_l": 1.99005, "optional": 0}}, {"solution_id": 5101, "solution_name": "Main
    sol. J1042", "provider_volume_ml": 1005, "locator": "$.data.solutions[0].recipe[1]",
    "source_row": {"recipe_order": 2, "compound": "Tryptone", "compound_id": 71, "attribute":
    "BD-Difco", "amount": 2, "unit": "g", "g_l": 1.99005, "mmol_l": 27.9973, "optional":
    0}}, {"solution_id": 5101, "solution_name": "Main sol. J1042", "provider_volume_ml":
    1005, "locator": "$.data.solutions[0].recipe[2]", "source_row": {"recipe_order":
    3, "compound": "Sodium pyruvate", "compound_id": 438, "amount": 5, "unit": "g",
    "g_l": 4.97512, "mmol_l": 45.212, "optional": 0}}, {"solution_id": 5101, "solution_name":
    "Main sol. J1042", "provider_volume_ml": 1005, "locator": "$.data.solutions[0].recipe[3]",
    "source_row": {"recipe_order": 4, "compound": "PIPES", "compound_id": 398, "amount":
    3.46, "unit": "g", "g_l": 3.44279, "mmol_l": 11.3849, "optional": 0}}, {"solution_id":
    5101, "solution_name": "Main sol. J1042", "provider_volume_ml": 1005, "locator":
    "$.data.solutions[0].recipe[4]", "source_row": {"recipe_order": 5, "solution":
    "Trace vitamins", "solution_id": 3861, "amount": 5, "unit": "ml", "optional":
    0}}, {"solution_id": 5101, "solution_name": "Main sol. J1042", "provider_volume_ml":
    1005, "locator": "$.data.solutions[0].recipe[5]", "source_row": {"recipe_order":
    6, "solution": "Artificial seawater", "solution_id": 5102, "amount": 1000, "unit":
    "ml", "optional": 0}}, {"solution_id": 5102, "solution_name": "Artificial seawater",
    "provider_volume_ml": 1005, "locator": "$.data.solutions[1].recipe[0]", "source_row":
    {"recipe_order": 1, "compound": "NaCl", "compound_id": 43, "amount": 22, "unit":
    "g", "g_l": 21.8905, "mmol_l": 374.582, "optional": 0}}, {"solution_id": 5102,
    "solution_name": "Artificial seawater", "provider_volume_ml": 1005, "locator":
    "$.data.solutions[1].recipe[1]", "source_row": {"recipe_order": 2, "compound":
    "MgCl2 x 6 H2O", "compound_id": 79, "amount": 3, "unit": "g", "g_l": 2.98507,
    "mmol_l": 14.6829, "optional": 0}}, {"solution_id": 5102, "solution_name": "Artificial
    seawater", "provider_volume_ml": 1005, "locator": "$.data.solutions[1].recipe[2]",
    "source_row": {"recipe_order": 3, "compound": "MgSO4 x 7 H2O", "compound_id":
    8, "amount": 6, "unit": "g", "g_l": 5.97015, "mmol_l": 24.222, "optional": 0}},
    {"solution_id": 5102, "solution_name": "Artificial seawater", "provider_volume_ml":
    1005, "locator": "$.data.solutions[1].recipe[3]", "source_row": {"recipe_order":
    4, "compound": "(NH4)2SO4", "compound_id": 27, "amount": 1, "unit": "g", "g_l":
    0.995025, "mmol_l": 7.53008, "optional": 0}}, {"solution_id": 5102, "solution_name":
    "Artificial seawater", "provider_volume_ml": 1005, "locator": "$.data.solutions[1].recipe[4]",
    "source_row": {"recipe_order": 5, "compound": "NaHCO3", "compound_id": 55, "amount":
    0.2, "unit": "g", "g_l": 0.199005, "mmol_l": 2.36891, "optional": 0}}, {"solution_id":
    5102, "solution_name": "Artificial seawater", "provider_volume_ml": 1005, "locator":
    "$.data.solutions[1].recipe[5]", "source_row": {"recipe_order": 6, "compound":
    "CaCl2 x 2 H2O", "compound_id": 7, "amount": 0.3, "unit": "g", "g_l": 0.298507,
    "mmol_l": 2.03046, "optional": 0}}, {"solution_id": 5102, "solution_name": "Artificial
    seawater", "provider_volume_ml": 1005, "locator": "$.data.solutions[1].recipe[6]",
    "source_row": {"recipe_order": 7, "compound": "KCl", "compound_id": 61, "amount":
    0.5, "unit": "g", "g_l": 0.497512, "mmol_l": 6.67354, "optional": 0}}, {"solution_id":
    5102, "solution_name": "Artificial seawater", "provider_volume_ml": 1005, "locator":
    "$.data.solutions[1].recipe[7]", "source_row": {"recipe_order": 8, "compound":
    "KH2PO4", "compound_id": 11, "amount": 0.42, "unit": "g", "g_l": 0.41791, "mmol_l":
    3.07093, "optional": 0}}, {"solution_id": 5102, "solution_name": "Artificial seawater",
    "provider_volume_ml": 1005, "locator": "$.data.solutions[1].recipe[8]", "source_row":
    {"recipe_order": 9, "compound": "NaBr", "compound_id": 353, "amount": 0.05, "unit":
    "g", "g_l": 0.0497512, "mmol_l": 0.483538, "optional": 0}}, {"solution_id": 5102,
    "solution_name": "Artificial seawater", "provider_volume_ml": 1005, "locator":
    "$.data.solutions[1].recipe[9]", "source_row": {"recipe_order": 10, "compound":
    "SrCl2 x 6 H2O", "compound_id": 176, "amount": 0.02, "unit": "g", "g_l": 0.0199005,
    "mmol_l": 0.0746408, "optional": 0}}, {"solution_id": 5102, "solution_name": "Artificial
    seawater", "provider_volume_ml": 1005, "locator": "$.data.solutions[1].recipe[10]",
    "source_row": {"recipe_order": 11, "compound": "Ammonium ferric citrate", "compound_id":
    2007, "amount": 0.01, "unit": "g", "g_l": 0.00995025, "optional": 0}}, {"solution_id":
    5102, "solution_name": "Artificial seawater", "provider_volume_ml": 1005, "locator":
    "$.data.solutions[1].recipe[11]", "source_row": {"recipe_order": 12, "solution":
    "Trace minerals", "solution_id": 3804, "amount": 5, "unit": "ml", "optional":
    0}}, {"solution_id": 5102, "solution_name": "Artificial seawater", "provider_volume_ml":
    1005, "locator": "$.data.solutions[1].recipe[12]", "source_row": {"recipe_order":
    13, "compound": "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml",
    "optional": 0}}, {"solution_id": 3861, "solution_name": "Trace vitamins", "provider_volume_ml":
    1000, "locator": "$.data.solutions[2].recipe[0]", "source_row": {"recipe_order":
    1, "compound": "Biotin", "compound_id": 46, "amount": 2, "unit": "mg", "g_l":
    0.002, "mmol_l": 0.00818632, "optional": 0}}, {"solution_id": 3861, "solution_name":
    "Trace vitamins", "provider_volume_ml": 1000, "locator": "$.data.solutions[2].recipe[1]",
    "source_row": {"recipe_order": 2, "compound": "Folic acid", "compound_id": 138,
    "amount": 2, "unit": "mg", "g_l": 0.002, "mmol_l": 0.00453104, "optional": 0}},
    {"solution_id": 3861, "solution_name": "Trace vitamins", "provider_volume_ml":
    1000, "locator": "$.data.solutions[2].recipe[2]", "source_row": {"recipe_order":
    3, "compound": "Pyridoxine hydrochloride", "compound_id": 519, "amount": 10, "unit":
    "mg", "g_l": 0.01, "mmol_l": 0.0486287, "optional": 0}}, {"solution_id": 3861,
    "solution_name": "Trace vitamins", "provider_volume_ml": 1000, "locator": "$.data.solutions[2].recipe[3]",
    "source_row": {"recipe_order": 4, "compound": "Thiamine HCl", "compound_id": 1207,
    "amount": 5, "unit": "mg", "g_l": 0.005, "mmol_l": 0.0148236, "optional": 0}},
    {"solution_id": 3861, "solution_name": "Trace vitamins", "provider_volume_ml":
    1000, "locator": "$.data.solutions[2].recipe[4]", "source_row": {"recipe_order":
    5, "compound": "Riboflavin", "compound_id": 136, "amount": 5, "unit": "mg", "g_l":
    0.005, "mmol_l": 0.0132837, "optional": 0}}, {"solution_id": 3861, "solution_name":
    "Trace vitamins", "provider_volume_ml": 1000, "locator": "$.data.solutions[2].recipe[5]",
    "source_row": {"recipe_order": 6, "compound": "Nicotinic acid", "compound_id":
    139, "amount": 5, "unit": "mg", "g_l": 0.005, "mmol_l": 0.0406141, "optional":
    0}}, {"solution_id": 3861, "solution_name": "Trace vitamins", "provider_volume_ml":
    1000, "locator": "$.data.solutions[2].recipe[6]", "source_row": {"recipe_order":
    7, "compound": "Calcium pantothenate", "compound_id": 518, "amount": 5, "unit":
    "mg", "g_l": 0.005, "mmol_l": 0.0104925, "optional": 0}}, {"solution_id": 3861,
    "solution_name": "Trace vitamins", "provider_volume_ml": 1000, "locator": "$.data.solutions[2].recipe[7]",
    "source_row": {"recipe_order": 8, "compound": "Vitamin B12", "compound_id": 18,
    "amount": 0.1, "unit": "mg", "g_l": 0.0001, "mmol_l": 7.3779e-05, "optional":
    0}}, {"solution_id": 3861, "solution_name": "Trace vitamins", "provider_volume_ml":
    1000, "locator": "$.data.solutions[2].recipe[8]", "source_row": {"recipe_order":
    9, "compound": "p-Aminobenzoic acid", "compound_id": 47, "amount": 5, "unit":
    "mg", "g_l": 0.005, "mmol_l": 0.0364591, "optional": 0}}, {"solution_id": 3861,
    "solution_name": "Trace vitamins", "provider_volume_ml": 1000, "locator": "$.data.solutions[2].recipe[9]",
    "source_row": {"recipe_order": 10, "compound": "Lipoic acid", "compound_id": 368,
    "amount": 5, "unit": "mg", "g_l": 0.005, "mmol_l": 0.024233, "optional": 0}},
    {"solution_id": 3861, "solution_name": "Trace vitamins", "provider_volume_ml":
    1000, "locator": "$.data.solutions[2].recipe[10]", "source_row": {"recipe_order":
    11, "compound": "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml",
    "optional": 0}}, {"solution_id": 3804, "solution_name": "Trace minerals", "provider_volume_ml":
    1000, "locator": "$.data.solutions[3].recipe[0]", "source_row": {"recipe_order":
    1, "compound": "Nitrilotriacetic acid", "compound_id": 189, "amount": 1.5, "unit":
    "g", "g_l": 1.5, "mmol_l": 7.84765, "optional": 0}}, {"solution_id": 3804, "solution_name":
    "Trace minerals", "provider_volume_ml": 1000, "locator": "$.data.solutions[3].recipe[1]",
    "source_row": {"recipe_order": 2, "compound": "MgSO4 x 7 H2O", "compound_id":
    8, "amount": 3, "unit": "g", "g_l": 3, "mmol_l": 12.1716, "optional": 0}}, {"solution_id":
    3804, "solution_name": "Trace minerals", "provider_volume_ml": 1000, "locator":
    "$.data.solutions[3].recipe[2]", "source_row": {"recipe_order": 3, "compound":
    "MnSO4 x n H2O", "compound_id": 1000, "amount": 0.5, "unit": "g", "g_l": 0.5,
    "optional": 0}}, {"solution_id": 3804, "solution_name": "Trace minerals", "provider_volume_ml":
    1000, "locator": "$.data.solutions[3].recipe[3]", "source_row": {"recipe_order":
    4, "compound": "NaCl", "compound_id": 43, "amount": 1, "unit": "g", "g_l": 1,
    "mmol_l": 17.1116, "optional": 0}}, {"solution_id": 3804, "solution_name": "Trace
    minerals", "provider_volume_ml": 1000, "locator": "$.data.solutions[3].recipe[4]",
    "source_row": {"recipe_order": 5, "compound": "FeSO4 x 7 H2O", "compound_id":
    12, "amount": 0.1, "unit": "g", "g_l": 0.1, "mmol_l": 0.359693, "optional": 0}},
    {"solution_id": 3804, "solution_name": "Trace minerals", "provider_volume_ml":
    1000, "locator": "$.data.solutions[3].recipe[5]", "source_row": {"recipe_order":
    6, "compound": "CoSO4 x 7 H2O", "compound_id": 198, "amount": 0.1, "unit": "g",
    "g_l": 0.1, "mmol_l": 0.645178, "optional": 0}}, {"solution_id": 3804, "solution_name":
    "Trace minerals", "provider_volume_ml": 1000, "locator": "$.data.solutions[3].recipe[6]",
    "source_row": {"recipe_order": 7, "compound": "CaCl2 x 2 H2O", "compound_id":
    7, "amount": 0.1, "unit": "g", "g_l": 0.1, "mmol_l": 0.680203, "optional": 0}},
    {"solution_id": 3804, "solution_name": "Trace minerals", "provider_volume_ml":
    1000, "locator": "$.data.solutions[3].recipe[7]", "source_row": {"recipe_order":
    8, "compound": "ZnSO4 x 7 H2O", "compound_id": 35, "amount": 0.1, "unit": "g",
    "g_l": 0.1, "mmol_l": 0.347752, "optional": 0}}, {"solution_id": 3804, "solution_name":
    "Trace minerals", "provider_volume_ml": 1000, "locator": "$.data.solutions[3].recipe[8]",
    "source_row": {"recipe_order": 9, "compound": "CuSO4 x 5 H2O", "compound_id":
    121, "amount": 0.01, "unit": "g", "g_l": 0.01, "mmol_l": 0.0400503, "optional":
    0}}, {"solution_id": 3804, "solution_name": "Trace minerals", "provider_volume_ml":
    1000, "locator": "$.data.solutions[3].recipe[9]", "source_row": {"recipe_order":
    10, "compound": "AlK(SO4)2", "compound_id": 1015, "amount": 0.01, "unit": "g",
    "g_l": 0.01, "mmol_l": 0.0387289, "optional": 0}}, {"solution_id": 3804, "solution_name":
    "Trace minerals", "provider_volume_ml": 1000, "locator": "$.data.solutions[3].recipe[10]",
    "source_row": {"recipe_order": 11, "compound": "H3BO3", "compound_id": 37, "amount":
    0.01, "unit": "g", "g_l": 0.01, "mmol_l": 0.161708, "optional": 0}}, {"solution_id":
    3804, "solution_name": "Trace minerals", "provider_volume_ml": 1000, "locator":
    "$.data.solutions[3].recipe[11]", "source_row": {"recipe_order": 12, "compound":
    "Na2MoO4 x 2 H2O", "compound_id": 9, "amount": 0.01, "unit": "g", "g_l": 0.01,
    "mmol_l": 0.0413309, "optional": 0}}, {"solution_id": 3804, "solution_name": "Trace
    minerals", "provider_volume_ml": 1000, "locator": "$.data.solutions[3].recipe[12]",
    "source_row": {"recipe_order": 13, "compound": "Distilled water", "compound_id":
    4, "amount": 1000, "unit": "ml", "optional": 0}}], "source_only_notes": ["Trace
    minerals contains12 solutes plus water1 L and unquantified KOH; retain pH6.5 dissolution
    then7.0 adjustment at this stock stage.", "Trace vitamins contains10 constituents
    plus water1 L; generic calcium pantothenate, B12 and lipoic-acid forms do not
    justify more specific stereochemical or vitamer claims.", "M1107 main pH7.0, N2
    atmosphere, butyl rubber stoppers and autoclaving are supported. No incubation
    temperature, duration or strain-growth claim was extracted.", "M190-specific vitamin
    filtration underN2 is a dependency-context instruction; resolve its compatibility
    with M1107 autoclave prose before transferring it.", "Exclude the M142 parent
    recipe and10 ml receiving dose, M190 parent10 ml vitamin dose, parent pH6.8/N2-CO2,
    and M190 separate mineral formulation.", "MediaDive43 recipe rows are preserved
    as reported database context; g_l and mmol_l are not automatically independently
    verified final concentrations."]}'
- assessment_id: topology
  area: representation
  topic: Main medium, seawater and two stock definitions
  outcome: concern
  summary: Eleven seawater solutes are flattened into main ingredients; trace minerals
    is attached at the wrong receiving level and both references lack composition.
  target_ids:
  - CultureMech:007626
  evidence_ids:
  - target
  - owner
  - togo1107-api
  - togo142-api
  - togo190-api
  - jcm151
  - jcm197
  details: Main batch has four solute masses, vitamin-stock5 ml and prepared seawater1
    L plus N2 handling. Seawater has11 solute masses, water1 L and trace-mineral stock5
    ml. The mineral and vitamin tables define12 and10 solutes respectively. Do not
    sum same-name substances across stages or substitute JCM197’s different mineral
    stock. The local Unknown solution name defaults do not erase the meaningful preferred
    terms.
- assessment_id: preparation
  area: completeness
  topic: Preparation, pH and condition boundaries
  outcome: concern
  summary: Selected record and owner omit the available main preparation and pH7.0;
    gas is left as a VARIABLE ingredient.
  target_ids:
  - CultureMech:007626
  evidence_ids:
  - target
  - owner
  - togo1107-api
  - mediadiveJ1042
  - jcm151
  - jcm197
  details: 'Retain source order: pH7, distribute underN2, butyl rubber stoppers, autoclave.
    Main source gives no temperature/time. General121°C15 min notices on dependency
    pages are not automatically authority for unavailable JCM1042. Stock-mineral pH6.5→7
    is separate. Vitamin filtration is contextual to M190 and needs explicit applicability
    review. LIQUID/COMPLEX/UNDEFINED align with the ungelling yeast/tryptone formulation;
    optional role and organism fields are not invented.'
- assessment_id: grounding
  area: grounding
  topic: Exact existing chemical identities and MIM linkage
  outcome: supported
  summary: All14 distinct asserted CHEBI identifiers have current matching nonobsolete
    labels; nine existing secondary links agree with maintained resolver output.
  target_ids:
  - CultureMech:007626
  evidence_ids:
  - target
  - owner
  - mim-index
  - mim-metadata
  - diagnostics
  - chebi-15377
  - chebi-17997
  - chebi-26710
  - chebi-31795
  - chebi-32139
  - chebi-32588
  - chebi-36385
  - chebi-39033
  - chebi-50144
  - chebi-62946
  - chebi-63004
  - chebi-63036
  - chebi-86158
  - chebi-86345
  details: '[{"field": "ingredients[0]", "label": "Sodium pyruvate", "primary": {"id":
    "CHEBI:50144", "label": "sodium pyruvate"}, "secondary": {"id": "CHEBI:50144",
    "label": "sodium pyruvate"}, "legacy": null, "decision": {"query_label": "Sodium
    pyruvate", "identifier": "CHEBI:50144", "ontology_id": "CHEBI:50144", "mim_preferred_term":
    "Na-pyruvate", "matched_label": "Sodium Pyruvate", "match_type": "synonym", "mapping_status":
    "MAPPED", "ambiguity": "unique", "resolution_source": "mim_exact", "local_identifier":
    "CHEBI:50144", "source_compound_id": null, "reason": "trusted MIM label-index
    answer"}}, {"field": "ingredients[1]", "label": "PIPES", "primary": {"id": "CHEBI:39033",
    "label": "PIPES"}, "secondary": {"id": "CHEBI:39033", "label": "PIPES"}, "legacy":
    null, "decision": {"query_label": "PIPES", "identifier": "CHEBI:39033", "ontology_id":
    "CHEBI:39033", "mim_preferred_term": "PIPES", "matched_label": "PIPES", "match_type":
    "preferred_term", "mapping_status": "MAPPED", "ambiguity": "unique", "resolution_source":
    "mim_exact", "local_identifier": "CHEBI:39033", "source_compound_id": null, "reason":
    "trusted MIM label-index answer"}}, {"field": "ingredients[2]", "label": "Yeast
    extract (BD-Difco)", "primary": null, "secondary": null, "legacy": null, "decision":
    {"query_label": "Yeast extract (BD-Difco)", "identifier": "FOODON:03315426", "ontology_id":
    "FOODON:03315426", "mim_preferred_term": "Yeast extract", "matched_label": "Yeast
    extract (BD-Difco)", "match_type": "synonym", "mapping_status": "MAPPED", "ambiguity":
    "unique", "resolution_source": "mim_exact", "local_identifier": null, "source_compound_id":
    null, "reason": "trusted MIM label-index answer"}}, {"field": "ingredients[3]",
    "label": "Tryptone (BD-Difco)", "primary": null, "secondary": null, "legacy":
    null, "decision": {"query_label": "Tryptone (BD-Difco)", "identifier": "MICRO:0000182",
    "ontology_id": "MICRO:0000182", "mim_preferred_term": "Tryptone", "matched_label":
    "Tryptone (BD-Difco)", "match_type": "synonym", "mapping_status": "MAPPED", "ambiguity":
    "unique", "resolution_source": "mim_exact", "local_identifier": null, "source_compound_id":
    null, "reason": "trusted MIM label-index answer"}}, {"field": "ingredients[4]",
    "label": "Artificial seawater (see below)", "primary": null, "secondary": null,
    "legacy": null, "decision": {"query_label": "Artificial seawater (see below)",
    "identifier": "MICRO:0001715", "ontology_id": "MICRO:0001715", "mim_preferred_term":
    "Artificial seawater", "matched_label": "Artificial seawater (see below)", "match_type":
    "synonym", "mapping_status": "MAPPED", "ambiguity": "unique", "resolution_source":
    "mim_exact", "local_identifier": null, "source_compound_id": null, "reason": "trusted
    MIM label-index answer"}}, {"field": "ingredients[5]", "label": "N2", "primary":
    {"id": "CHEBI:17997", "label": "dinitrogen"}, "secondary": null, "legacy": null,
    "decision": {"query_label": "N2", "identifier": "CHEBI:17997", "ontology_id":
    "CHEBI:17997", "mim_preferred_term": "Nitrogen gas", "matched_label": "N2", "match_type":
    "synonym", "mapping_status": "MAPPED", "ambiguity": "unique", "resolution_source":
    "mim_exact", "local_identifier": "CHEBI:17997", "source_compound_id": null, "reason":
    "trusted MIM label-index answer"}}, {"field": "ingredients[6]", "label": "Distilled
    water", "primary": {"id": "CHEBI:15377", "label": "water"}, "secondary": {"id":
    "CHEBI:15377", "label": "water"}, "legacy": null, "decision": {"query_label":
    "Distilled water", "identifier": "CHEBI:15377", "ontology_id": "CHEBI:15377",
    "mim_preferred_term": "Distilled water", "matched_label": "Distilled water", "match_type":
    "preferred_term", "mapping_status": "MAPPED", "ambiguity": "unique", "resolution_source":
    "mim_exact", "local_identifier": "CHEBI:15377", "source_compound_id": null, "reason":
    "trusted MIM label-index answer"}}, {"field": "ingredients[7]", "label": "MgSO4・7H2O",
    "primary": {"id": "CHEBI:31795", "label": "magnesium sulfate heptahydrate"}, "secondary":
    null, "legacy": null, "decision": {"query_label": "MgSO4・7H2O", "identifier":
    "CHEBI:31795", "ontology_id": null, "mim_preferred_term": null, "matched_label":
    null, "match_type": null, "mapping_status": null, "ambiguity": null, "resolution_source":
    "local_fallback", "local_identifier": "CHEBI:31795", "source_compound_id": null,
    "reason": "label not found in pinned MIM index; retained local identity"}}, {"field":
    "ingredients[8]", "label": "NaCl", "primary": {"id": "CHEBI:26710", "label": "sodium
    chloride"}, "secondary": {"id": "CHEBI:26710", "label": "sodium chloride"}, "legacy":
    null, "decision": {"query_label": "NaCl", "identifier": "CHEBI:26710", "ontology_id":
    "CHEBI:26710", "mim_preferred_term": "NaCl", "matched_label": "NaCl", "match_type":
    "preferred_term", "mapping_status": "MAPPED", "ambiguity": "unique", "resolution_source":
    "mim_exact", "local_identifier": "CHEBI:26710", "source_compound_id": null, "reason":
    "trusted MIM label-index answer"}}, {"field": "ingredients[9]", "label": "CaCl2・2H2O",
    "primary": {"id": "CHEBI:86158", "label": "calcium chloride dihydrate"}, "secondary":
    null, "legacy": null, "decision": {"query_label": "CaCl2・2H2O", "identifier":
    "CHEBI:86158", "ontology_id": null, "mim_preferred_term": null, "matched_label":
    null, "match_type": null, "mapping_status": null, "ambiguity": null, "resolution_source":
    "local_fallback", "local_identifier": "CHEBI:86158", "source_compound_id": null,
    "reason": "label not found in pinned MIM index; retained local identity"}}, {"field":
    "ingredients[10]", "label": "KH2PO4", "primary": {"id": "CHEBI:63036", "label":
    "potassium dihydrogen phosphate"}, "secondary": {"id": "CHEBI:63036", "label":
    "potassium dihydrogen phosphate"}, "legacy": null, "decision": {"query_label":
    "KH2PO4", "identifier": "CHEBI:63036", "ontology_id": "CHEBI:63036", "mim_preferred_term":
    "KH2PO4", "matched_label": "KH2PO4", "match_type": "preferred_term", "mapping_status":
    "MAPPED", "ambiguity": "unique", "resolution_source": "mim_exact", "local_identifier":
    "CHEBI:63036", "source_compound_id": null, "reason": "trusted MIM label-index
    answer"}}, {"field": "ingredients[11]", "label": "MgCl2・6H2O", "primary": {"id":
    "CHEBI:86345", "label": "magnesium dichloride hexahydrate"}, "secondary": null,
    "legacy": null, "decision": {"query_label": "MgCl2・6H2O", "identifier": "CHEBI:86345",
    "ontology_id": "CHEBI:86345", "mim_preferred_term": "MgCl2 x 6 H2O", "matched_label":
    "MgCl2・6H2O", "match_type": "synonym", "mapping_status": "MAPPED", "ambiguity":
    "unique", "resolution_source": "mim_exact", "local_identifier": "CHEBI:86345",
    "source_compound_id": null, "reason": "trusted MIM label-index answer"}}, {"field":
    "ingredients[12]", "label": "KCl", "primary": {"id": "CHEBI:32588", "label": "potassium
    chloride"}, "secondary": {"id": "CHEBI:32588", "label": "potassium chloride"},
    "legacy": null, "decision": {"query_label": "KCl", "identifier": "CHEBI:32588",
    "ontology_id": "CHEBI:32588", "mim_preferred_term": "KCl", "matched_label": "KCl",
    "match_type": "preferred_term", "mapping_status": "MAPPED", "ambiguity": "unique",
    "resolution_source": "mim_exact", "local_identifier": "CHEBI:32588", "source_compound_id":
    null, "reason": "trusted MIM label-index answer"}}, {"field": "ingredients[13]",
    "label": "NaHCO3", "primary": {"id": "CHEBI:32139", "label": "sodium hydrogencarbonate"},
    "secondary": {"id": "CHEBI:32139", "label": "sodium hydrogencarbonate"}, "legacy":
    null, "decision": {"query_label": "NaHCO3", "identifier": "CHEBI:32139", "ontology_id":
    "CHEBI:32139", "mim_preferred_term": "NaHCO3", "matched_label": "NaHCO3", "match_type":
    "preferred_term", "mapping_status": "MAPPED", "ambiguity": "unique", "resolution_source":
    "mim_exact", "local_identifier": "CHEBI:32139", "source_compound_id": null, "reason":
    "trusted MIM label-index answer"}}, {"field": "ingredients[14]", "label": "(NH4)2SO4",
    "primary": {"id": "CHEBI:62946", "label": "ammonium sulfate"}, "secondary": {"id":
    "CHEBI:62946", "label": "ammonium sulfate"}, "legacy": null, "decision": {"query_label":
    "(NH4)2SO4", "identifier": "CHEBI:62946", "ontology_id": "CHEBI:62946", "mim_preferred_term":
    "(NH4)2SO4", "matched_label": "(NH4)2SO4", "match_type": "preferred_term", "mapping_status":
    "MAPPED", "ambiguity": "unique", "resolution_source": "mim_exact", "local_identifier":
    "CHEBI:62946", "source_compound_id": null, "reason": "trusted MIM label-index
    answer"}}, {"field": "ingredients[15]", "label": "NaBr", "primary": {"id": "CHEBI:63004",
    "label": "sodium bromide"}, "secondary": {"id": "CHEBI:63004", "label": "sodium
    bromide"}, "legacy": null, "decision": {"query_label": "NaBr", "identifier": "CHEBI:63004",
    "ontology_id": "CHEBI:63004", "mim_preferred_term": "NaBr", "matched_label": "NaBr",
    "match_type": "preferred_term", "mapping_status": "MAPPED", "ambiguity": "unique",
    "resolution_source": "mim_exact", "local_identifier": "CHEBI:63004", "source_compound_id":
    null, "reason": "trusted MIM label-index answer"}}, {"field": "ingredients[16]",
    "label": "SrCl2・6H2O", "primary": {"id": "CHEBI:36385", "label": "strontium dichloride
    hexahydrate"}, "secondary": null, "legacy": null, "decision": {"query_label":
    "SrCl2・6H2O", "identifier": "CHEBI:36385", "ontology_id": "CHEBI:36385", "mim_preferred_term":
    "SrCl2 x 6 H2O", "matched_label": "SrCl2・6H2O", "match_type": "synonym", "mapping_status":
    "MAPPED", "ambiguity": "unique", "resolution_source": "mim_exact", "local_identifier":
    "CHEBI:36385", "source_compound_id": null, "reason": "trusted MIM label-index
    answer"}}, {"field": "ingredients[17]", "label": "Ammonium Fe(III) citrate", "primary":
    null, "secondary": null, "legacy": null, "decision": {"query_label": "Ammonium
    Fe(III) citrate", "identifier": null, "ontology_id": null, "mim_preferred_term":
    null, "matched_label": null, "match_type": null, "mapping_status": null, "ambiguity":
    null, "resolution_source": "not_found", "local_identifier": null, "source_compound_id":
    null, "reason": "label not found in pinned MIM index and no usable local identity"}}]

    Primary hydrate repairs are credited. MgSO4・7H2O and CaCl2・2H2O use local fallbacks
    because these exact written labels are not in the pinned index; fallback does
    not invalidate their separately verified CHEBI identities. Ammonium Fe(III) citrate
    remains unresolved. FOODON/MICRO resolver outputs for mixtures are observations,
    not externally verified new grounding proposals. PIPES authority object is sparse;
    no additional chemical-form precision is claimed.'
  metrics:
  - name: primary_coverage
    value: 77.77777777777777
    unit: percent
    denominator: 18
    minimum: 0
    maximum: 100
    definition: 14 of18 selected ingredient descriptors carry a primary ontology term;
      field coverage, not accuracy.
  - name: secondary_coverage
    value: 50.0
    unit: percent
    denominator: 18
    minimum: 0
    maximum: 100
    definition: 9 of18 selected descriptors carry a CHEBI-keyed secondary link; not
      accuracy.
  - name: secondary_resolver_agreement
    value: 100
    unit: percent
    denominator: 9
    minimum: 0
    maximum: 100
    definition: All9 existing secondary identifiers agree with the exact maintained
      resolver; not experimental or chemical-form proof.
- assessment_id: writer
  area: provenance
  topic: Current writer and historical evidence assessment
  outcome: concern
  summary: Current importer preview improves stock separation but still leaves name-resolution,
    denominator and pH extraction gaps.
  target_ids:
  - CultureMech:007626
  evidence_ids:
  - importer
  - generator
  - formulation
  - diagnostics
  - counterpart
  - solution5101-local
  - solution5101
  - historical-1
  - historical-2
  - historical-3
  - historical-4
  - historical-5
  - historical-6
  - historical-7
  details: Pure-method preview emits four main solutes plus unquantifiedN2 and two
    stock additions. Artificial seawater (see below) fails exact matching to Artificial
    seawater, yielding empty composition. Raw5 ml becomes5 ML_PER_L despite unproved
    final volume. _extract_ph reads a top-level field while current meta.ph=7.0, returning
    empty conditions. Preparation prose is now retained by current extractor, but
    old owner/target lack it. Current improvements are credited without treating regeneration
    alone as sufficient. All45 October historical source-object/literal joins match
    the fresh J1042 API; both existing solution5101 claims match fresh bytes and digest.
    These joins do not authenticate historical retrieval times. Earlier claims that
    API main rates are underconcentrated or that raw batch masses automatically mean
    per-litre values are not adopted. Sibling NaCl/MgSO4/CaCl2 sums mix separate solution
    bases; sibling identity alone is no authority to merge. No historical review is
    treated as structured coverage or silently closed.
findings:
- finding_id: F1
  issue_key: CM007626-quantity-dimension-basis
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Liquid batch inputs use mass units and other rate bases are unproved
  description: Two1 L liquid inputs and two5 ml stock doses are G_PER_L in both records.
    The four main masses also lack an explicit final-litre basis. Preserve exact batch
    amounts and distinguish database-reported normalized values from independent final-volume
    evidence.
  target_ids:
  - CultureMech:007626
  field_paths:
  - ingredients[0:5].concentration
  - ingredients[6].concentration
  - solutions[].concentration
  evidence_ids:
  - target
  - owner
  - togo1107-api
  - mediadiveJ1042
  - diagnostics
  rule_id: concentration-evidence-contract
  native_severity: P2
  normalization_reason: 'P2 normalized to major: material quantity, preparation or
    stock-stage defect.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml
    role: maintained normalized source
- finding_id: F2
  issue_key: CM007626-stock-topology
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Seawater and referenced stocks lose their preparation stages
  description: Eleven seawater solutes are direct main ingredients, the trace-mineral
    dose sits at medium level, and both referenced definitions are empty. Current
    importer separates primary items but cannot match the see-below suffix to the
    local stock section.
  target_ids:
  - CultureMech:007626
  field_paths:
  - ingredients[7:18]
  - solutions
  evidence_ids:
  - target
  - owner
  - togo1107-api
  - togo142-api
  - togo190-api
  - jcm151
  - jcm197
  - importer
  - diagnostics
  rule_id: source-stock-scope
  native_severity: P2
  normalization_reason: 'P2 normalized to major: material quantity, preparation or
    stock-stage defect.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml
    role: maintained normalized source
- finding_id: F3
  issue_key: CM007626-preparation-gas-ph
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Main preparation and pH are missing while nitrogen is a variable solute
  description: Recoverable main pH7.0, N2 distribution, butyl stoppers and autoclave
    instructions are absent. Preserve gas handling and separate stock pH steps. Current
    pH extractor misses meta.ph; review vitamin-specific dependency handling before
    transfer.
  target_ids:
  - CultureMech:007626
  field_paths:
  - preparation_steps
  - ph_value
  - ingredients[5]
  evidence_ids:
  - target
  - owner
  - togo1107-api
  - mediadiveJ1042
  - jcm151
  - jcm197
  - importer
  - diagnostics
  rule_id: source-preparation-scope
  native_severity: P2
  normalization_reason: 'P2 normalized to major: material quantity, preparation or
    stock-stage defect.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml
    role: maintained normalized source
- finding_id: F4
  issue_key: CM007626-claim-provenance
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Selected recipe lacks scoped claim evidence and primary source remains unavailable
  description: TOGO and MediaDive support bounded formula claims, and primary JCM
    pages support the two dependency definitions. The exact JCM1042 recipe is unavailable.
    Attach honest scoped provenance and retain prior history; do not label fallback
    data as directly inspected JCM1042.
  target_ids:
  - CultureMech:007626
  field_paths:
  - ingredients[].evidence
  - evidence
  - curation_history
  evidence_ids:
  - target
  - owner
  - togo1107-api
  - mediadiveJ1042
  - jcm1042
  - jcm1042-pdf
  - jcm151
  - jcm197
  rule_id: source-provenance-and-history
  native_severity: P3
  normalization_reason: 'P3 normalized to minor: recoverable source/provenance gap.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml
    role: maintained normalized source
actions:
- action_id: A1
  description: Curate explicit batch amounts and correct quantity dimensions; repair
    source-transform denominator handling.
  finding_ids:
  - F1
  target_ids:
  - CultureMech:007626
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml
    role: maintained normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/togo_importer.py
    role: maintained TOGO source transform
  acceptance_checks:
  - Account for all40 local quantity fields and45 scoped source rows.
  - Retain main vitamin5 ml, main seawater1 L, seawater water1 L and internal mineral5
    ml as distinct inputs.
  - Require explicit final-volume evidence before asserting per-litre rates; retain
    provider-reported API rates only with their declared solution basis.
  - Do not use density, additive liquid volumes or historical recommendations to invent
    final concentrations; run the four native recipe checks.
- action_id: A2
  description: Restore seawater and exact referenced mineral/vitamin definitions with
    distinct receiving stages.
  finding_ids:
  - F2
  target_ids:
  - CultureMech:007626
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml
    role: maintained normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/togo_importer.py
    role: maintained TOGO source transform
  acceptance_checks:
  - Account for11 seawater solutes,12 trace-mineral solutes and10 vitamins, plus their
    water and unquantified adjustment inputs.
  - Resolve see-below local section naming without merging unrelated sections; preserve
    exact hydrate/generic-form distinctions.
  - Do not import parent receiving doses, unrelated parent formulations or JCM197’s
    different mineral stock.
  - Use supported schema representation; if nested batch doses cannot be represented
    losslessly, document the exact schema gap rather than flatten.
- action_id: A3
  description: Restore main preparation and correctly extract source pH while separating
    gas and stock instructions.
  finding_ids:
  - F3
  target_ids:
  - CultureMech:007626
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml
    role: maintained normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/togo_importer.py
    role: maintained TOGO source transform
  acceptance_checks:
  - Retain pH7.0, N2 atmosphere, butyl rubber stoppers and autoclaving without invented
    time/temperature.
  - Keep mineral pH6.5 then7.0 stock-scoped; assess vitamin filtration applicability
    explicitly.
  - Keep N2 unquantified and preparation-scoped; do not invent solute concentration,
    pressure, incubation or growth.
  - Test current payload meta.ph path and local-section behavior after an authorized
    writer fix; run schema, strict, terms and references.
- action_id: A4
  description: Attach claim-level provenance, preserve append-only history and regenerate
    only from curated maintained inputs.
  finding_ids:
  - F4
  target_ids:
  - CultureMech:007626
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1107_Calroanaerobacter_Medium.yaml
    role: maintained normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merger.py
    role: generated merge implementation
  acceptance_checks:
  - Use ingredient evidence for supported ingredient claims and root evidence scoped
    to solution/preparation field paths.
  - Distinguish current fallback recipe sources, directly inspected dependency primary
    sources and unavailable exact JCM1042; preserve real capture times.
  - Retain June corrections and all earlier history without rewriting or guessing
    values; record new curation only under separate authorization.
  - Respect formulation compatibility before any sibling reconciliation; run just
    verify-merges and just audit-merge-freshness after authorized regeneration.
  depends_on:
  - A1
  - A2
  - A3
  generator: python -m culturemech.merge.merge_recipes
limitations:
- Exact JCM1042 CGI returns Nothing found and historical PDF candidate returns404.
  Current TOGO/MediaDive recipe evidence is explicitly secondary; JCM151/197 primary
  evidence is scoped to referenced stocks.
- No final mixed volume, density, molarity or stock contribution was inferred from
  input liquid volumes. Database g_l and mmol_l fields are retained as reported context,
  not blanket chemical or arithmetic endorsement.
- All14 asserted CHEBI identities were checked. New FOODON/MICRO resolver outputs
  for mixtures were not independently verified and are not new grounding proposals;
  ammonium ferric citrate remains unresolved.
- Canonical checks target only the selected generated record; owners/context files
  were read. Schema validity is not scientific accuracy. Full-corpus ID/product/merge
  gates and experiments were not rerun for this review-only addition.
- The source provides no strain-specific growth or incubation evidence. Source spelling
  alone is not an organism identification; vitamin dependency handling requires explicit
  applicability review.
notes:
- All scientific records remain unchanged; original native inspect source hashes and
  four check streams are retained.
- Seven historical reports were read with complete prose and source-row comparison;45
  historical API objects and2 existing solution claims authenticate against fresh
  bytes. Historical access times are not independently authenticated.
- No prior structured finding is closed. Primary-source access limits remain explicit
  despite successful deterministic checks.
tags:
- source-review
- generated-record
- togo
- stock-topology
- batch-058
```
