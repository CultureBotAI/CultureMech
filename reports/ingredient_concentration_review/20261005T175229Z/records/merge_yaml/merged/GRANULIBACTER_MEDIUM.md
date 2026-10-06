# Ingredient Concentration Review

- Record: data/merge_yaml/merged/GRANULIBACTER_MEDIUM.yaml
- ID: CultureMech:003906
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 6a580b3b8f63a1b0070b4da46f379eee1236467fd0887c5033a5e3391fa72fa1
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/4
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/KOMODO_105_GLUCONOBACTER_OXYDANS_medium.yaml
- data/normalized_yaml/bacterial/KOMODO_1186_GRANULIBACTER_medium.yaml
- data/normalized_yaml/bacterial/TOGO_M89_Acetobacter_Medium.yaml
- data/normalized_yaml/bacterial/acetobacter_medium.yaml
- data/normalized_yaml/bacterial/clostridium_sp_medium.yaml
- data/normalized_yaml/bacterial/gluconobacter_oxydans_medium.yaml
- data/normalized_yaml/bacterial/glucose_yeast_extract_medium.yaml
- data/normalized_yaml/bacterial/granulibacter_medium.yaml
- data/normalized_yaml/bacterial/medium_105_modified_for_dsm_15972.yaml
- data/normalized_yaml/fungal/glucose_yeast_extract_medium.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Glucose | {"value": "100", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Yeast extract | {"value": "10", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / CaCO3 | {"value": "20", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / Agar | {"value": "15", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.


## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
