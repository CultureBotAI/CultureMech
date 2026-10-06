# Ingredient Concentration Review

- Record: data/merge_yaml/merged/czapek_dox_agar.yaml
- ID: CultureMech:004065
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 106423f555664abb2fbf4c09668f687d980c552c2d794df1086ef9f0b3e5c128
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/7
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/czapek_dox_agar.yaml
- data/normalized_yaml/bacterial/czapek_solution_agar_a.yaml
- data/normalized_yaml/bacterial/czapek_solution_agar_b.yaml
- data/normalized_yaml/bacterial/czapeks_solution_agar_with_200_g_sucrose.yaml
- data/normalized_yaml/bacterial/sucrose_nitrate_agar_czapek_dox_agar.yaml
- data/normalized_yaml/fungal/czapek_dox_agar.yaml
- data/normalized_yaml/fungal/czapek_solution_agar_a.yaml
- data/normalized_yaml/fungal/czapek_solution_agar_b.yaml
- data/normalized_yaml/fungal/czapeks_solution_agar_with_200_g_sucrose.yaml
- data/normalized_yaml/fungal/sucrose_nitrate_agar_czapek_dox_agar.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Sucrose | {"value": "30", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / NaNO3 | {"value": "3", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / MgSO4 x 7 H2O | {"value": "0.5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / KCl | {"value": "0.5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / FeSO4 x 7 H2O | {"value": "0.01", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[5].concentration / K2HPO4 | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[6].concentration / Agar | {"value": "13", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.


## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
