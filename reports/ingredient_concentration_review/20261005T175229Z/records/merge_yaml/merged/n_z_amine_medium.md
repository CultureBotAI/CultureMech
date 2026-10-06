# Ingredient Concentration Review

- Record: data/merge_yaml/merged/n_z_amine_medium.yaml
- ID: CultureMech:006003
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 9dadb5a8f1ffaddb13c0dc13c1444b2aab63c9c977ac1a6abac6b630958dcd15
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/6
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/KOMODO_554_N-Z-AMINE-MEDIUM.yaml
- data/normalized_yaml/bacterial/TOGO_M2370_N-Z-Amine-Medium.yaml
- data/normalized_yaml/bacterial/TOGO_M437_N-Z_Amine_With_Soluble_Starch_And_Glucose.yaml
- data/normalized_yaml/bacterial/medium_554_modified_for_dsm_44396.yaml
- data/normalized_yaml/bacterial/n_z_amine_medium.yaml
- data/normalized_yaml/bacterial/n_z_amine_with_soluble_starch_and_glucose.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Glucose | {"value": "10", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Starch | {"value": "20", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Yeast extract | {"value": "5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / N-Z amine | {"value": "5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / CaCO3 | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[5].concentration / Agar | {"value": "20", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.


## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
