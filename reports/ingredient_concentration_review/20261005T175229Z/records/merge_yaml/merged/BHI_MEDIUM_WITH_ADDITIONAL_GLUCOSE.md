# Ingredient Concentration Review

- Record: data/merge_yaml/merged/BHI_MEDIUM_WITH_ADDITIONAL_GLUCOSE.yaml
- ID: CultureMech:001316
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: e3badb569cae61d156d4d91483ec679176b09a77662d9dc9e02902be6df0fe77
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/7
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/KOMODO_215_BHI_medium.yaml
- data/normalized_yaml/bacterial/KOMODO_215b_BHI_medium_WITH_ADDITIONAL_GLUCOSE.yaml
- data/normalized_yaml/bacterial/TOGO_M2360_BHI_Medium.yaml
- data/normalized_yaml/bacterial/TOGO_M284_Modified_BHI.yaml
- data/normalized_yaml/bacterial/TOGO_M63_Brain_Heart_Infusion_With_5_NaCl.yaml
- data/normalized_yaml/bacterial/bhi_agar.yaml
- data/normalized_yaml/bacterial/bhi_broth.yaml
- data/normalized_yaml/bacterial/bhi_medium.yaml
- data/normalized_yaml/bacterial/bhi_medium_with_additional_glucose.yaml
- data/normalized_yaml/bacterial/brain_heart_agar_bhi_luqiao_beijing.yaml
- data/normalized_yaml/bacterial/brain_heart_infusion_bhi_broth.yaml
- data/normalized_yaml/bacterial/brain_heart_infusion_bhi_difco_agar.yaml
- data/normalized_yaml/bacterial/brain_heart_infusion_broth_bhi_oxoid.yaml
- data/normalized_yaml/bacterial/brain_heart_infusion_broth_himedia.yaml
- data/normalized_yaml/bacterial/brain_heart_infusion_media.yaml
- data/normalized_yaml/bacterial/brain_heart_infusion_with_5_nacl.yaml
- data/normalized_yaml/bacterial/for_dsm_10643.yaml
- data/normalized_yaml/bacterial/for_dsm_19851.yaml
- data/normalized_yaml/bacterial/medium_215_modified_for_dsm_10548.yaml
- data/normalized_yaml/bacterial/medium_215_modified_for_dsm_10599.yaml
- data/normalized_yaml/bacterial/medium_215_modified_for_dsm_13140.yaml
- data/normalized_yaml/bacterial/medium_215_modified_for_dsm_13191.yaml
- data/normalized_yaml/bacterial/medium_215_modified_for_dsm_13666.yaml
- data/normalized_yaml/bacterial/medium_215_modified_for_dsm_13667.yaml
- data/normalized_yaml/bacterial/medium_215_modified_for_dsm_21511.yaml
- data/normalized_yaml/bacterial/medium_215_modified_for_dsm_22834.yaml
- data/normalized_yaml/bacterial/medium_215_modified_for_dsm_23150.yaml
- data/normalized_yaml/bacterial/medium_215_modified_for_dsm_25050.yaml
- data/normalized_yaml/bacterial/medium_215_modified_for_dsm_8629.yaml
- data/normalized_yaml/bacterial/medium_215b_modified_for_dsm_41834.yaml
- data/normalized_yaml/bacterial/modified_bhi.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Calf brains | {"value": "variable", "unit": "VARIABLE"} | missing_attached_evidence; VARIABLE_REQUIRES_SOURCE | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Beef heart | {"value": "variable", "unit": "VARIABLE"} | missing_attached_evidence; VARIABLE_REQUIRES_SOURCE | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Proteose peptone | {"value": "10.0", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / Dextrose | {"value": "2.0", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / Sodium chloride | {"value": "5.0", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[5].concentration / Disodium phosphate | {"value": "2.5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[6].concentration / Glucose | {"value": "5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://microbenotes.com/brain-heart-infusion-bhi-agar/
- https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium215b.pdf

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
