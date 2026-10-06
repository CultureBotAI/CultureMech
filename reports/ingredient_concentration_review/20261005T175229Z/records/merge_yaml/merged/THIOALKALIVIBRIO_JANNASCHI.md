# Ingredient Concentration Review

- Record: data/merge_yaml/merged/THIOALKALIVIBRIO_JANNASCHI.yaml
- ID: CultureMech:004026
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 3d226b99f77bc1018a34165fa6545725470c4bb117a478df8512c2a4709c8a37
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/14
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/KOMODO_1272_THIOALKALIVIBRIO_JANNASCHI.yaml
- data/normalized_yaml/bacterial/KOMODO_925_ALKALIPHILIC_SULPHUR_RESPIRING_STRAINS_MEDIUM.yaml
- data/normalized_yaml/bacterial/TOGO_M2459_Alkaliphilic_Sulphur_Respiring_Strains_Medium.yaml
- data/normalized_yaml/bacterial/alkaliphilic_sulphur_respiring_strains_medium.yaml
- data/normalized_yaml/bacterial/dsm_13531_arh1_and_dsm_13532_arh2_kscn_grown.yaml
- data/normalized_yaml/bacterial/dsm_13533_alrh.yaml
- data/normalized_yaml/bacterial/dsm_13541_arh2_thiosulphate_grown.yaml
- data/normalized_yaml/bacterial/dsm_13542_arh1_thiosulphate_grown.yaml
- data/normalized_yaml/bacterial/thioalkalimicrobium_aerophilum_al_3_dsm_13739_and_tm_sibericum_al_7_dsm_13740.yaml
- data/normalized_yaml/bacterial/thioalkalispira_microaerophila_alen_1_dsm_14786.yaml
- data/normalized_yaml/bacterial/thioalkalivibrio_jannaschi.yaml
- data/normalized_yaml/bacterial/thioalkalivibrio_nitratireducens_alen_2_dsm_14787.yaml
- data/normalized_yaml/bacterial/thioalkalivibrio_versutus_al_2_dsm_13738_tv_nitratus_alj_12_dsm_13741_and_tv_denitrificans_aljd_dsm_13742.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Na2CO3 | {"value": "0.5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / NaHCO3 | {"value": "15", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / NaCl | {"value": "15", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / K2HPO4 | {"value": "0.5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / MgCl2 x 6 H2O | {"value": "0.2", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[5].concentration / EDTA | {"value": "0.005", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[6].concentration / FeSO4 x 7 H2O | {"value": "0.002", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[7].concentration / ZnSO4 x 7 H2O | {"value": "0.1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[8].concentration / MnCl2 x 4 H2O | {"value": "0.03", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[9].concentration / CoCl2 x 6 H2O | {"value": "0.2", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[10].concentration / NiCl2 x 6 H2O | {"value": "0.02", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[11].concentration / Na2MoO4 x 2 H2O | {"value": "0.03", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[12].concentration / CuCl2 x 2 H2O | {"value": "0.01", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[13].concentration / H3BO3 | {"value": "0.3", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.


## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
