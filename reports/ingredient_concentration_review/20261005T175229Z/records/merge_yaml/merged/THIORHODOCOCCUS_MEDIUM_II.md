# Ingredient Concentration Review

- Record: data/merge_yaml/merged/THIORHODOCOCCUS_MEDIUM_II.yaml
- ID: CultureMech:004750
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 3fd3987c10879a594eb179b3bf86fa6899dde624bc3b01e2cef82a7cb5fd7cb2
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/4
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/KOMODO_28b_THIORHODOCOCCUS_medium_II.yaml
- data/normalized_yaml/bacterial/medium_28_modified_for_dsm_12498.yaml
- data/normalized_yaml/bacterial/medium_28_modified_for_dsm_15006.yaml
- data/normalized_yaml/bacterial/medium_28_modified_for_dsm_15907.yaml
- data/normalized_yaml/bacterial/medium_28_modified_for_dsm_1591.yaml
- data/normalized_yaml/bacterial/medium_28_modified_for_dsm_1711.yaml
- data/normalized_yaml/bacterial/medium_28_modified_for_dsm_1712.yaml
- data/normalized_yaml/bacterial/medium_28_modified_for_dsm_1713.yaml
- data/normalized_yaml/bacterial/medium_28_modified_for_dsm_18858.yaml
- data/normalized_yaml/bacterial/medium_28_modified_for_dsm_203.yaml
- data/normalized_yaml/bacterial/medium_28_modified_for_dsm_204.yaml
- data/normalized_yaml/bacterial/medium_28_modified_for_dsm_212.yaml
- data/normalized_yaml/bacterial/medium_28_modified_for_dsm_213.yaml
- data/normalized_yaml/bacterial/medium_28_modified_for_dsm_214.yaml
- data/normalized_yaml/bacterial/medium_28_modified_for_dsm_237.yaml
- data/normalized_yaml/bacterial/medium_28_modified_for_dsm_238.yaml
- data/normalized_yaml/bacterial/medium_28_modified_for_dsm_239.yaml
- data/normalized_yaml/bacterial/medium_28_modified_for_dsm_240.yaml
- data/normalized_yaml/bacterial/medium_28_modified_for_dsm_243.yaml
- data/normalized_yaml/bacterial/medium_28_modified_for_dsm_4868.yaml
- data/normalized_yaml/bacterial/medium_28_modified_for_dsm_5261.yaml
- data/normalized_yaml/bacterial/medium_28_modified_for_dsm_5652.yaml
- data/normalized_yaml/bacterial/medium_28_modified_for_dsm_5653.yaml
- data/normalized_yaml/bacterial/medium_28_modified_for_dsm_6702.yaml
- data/normalized_yaml/bacterial/medium_28_modified_for_dsm_726.yaml
- data/normalized_yaml/bacterial/thiorhodococcus_medium_ii.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / NaCl | {"value": "15", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Na2S2O3 x 5 H2O | {"value": "0.5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / MgCl2 x 6 H2O | {"value": "2.5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / Na2S x 9 H2O | {"value": "30", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.


## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
