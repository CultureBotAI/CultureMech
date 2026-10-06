# Ingredient Concentration Review

- Record: data/merge_yaml/merged/tryptone_soya_broth_anaerob.yaml
- ID: CultureMech:001679
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: eee37fd2d5a4a06d4280d007970f5c9dce7f670134356b6a49ca119c8b754555
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/8
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/for_dsm_22112.yaml
- data/normalized_yaml/bacterial/medium_545_modified_for_dsm_13887.yaml
- data/normalized_yaml/bacterial/medium_545_modified_for_dsm_14656.yaml
- data/normalized_yaml/bacterial/medium_545_modified_for_dsm_15825.yaml
- data/normalized_yaml/bacterial/medium_545_modified_for_dsm_17447.yaml
- data/normalized_yaml/bacterial/medium_545_modified_for_dsm_17566.yaml
- data/normalized_yaml/bacterial/medium_545_modified_for_dsm_21372.yaml
- data/normalized_yaml/bacterial/medium_545_modified_for_dsm_21886.yaml
- data/normalized_yaml/bacterial/medium_545_modified_for_dsm_23581.yaml
- data/normalized_yaml/bacterial/medium_545_modified_for_dsm_6385.yaml
- data/normalized_yaml/bacterial/medium_545a_modified_for_dsm_17448.yaml
- data/normalized_yaml/bacterial/tryptone_soya_broth_anaerob.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Casein peptone | {"value": "17", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Soy peptone | {"value": "3", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / D(+)-Glucose | {"value": "2.5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / NaCl | {"value": "5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / K2HPO4 | {"value": "2.5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[5].concentration / Sodium resazurin | {"value": "0.0005", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[6].concentration / L-Cysteine HCl x H2O | {"value": "0.3", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[7].concentration / Na-thioglycolate | {"value": "0.3", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.


## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
