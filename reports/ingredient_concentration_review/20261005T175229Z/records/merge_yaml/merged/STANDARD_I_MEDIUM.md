# Ingredient Concentration Review

- Record: data/merge_yaml/merged/STANDARD_I_MEDIUM.yaml
- ID: CultureMech:005303
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 5b5d35510cd7568d83e7314dbf8592c02c88f54cd8293db44eacca086edc00b8
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/5
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/KOMODO_453_STANDARD_I_medium.yaml
- data/normalized_yaml/bacterial/medium_453_modified_for_dsm_43934.yaml
- data/normalized_yaml/bacterial/medium_453_modified_for_dsm_6341.yaml
- data/normalized_yaml/bacterial/medium_453_modified_for_dsm_6349.yaml
- data/normalized_yaml/bacterial/medium_453_modified_for_dsm_6364.yaml
- data/normalized_yaml/bacterial/medium_453_modified_for_dsm_6366.yaml
- data/normalized_yaml/bacterial/medium_453_modified_for_dsm_6406.yaml
- data/normalized_yaml/bacterial/medium_453_modified_for_dsm_6453.yaml
- data/normalized_yaml/bacterial/medium_453_modified_for_dsm_6454.yaml
- data/normalized_yaml/bacterial/medium_453_modified_for_dsm_6455.yaml
- data/normalized_yaml/bacterial/medium_453_modified_for_dsm_6458.yaml
- data/normalized_yaml/bacterial/medium_453_modified_for_dsm_6472.yaml
- data/normalized_yaml/bacterial/standard_i_medium.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Meat peptone | {"value": "7.8", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Casein peptone | {"value": "7.8", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Yeast extract | {"value": "2.8", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / NaCl | {"value": "5.6", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / D(+)-Glucose | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.


## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
