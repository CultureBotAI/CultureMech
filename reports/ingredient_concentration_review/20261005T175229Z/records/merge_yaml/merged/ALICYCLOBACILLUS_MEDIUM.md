# Ingredient Concentration Review

- Record: data/merge_yaml/merged/ALICYCLOBACILLUS_MEDIUM.yaml
- ID: CultureMech:005217
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 508a36becff12197d3c40e7b6a2395d8f4eb85c0444807f941383d34f67e2b17
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/14
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/KOMODO_402_ALICYCLOBACILLUS_medium.yaml
- data/normalized_yaml/bacterial/TOGO_M2390_Alicyclobacillus_Medium.yaml
- data/normalized_yaml/bacterial/TOGO_M2391_Alicyclobacillus_Medium.yaml
- data/normalized_yaml/bacterial/alicyclobacillus_medium.yaml
- data/normalized_yaml/bacterial/for_strains_of_a_cycloheptanicus.yaml
- data/normalized_yaml/bacterial/medium_402_modified_for_dsm_11983.yaml
- data/normalized_yaml/bacterial/medium_402_modified_for_dsm_14558.yaml
- data/normalized_yaml/bacterial/medium_402_modified_for_dsm_14745.yaml
- data/normalized_yaml/bacterial/medium_402_modified_for_dsm_14955.yaml
- data/normalized_yaml/bacterial/medium_402_modified_for_dsm_16176.yaml
- data/normalized_yaml/bacterial/medium_402_modified_for_dsm_17614.yaml
- data/normalized_yaml/bacterial/medium_402_modified_for_dsm_18237.yaml
- data/normalized_yaml/bacterial/medium_402_modified_for_dsm_2498.yaml
- data/normalized_yaml/bacterial/medium_402_modified_for_dsm_3922.yaml
- data/normalized_yaml/bacterial/medium_402_modified_for_dsm_3923.yaml
- data/normalized_yaml/bacterial/medium_402_modified_for_dsm_3924.yaml
- data/normalized_yaml/bacterial/medium_402_modified_for_dsm_446.yaml
- data/normalized_yaml/bacterial/medium_402_modified_for_dsm_448.yaml
- data/normalized_yaml/bacterial/medium_402_modified_for_dsm_449.yaml
- data/normalized_yaml/bacterial/medium_402_modified_for_dsm_451.yaml
- data/normalized_yaml/bacterial/medium_402_modified_for_dsm_452.yaml
- data/normalized_yaml/bacterial/medium_402_modified_for_dsm_453.yaml
- data/normalized_yaml/bacterial/medium_402_modified_for_dsm_454.yaml
- data/normalized_yaml/bacterial/medium_402_modified_for_dsm_455.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / CaCl2 x 2 H2O | {"value": "0.25", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / MgSO4 x 7 H2O | {"value": "0.5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / (NH4)2SO4 | {"value": "0.2", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / Yeast extract | {"value": "2", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / Glucose | {"value": "5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[5].concentration / KH2PO4 | {"value": "3", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[6].concentration / Agar | {"value": "30", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[7].concentration / ZnSO4 x 7 H2O | {"value": "0.1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[8].concentration / MnCl2 x 4 H2O | {"value": "0.03", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[9].concentration / H3BO3 | {"value": "0.3", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[10].concentration / CoCl2 x 6 H2O | {"value": "0.2", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[11].concentration / CuCl2 x 2 H2O | {"value": "0.01", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[12].concentration / NiCl2 x 6 H2O | {"value": "0.02", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[13].concentration / Na2MoO4 x 2 H2O | {"value": "0.03", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.


## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
