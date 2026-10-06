# Ingredient Concentration Review

- Record: data/merge_yaml/merged/yps_medium__18c2c656.yaml
- ID: CultureMech:003886
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 0767de2a1103a7fc69ff5a57bdf2d04a8b4674815f2ae477bc9d2f68a6cc90eb
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/4
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/DSMZ_990_YPS_MEDIUM.yaml
- data/normalized_yaml/bacterial/KOMODO_1168_YPS_medium.yaml
- data/normalized_yaml/bacterial/KOMODO_990_YPS_medium.yaml
- data/normalized_yaml/bacterial/TOGO_M2567_YPS_medium.yaml
- data/normalized_yaml/bacterial/TOGO_M2780_YPS_medium.yaml
- data/normalized_yaml/bacterial/medium_381_modified_for_dsm_12449.yaml
- data/normalized_yaml/bacterial/medium_381_modified_for_dsm_15370.yaml
- data/normalized_yaml/bacterial/medium_381_modified_for_dsm_17298.yaml
- data/normalized_yaml/bacterial/medium_381_modified_for_dsm_18339.yaml
- data/normalized_yaml/bacterial/medium_381_modified_for_dsm_22074.yaml
- data/normalized_yaml/bacterial/medium_381_modified_for_dsm_2304.yaml
- data/normalized_yaml/bacterial/medium_381_modified_for_dsm_23293.yaml
- data/normalized_yaml/bacterial/medium_381_modified_for_dsm_6188.yaml
- data/normalized_yaml/bacterial/medium_381_modified_for_dsm_6256.yaml
- data/normalized_yaml/bacterial/medium_381_modified_for_dsm_7123.yaml
- data/normalized_yaml/bacterial/medium_381_modified_for_dsm_7144.yaml
- data/normalized_yaml/bacterial/modified_lb.yaml
- data/normalized_yaml/bacterial/yps_medium.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Yeast extract | {"value": "4", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Peptone | {"value": "2", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Sea Salt | {"value": "25", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / Agar | {"value": "15", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.


## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
