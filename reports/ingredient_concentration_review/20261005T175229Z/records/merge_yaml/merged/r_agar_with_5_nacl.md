# Ingredient Concentration Review

- Record: data/merge_yaml/merged/r_agar_with_5_nacl.yaml
- ID: CultureMech:003111
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 9bad0c9cda1fdc9762c7e7fe1a8582b7d20c5a0dcb36dfc3b72cb0b5e5631e6d
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/2
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/TOGO_M105_R_Agar_With_3_NaCl.yaml
- data/normalized_yaml/bacterial/TOGO_M1235_R2A_Agar_With_2_NaCl.yaml
- data/normalized_yaml/bacterial/TOGO_M1238_Inorganic_Salts-Starch_Agar_ISP-4_With_5_NaCl.yaml
- data/normalized_yaml/bacterial/TOGO_M1376_R2A_Agar_With_3_NaCl.yaml
- data/normalized_yaml/bacterial/TOGO_M346_Inorganic_Salts-Starch_Agar_ISP-4_With_10_NaCl.yaml
- data/normalized_yaml/bacterial/TOGO_M408_Glycerol-Asparagine_Agar_ISP-5_With_10_NaCl.yaml
- data/normalized_yaml/bacterial/TOGO_M67_R_Agar_With_5_NaCl.yaml
- data/normalized_yaml/bacterial/TOGO_M900_Inorganic_Salts-Starch_Agar_ISP-4_With_15_NaCl.yaml
- data/normalized_yaml/bacterial/TOGO_M916_R_Agar_With_10_NaCl.yaml
- data/normalized_yaml/bacterial/TOGO_M957_R2A_Agar_With_1_NaCl.yaml
- data/normalized_yaml/bacterial/brewer_anaerobic_agar_with_2_nacl.yaml
- data/normalized_yaml/bacterial/glycerol_asparagine_agar_isp_5_with_10_nacl.yaml
- data/normalized_yaml/bacterial/inorganic_salts_starch_agar_isp_4_with_10_nacl.yaml
- data/normalized_yaml/bacterial/inorganic_salts_starch_agar_isp_4_with_15_nacl.yaml
- data/normalized_yaml/bacterial/inorganic_salts_starch_agar_isp_4_with_5_nacl.yaml
- data/normalized_yaml/bacterial/marine_agar_2216_with_10_nacl.yaml
- data/normalized_yaml/bacterial/marine_agar_2216_with_1_nacl.yaml
- data/normalized_yaml/bacterial/marine_agar_2216_with_3_1_nacl.yaml
- data/normalized_yaml/bacterial/marine_agar_2216_with_5_nacl.yaml
- data/normalized_yaml/bacterial/marine_agar_2216_with_8_0_nacl.yaml
- data/normalized_yaml/bacterial/marine_agar_2216_with_8_nacl.yaml
- data/normalized_yaml/bacterial/r2a_agar_with_1_nacl.yaml
- data/normalized_yaml/bacterial/r2a_agar_with_2_nacl.yaml
- data/normalized_yaml/bacterial/r2a_agar_with_3_nacl.yaml
- data/normalized_yaml/bacterial/r_agar_with_10_nacl.yaml
- data/normalized_yaml/bacterial/r_agar_with_3_nacl.yaml
- data/normalized_yaml/bacterial/r_agar_with_5_nacl.yaml
- data/normalized_yaml/specialized/brewer_anaerobic_agar_with_2_nacl.yaml
- data/normalized_yaml/specialized/marine_agar_2216_with_10_nacl.yaml
- data/normalized_yaml/specialized/marine_agar_2216_with_1_nacl.yaml
- data/normalized_yaml/specialized/marine_agar_2216_with_3_1_nacl.yaml
- data/normalized_yaml/specialized/marine_agar_2216_with_5_nacl.yaml
- data/normalized_yaml/specialized/marine_agar_2216_with_8_0_nacl.yaml
- data/normalized_yaml/specialized/marine_agar_2216_with_8_nacl.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Glycerol-asparagine agar | {"value": "1000", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / NaCl | {"value": "100", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=76

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
