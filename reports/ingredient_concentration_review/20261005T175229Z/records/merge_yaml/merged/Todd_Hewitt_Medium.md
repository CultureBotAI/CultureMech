# Ingredient Concentration Review

- Record: data/merge_yaml/merged/Todd_Hewitt_Medium.yaml
- ID: CultureMech:006321
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 6320ccb7413f689369e0b2ed4d8f14364c4731cdae27e32f8792eabe7468c23b
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/6
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/KOMODO_697_TODD-HEWITT_medium.yaml
- data/normalized_yaml/bacterial/TOGO_M1524_Todd_Hewitt_Medium.yaml
- data/normalized_yaml/bacterial/medium_697_modified_for_dsm_10695.yaml
- data/normalized_yaml/bacterial/medium_697_modified_for_dsm_11867.yaml
- data/normalized_yaml/bacterial/medium_697_modified_for_dsm_11868.yaml
- data/normalized_yaml/bacterial/medium_697_modified_for_dsm_20566.yaml
- data/normalized_yaml/bacterial/medium_697_modified_for_dsm_20617.yaml
- data/normalized_yaml/bacterial/medium_697_modified_for_dsm_24048.yaml
- data/normalized_yaml/bacterial/todd_hewitt_medium.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Meat infusion | {"value": "10", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Casein peptone | {"value": "20", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Dextrose | {"value": "2", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / NaHCO3 | {"value": "2", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / NaCl | {"value": "2", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[5].concentration / Na2HPO4 | {"value": "0.4", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.


## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
