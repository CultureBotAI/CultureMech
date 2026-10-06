# Ingredient Concentration Review

- Record: data/merge_yaml/merged/r3_a_medium.yaml
- ID: CultureMech:003863
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 45099f44bb9ba12f3e7ee07e01136318dc620fc69642c0bab9896bc93d5567dd
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/10
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/1_10_r2a_medium.yaml
- data/normalized_yaml/bacterial/KOMODO_1153_R3_A_medium.yaml
- data/normalized_yaml/bacterial/KOMODO_1320_HALF_STRENGTH_R2A_MEDIUM_IN_75_SEAWATER.yaml
- data/normalized_yaml/bacterial/KOMODO_830_R2A_medium.yaml
- data/normalized_yaml/bacterial/KOMODO_919_LIMNOBACTER_medium.yaml
- data/normalized_yaml/bacterial/TOGO_M1646_R2A_Medium.yaml
- data/normalized_yaml/bacterial/TOGO_M2301_R2A_Medium.yaml
- data/normalized_yaml/bacterial/TOGO_M2520_R2A_Medium.yaml
- data/normalized_yaml/bacterial/TOGO_M2592_R2A_Medium.yaml
- data/normalized_yaml/bacterial/double_concentrated_830_0_06_sodium_pyruvate.yaml
- data/normalized_yaml/bacterial/half_strength_r2a.yaml
- data/normalized_yaml/bacterial/half_strength_r2a_medium_in_75_seawater.yaml
- data/normalized_yaml/bacterial/limnobacter_medium.yaml
- data/normalized_yaml/bacterial/r2a_medium.yaml
- data/normalized_yaml/bacterial/r3_a_medium.yaml
- data/normalized_yaml/bacterial/reactivation_with_liquid_medium_830.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Yeast extract | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Proteose peptone | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Casamino acids | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / Glucose | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / Starch | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[5].concentration / Na-pyruvate | {"value": "0.6", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[6].concentration / K2HPO4 | {"value": "0.6", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[7].concentration / MgSO4 x 7 H2O | {"value": "0.1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[8].concentration / Sodium pyruvate | {"value": "0.6", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[9].concentration / Agar | {"value": "15", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.


## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
