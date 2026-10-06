# Ingredient Concentration Review

- Record: data/merge_yaml/merged/WEISSELA_KOREENSIS_MEDIUM.yaml
- ID: CultureMech:004607
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 6f2d1377c15c47909a08dc1b08576762a9583d07861f80cb6c692971c48bc346
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/10
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/KOMODO_232_MRS_medium_WITH_CYSTEINE.yaml
- data/normalized_yaml/bacterial/KOMODO_232b_WEISSELA_KOREENSIS_medium.yaml
- data/normalized_yaml/bacterial/medium_232_modified_for_dsm_16982.yaml
- data/normalized_yaml/bacterial/medium_232_modified_for_dsm_17330.yaml
- data/normalized_yaml/bacterial/medium_232_modified_for_dsm_20079.yaml
- data/normalized_yaml/bacterial/medium_232_modified_for_dsm_20243.yaml
- data/normalized_yaml/bacterial/medium_232_modified_for_dsm_20289.yaml
- data/normalized_yaml/bacterial/medium_232_modified_for_dsm_20356.yaml
- data/normalized_yaml/bacterial/medium_232_modified_for_dsm_20403.yaml
- data/normalized_yaml/bacterial/medium_232_modified_for_dsm_20404.yaml
- data/normalized_yaml/bacterial/medium_232_modified_for_dsm_20405.yaml
- data/normalized_yaml/bacterial/medium_232_modified_for_dsm_20406.yaml
- data/normalized_yaml/bacterial/medium_232_modified_for_dsm_20653.yaml
- data/normalized_yaml/bacterial/medium_232_modified_for_dsm_20654.yaml
- data/normalized_yaml/bacterial/medium_232_modified_for_dsm_20655.yaml
- data/normalized_yaml/bacterial/medium_232_modified_for_dsm_20656.yaml
- data/normalized_yaml/bacterial/medium_232_modified_for_dsm_6306.yaml
- data/normalized_yaml/bacterial/mrs_medium_with_cysteine.yaml
- data/normalized_yaml/bacterial/weissela_koreensis_medium.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Casein peptone | {"value": "10", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Meat extract | {"value": "10", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Yeast extract | {"value": "5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / Glucose | {"value": "20", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / Tween 80 | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[5].concentration / K2HPO4 | {"value": "2", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[6].concentration / Na-acetate | {"value": "5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[7].concentration / (NH4)2 citrate | {"value": "2", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[8].concentration / MgSO4 x 7 H2O | {"value": "0.2", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[9].concentration / MnSO4 x H2O | {"value": "0.05", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.


## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
