# Ingredient Concentration Review

- Record: data/merge_yaml/merged/vy_2_reduced_medium.yaml
- ID: CultureMech:006986
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 8c602647661c3f191fe0391881bfa05302da35c2eaa2cf55ddcee32e1b8bd837
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/4
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/JCM_J436_VY_2_AGAR.yaml
- data/normalized_yaml/bacterial/KOMODO_9_VY_2_AGAR.yaml
- data/normalized_yaml/bacterial/KOMODO_9a_VY_2_REDUCED_medium.yaml
- data/normalized_yaml/bacterial/TOGO_M1589_VY_2_Agar.yaml
- data/normalized_yaml/bacterial/medium_9_modified_for_dsm_14553.yaml
- data/normalized_yaml/bacterial/medium_9_modified_for_dsm_14608.yaml
- data/normalized_yaml/bacterial/medium_9_modified_for_dsm_14670.yaml
- data/normalized_yaml/bacterial/medium_9_modified_for_dsm_53191.yaml
- data/normalized_yaml/bacterial/medium_9_modified_for_dsm_53271.yaml
- data/normalized_yaml/bacterial/medium_9_modified_for_dsm_53343.yaml
- data/normalized_yaml/bacterial/medium_9_modified_for_dsm_53796.yaml
- data/normalized_yaml/bacterial/vy_2_agar.yaml
- data/normalized_yaml/bacterial/vy_2_reduced_medium.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Baker's yeast | {"value": "5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / CaCl2 x 2 H2O | {"value": "1.36", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Vitamin B12 | {"value": "0.0005", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / Agar | {"value": "15", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.


## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
