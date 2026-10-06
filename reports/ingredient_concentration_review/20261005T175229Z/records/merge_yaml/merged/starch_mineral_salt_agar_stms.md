# Ingredient Concentration Review

- Record: data/merge_yaml/merged/starch_mineral_salt_agar_stms.yaml
- ID: CultureMech:004654
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: c5675caa0e4b1fe3a1c007196f71682c7b28fa1833c4164eee6a0d10671ad202
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/10
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/KOMODO_1240_STARCH-MINERAL_SALT-AGAR_10_NACL.yaml
- data/normalized_yaml/bacterial/KOMODO_252_STARCH_-_MINERAL_salt_-_AGAR_STMS.yaml
- data/normalized_yaml/bacterial/KOMODO_547_ISP_medium_4.yaml
- data/normalized_yaml/bacterial/TOGO_M50_Inorganic_Salts-Starch_Agar_ISP-4.yaml
- data/normalized_yaml/bacterial/inorganic_salts_starch_agar_isp_4.yaml
- data/normalized_yaml/bacterial/isp_medium_4.yaml
- data/normalized_yaml/bacterial/medium_252_modified_for_dsm_41399.yaml
- data/normalized_yaml/bacterial/medium_252_modified_for_dsm_41400.yaml
- data/normalized_yaml/bacterial/medium_252_modified_for_dsm_41403.yaml
- data/normalized_yaml/bacterial/medium_252_modified_for_dsm_41404.yaml
- data/normalized_yaml/bacterial/medium_252_modified_for_dsm_41405.yaml
- data/normalized_yaml/bacterial/medium_252_modified_for_dsm_41406.yaml
- data/normalized_yaml/bacterial/medium_252_modified_for_dsm_41407.yaml
- data/normalized_yaml/bacterial/medium_252_modified_for_dsm_41408.yaml
- data/normalized_yaml/bacterial/medium_252_modified_for_dsm_41410.yaml
- data/normalized_yaml/bacterial/medium_252_modified_for_dsm_41411.yaml
- data/normalized_yaml/bacterial/medium_252_modified_for_dsm_41412.yaml
- data/normalized_yaml/bacterial/medium_252_modified_for_dsm_41413.yaml
- data/normalized_yaml/bacterial/medium_252_modified_for_dsm_41415.yaml
- data/normalized_yaml/bacterial/medium_252_modified_for_dsm_41416.yaml
- data/normalized_yaml/bacterial/medium_252_modified_for_dsm_41417.yaml
- data/normalized_yaml/bacterial/medium_252_modified_for_dsm_41418.yaml
- data/normalized_yaml/bacterial/medium_252_modified_for_dsm_41419.yaml
- data/normalized_yaml/bacterial/medium_252_modified_for_dsm_41420.yaml
- data/normalized_yaml/bacterial/medium_252_modified_for_dsm_41877.yaml
- data/normalized_yaml/bacterial/medium_252_modified_for_dsm_44410.yaml
- data/normalized_yaml/bacterial/medium_252_modified_for_dsm_44964.yaml
- data/normalized_yaml/bacterial/medium_252_modified_for_dsm_45004.yaml
- data/normalized_yaml/bacterial/medium_252_modified_for_dsm_45007.yaml
- data/normalized_yaml/bacterial/medium_252_modified_for_dsm_45009.yaml
- data/normalized_yaml/bacterial/medium_252_modified_for_dsm_45012.yaml
- data/normalized_yaml/bacterial/medium_252_modified_for_dsm_45015.yaml
- data/normalized_yaml/bacterial/medium_252_modified_for_dsm_45017.yaml
- data/normalized_yaml/bacterial/medium_252_modified_for_dsm_45088.yaml
- data/normalized_yaml/bacterial/medium_252_modified_for_dsm_45210.yaml
- data/normalized_yaml/bacterial/medium_252_modified_for_dsm_45211.yaml
- data/normalized_yaml/bacterial/medium_547_modified_for_dsm_44048.yaml
- data/normalized_yaml/bacterial/medium_547_modified_for_dsm_44681.yaml
- data/normalized_yaml/bacterial/medium_547_modified_for_dsm_44682.yaml
- data/normalized_yaml/bacterial/starch_mineral_salt_agar_10_nacl.yaml
- data/normalized_yaml/bacterial/starch_mineral_salt_agar_stms.yaml
- data/normalized_yaml/bacterial/starch_mineral_salt_agar_stms_15_nacl.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Starch | {"value": "10", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / (NH4)2SO4 | {"value": "2", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / K2HPO4 | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / MgSO4 x 7 H2O | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / NaCl | {"value": "101.0", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[5].concentration / CaCO3 | {"value": "2", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[6].concentration / Agar | {"value": "15", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[7].concentration / FeSO4 x 7 H2O | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence; PLAUSIBILITY_TRACE_SALT_AS_STOCK | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[8].concentration / MnCl2 x 4 H2O | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence; PLAUSIBILITY_TRACE_SALT_AS_STOCK | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[9].concentration / ZnSO4 x 7 H2O | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence; PLAUSIBILITY_TRACE_SALT_AS_STOCK | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.


## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
