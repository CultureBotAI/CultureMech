# Ingredient Concentration Review

- Record: data/merge_yaml/merged/reactivation_with_liquid_medium_464.yaml
- ID: CultureMech:005520
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 834a804b32dff08485289db212a6522ed44b3f68c77e265f5efd2c4a17cdebf0
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/4
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/KOMODO_464_PLATE_COUNT_AGAR.yaml
- data/normalized_yaml/bacterial/KOMODO_464a_REACTIVATION_WITH_LIQUID_medium_464.yaml
- data/normalized_yaml/bacterial/medium_464_modified_for_dsm_11199.yaml
- data/normalized_yaml/bacterial/medium_464_modified_for_dsm_15726.yaml
- data/normalized_yaml/bacterial/medium_464_modified_for_dsm_15727.yaml
- data/normalized_yaml/bacterial/medium_464_modified_for_dsm_15891.yaml
- data/normalized_yaml/bacterial/medium_464_modified_for_dsm_17107.yaml
- data/normalized_yaml/bacterial/medium_464_modified_for_dsm_1986.yaml
- data/normalized_yaml/bacterial/medium_464_modified_for_dsm_2114.yaml
- data/normalized_yaml/bacterial/medium_464_modified_for_dsm_2117.yaml
- data/normalized_yaml/bacterial/medium_464_modified_for_dsm_22870.yaml
- data/normalized_yaml/bacterial/medium_464_modified_for_dsm_6824.yaml
- data/normalized_yaml/bacterial/plate_count_agar.yaml
- data/normalized_yaml/bacterial/reactivation_with_liquid_medium_464.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Tryptone | {"value": "5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Yeast extract | {"value": "2.5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Dextrose | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / Agar | {"value": "15", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.


## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
