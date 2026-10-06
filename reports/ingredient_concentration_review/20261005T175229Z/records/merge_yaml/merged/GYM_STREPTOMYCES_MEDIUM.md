# Ingredient Concentration Review

- Record: data/merge_yaml/merged/GYM_STREPTOMYCES_MEDIUM.yaml
- ID: CultureMech:006237
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: ec0d900ff41d0769badbcea6967a07ce41e3c25886975a6c9a3f75747e23674e
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/5
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/KOMODO_65_GYM_STREPTOMYCES_medium.yaml
- data/normalized_yaml/bacterial/TOGO_M2331_GYM_Streptomyces_Medium.yaml
- data/normalized_yaml/bacterial/gym_streptomyces_medium.yaml
- data/normalized_yaml/bacterial/medium_65_modified_for_dsm_10552.yaml
- data/normalized_yaml/bacterial/medium_65_modified_for_dsm_40947.yaml
- data/normalized_yaml/bacterial/medium_65_modified_for_dsm_41697.yaml
- data/normalized_yaml/bacterial/medium_65_modified_for_dsm_41835.yaml
- data/normalized_yaml/bacterial/medium_65_modified_for_dsm_41868.yaml
- data/normalized_yaml/bacterial/medium_65_modified_for_dsm_43160.yaml
- data/normalized_yaml/bacterial/medium_65_modified_for_dsm_44099.yaml
- data/normalized_yaml/bacterial/medium_65_modified_for_dsm_44107.yaml
- data/normalized_yaml/bacterial/medium_65_modified_for_dsm_44117.yaml
- data/normalized_yaml/bacterial/medium_65_modified_for_dsm_44118.yaml
- data/normalized_yaml/bacterial/medium_65_modified_for_dsm_44119.yaml
- data/normalized_yaml/bacterial/medium_65_modified_for_dsm_44396.yaml
- data/normalized_yaml/bacterial/medium_65_modified_for_dsm_44588.yaml
- data/normalized_yaml/bacterial/medium_65_modified_for_dsm_44589.yaml
- data/normalized_yaml/bacterial/medium_65_modified_for_dsm_44590.yaml
- data/normalized_yaml/bacterial/medium_65_modified_for_dsm_44593.yaml
- data/normalized_yaml/bacterial/medium_65_modified_for_dsm_44617.yaml
- data/normalized_yaml/bacterial/medium_65_modified_for_dsm_44618.yaml
- data/normalized_yaml/bacterial/medium_65_modified_for_dsm_44619.yaml
- data/normalized_yaml/bacterial/medium_65_modified_for_dsm_44640.yaml
- data/normalized_yaml/bacterial/medium_65_modified_for_dsm_44686.yaml
- data/normalized_yaml/bacterial/medium_65_modified_for_dsm_44839.yaml
- data/normalized_yaml/bacterial/medium_65_modified_for_dsm_44840.yaml
- data/normalized_yaml/bacterial/medium_65_modified_for_dsm_44844.yaml
- data/normalized_yaml/bacterial/medium_65_modified_for_dsm_44845.yaml
- data/normalized_yaml/bacterial/medium_65_modified_for_dsm_44928.yaml
- data/normalized_yaml/bacterial/medium_65_modified_for_dsm_44963.yaml
- data/normalized_yaml/bacterial/medium_65_modified_for_dsm_45662.yaml
- data/normalized_yaml/bacterial/medium_65_modified_for_dsm_7487.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Glucose | {"value": "4", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Yeast extract | {"value": "4", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Malt extract | {"value": "10", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / CaCO3 | {"value": "2", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / Agar | {"value": "20", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.


## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
