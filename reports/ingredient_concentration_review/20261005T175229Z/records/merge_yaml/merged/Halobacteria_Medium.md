# Ingredient Concentration Review

- Record: data/merge_yaml/merged/Halobacteria_Medium.yaml
- ID: CultureMech:005104
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: b15fe1f1c16f24b12cae4430538bff2c1fe9de5096d0a180b670196c4e0b44cc
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/10
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/archaea/JCM_J168_HALOBACTERIA_MEDIUM.yaml
- data/normalized_yaml/archaea/KOMODO_372_HALOBACTERIA_medium.yaml
- data/normalized_yaml/archaea/TOGO_M159_Halobacteria_Medium.yaml
- data/normalized_yaml/archaea/TOGO_M160_Halobacteria_Medium.yaml
- data/normalized_yaml/archaea/TOGO_M2369_Halobacteria_Medium.yaml
- data/normalized_yaml/archaea/halobacteria_medium.yaml
- data/normalized_yaml/bacterial/jcm_medium_no_1241.yaml
- data/normalized_yaml/bacterial/medium_372_modified_for_dsm_18341.yaml
- data/normalized_yaml/bacterial/medium_372_modified_for_dsm_18342.yaml
- data/normalized_yaml/bacterial/medium_372_modified_for_dsm_19336.yaml
- data/normalized_yaml/bacterial/medium_372_modified_for_dsm_21622.yaml
- data/normalized_yaml/bacterial/medium_372_modified_for_dsm_21769.yaml
- data/normalized_yaml/bacterial/medium_372_modified_for_dsm_21771.yaml
- data/normalized_yaml/bacterial/medium_372_modified_for_dsm_23158.yaml
- data/normalized_yaml/bacterial/medium_372_modified_for_dsm_23862.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Yeast extract | {"value": "5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Casamino acids | {"value": "5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Na glutamate | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / KCl | {"value": "2", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / Na3-citrate | {"value": "3", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[5].concentration / MgSO4 x 7 H2O | {"value": "20", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[6].concentration / NaCl | {"value": "200", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[7].concentration / FeCl2 x 4 H2O | {"value": "0.036", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[8].concentration / MnCl2 x 4 H2O | {"value": "0.00036", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[9].concentration / Agar | {"value": "20", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.


## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
