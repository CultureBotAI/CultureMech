# Ingredient Concentration Review

- Record: data/merge_yaml/merged/BRAIN_HEART_INFUSION_AGAR_WITH_SOIL_EXTRACT.yaml
- ID: CultureMech:009715
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: ff3be9dc3c68509bbcf6c71a88a575f25508851c1db39933f0c11c098bf268c7
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/9
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml
- data/normalized_yaml/bacterial/TOGO_M21_Brain_Heart_Infusion_Agar.yaml
- data/normalized_yaml/bacterial/TOGO_M2425_Brain_Heart_Infusion_Agar.yaml
- data/normalized_yaml/bacterial/TOGO_M255_Brain_Heart_Infusion_Agar_With_2_NaCl.yaml
- data/normalized_yaml/bacterial/TOGO_M2971_Brain_Heart_Infusion_Agar.yaml
- data/normalized_yaml/bacterial/TOGO_M337_Brain_Heart_Infusion_Agar_With_Soil_Extract.yaml
- data/normalized_yaml/bacterial/bhi_glucose_medium.yaml
- data/normalized_yaml/bacterial/brain_heart_infusion_agar.yaml
- data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_2_nacl.yaml
- data/normalized_yaml/bacterial/brain_heart_infusion_agar_with_soil_extract.yaml

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
| ingredients[7].concentration / Agar | {"value": "12", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[0].concentration / Soil extract (see Medium [M94]) | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://microbenotes.com/brain-heart-infusion-bhi-agar/
- https://togomedium.org/medium/M337
- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=342

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
