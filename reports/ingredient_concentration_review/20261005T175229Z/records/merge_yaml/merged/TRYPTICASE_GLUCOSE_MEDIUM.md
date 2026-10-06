# Ingredient Concentration Review

- Record: data/merge_yaml/merged/TRYPTICASE_GLUCOSE_MEDIUM.yaml
- ID: CultureMech:002540
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: ef64f1387d3e40cf6513aed9b8b53c2225a596c87b44e0f5c8e3e4ec48d5334d
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/9
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/TOGO_M10_Trypticase_Glucose_Medium.yaml
- data/normalized_yaml/bacterial/TOGO_M1614_Trypticase_Soy_Yeast_Extract_Medium.yaml
- data/normalized_yaml/bacterial/TOGO_M2191_Trypticase_Soy_Yeast_Extract_Medium.yaml
- data/normalized_yaml/bacterial/TOGO_M2330_Trypticase_Soy_Yeast_Extract_Medium.yaml
- data/normalized_yaml/bacterial/medium_92_modified_for_dsm_10249.yaml
- data/normalized_yaml/bacterial/medium_92_modified_for_dsm_10672.yaml
- data/normalized_yaml/bacterial/medium_92_modified_for_dsm_10673.yaml
- data/normalized_yaml/bacterial/medium_92_modified_for_dsm_11865.yaml
- data/normalized_yaml/bacterial/medium_92_modified_for_dsm_13240.yaml
- data/normalized_yaml/bacterial/medium_92_modified_for_dsm_14684.yaml
- data/normalized_yaml/bacterial/medium_92_modified_for_dsm_15461.yaml
- data/normalized_yaml/bacterial/medium_92_modified_for_dsm_17027.yaml
- data/normalized_yaml/bacterial/medium_92_modified_for_dsm_17065.yaml
- data/normalized_yaml/bacterial/medium_92_modified_for_dsm_17066.yaml
- data/normalized_yaml/bacterial/medium_92_modified_for_dsm_18607.yaml
- data/normalized_yaml/bacterial/medium_92_modified_for_dsm_18966.yaml
- data/normalized_yaml/bacterial/medium_92_modified_for_dsm_19663.yaml
- data/normalized_yaml/bacterial/medium_92_modified_for_dsm_21577.yaml
- data/normalized_yaml/bacterial/medium_92_modified_for_dsm_23765.yaml
- data/normalized_yaml/bacterial/medium_92_modified_for_dsm_23766.yaml
- data/normalized_yaml/bacterial/medium_92_modified_for_dsm_25585.yaml
- data/normalized_yaml/bacterial/medium_92_modified_for_dsm_43846.yaml
- data/normalized_yaml/bacterial/medium_92_modified_for_dsm_6685.yaml
- data/normalized_yaml/bacterial/medium_92_modified_for_dsm_6688.yaml
- data/normalized_yaml/bacterial/medium_92_modified_for_dsm_7109.yaml
- data/normalized_yaml/bacterial/medium_92_modified_for_dsm_7110.yaml
- data/normalized_yaml/bacterial/medium_92_modified_for_dsm_7111.yaml
- data/normalized_yaml/bacterial/medium_92_modified_for_dsm_7112.yaml
- data/normalized_yaml/bacterial/medium_92_modified_for_dsm_7113.yaml
- data/normalized_yaml/bacterial/medium_92_modified_for_dsm_7171.yaml
- data/normalized_yaml/bacterial/trypticase_glucose_medium.yaml
- data/normalized_yaml/bacterial/trypticase_soy_yeast_extract_medium.yaml
- data/normalized_yaml/fungal/trypticase_soy_yeast_extract_medium.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Pancreatic digest of casein | {"value": "17.0", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Peptic digest of soybean meal | {"value": "3.0", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Glucose | {"value": "2.5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / Sodium chloride | {"value": "5.0", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / Dipotassium phosphate | {"value": "2.5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[5].concentration / Agar | {"value": "15.0", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[6].concentration / Yeast extract | {"value": "3", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[7].concentration / Glucose | {"value": "5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[8].concentration / Agar | {"value": "15", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://en.wikipedia.org/wiki/Tryptic_soy_broth
- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=17

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
