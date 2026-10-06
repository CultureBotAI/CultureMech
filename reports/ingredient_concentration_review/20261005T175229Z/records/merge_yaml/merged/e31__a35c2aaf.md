# Ingredient Concentration Review

- Record: data/merge_yaml/merged/e31__a35c2aaf.yaml
- ID: CultureMech:000340
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: c66a75405cd613e67a61496a69c3408dc463457bcf35b2e3266c8679d08cf9c5
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/8
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/algae/e26_biotin.yaml
- data/normalized_yaml/algae/e31.yaml
- data/normalized_yaml/bacterial/e26_biotin.yaml
- data/normalized_yaml/bacterial/e31.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Natural sea water | {"value": "500", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / KNO3 | {"value": "0.2", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / K2HPO4 | {"value": "0.02", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / MgSO4 x 7 H2O | {"value": "0.02", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / Cyanocobalamine | {"value": "0.1", "unit": "MICROG_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[5].concentration / Thiamine HCl | {"value": "50", "unit": "MICROG_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[6].concentration / Biotin | {"value": "0.1", "unit": "MICROG_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[7].concentration / Soil | {"value": "variable", "unit": "VARIABLE"} | missing_attached_evidence; VARIABLE_REQUIRES_SOURCE | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://www.ccap.ac.uk/wp-content/uploads/MR_E31.pdf

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
