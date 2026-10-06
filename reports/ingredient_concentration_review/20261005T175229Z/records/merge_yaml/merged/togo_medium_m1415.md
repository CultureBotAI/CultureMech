# Ingredient Concentration Review

- Record: data/merge_yaml/merged/togo_medium_m1415.yaml
- ID: CultureMech:007952
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 4f155b9415312030dd064d20e50a26ecd2f54835aea31717fe7697f226c7bb50
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/8
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/czapek_solution_agar_a.yaml
- data/normalized_yaml/bacterial/czapek_solution_agar_b.yaml
- data/normalized_yaml/bacterial/czapeks_agar_for_the_genomic_modified_aspergillus.yaml
- data/normalized_yaml/bacterial/czapeks_solution_agar_with_200_g_sucrose.yaml
- data/normalized_yaml/bacterial/sucrose_nitrate_agar_czapek_dox_agar.yaml
- data/normalized_yaml/bacterial/togo_medium_m1414.yaml
- data/normalized_yaml/bacterial/togo_medium_m1415.yaml
- data/normalized_yaml/fungal/czapek_solution_agar_a.yaml
- data/normalized_yaml/fungal/czapek_solution_agar_b.yaml
- data/normalized_yaml/fungal/czapeks_solution_agar_with_200_g_sucrose.yaml
- data/normalized_yaml/fungal/sucrose_nitrate_agar_czapek_dox_agar.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Distilled water | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / MgSO4・7H2O | {"value": "0.5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / K2HPO4 | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / FeSO4・7H2O | {"value": "10", "unit": "G_PER_L"} | missing_attached_evidence; PLAUSIBILITY_TRACE_SALT_AS_STOCK | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / KCl | {"value": "0.5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[5].concentration / NaNO3 | {"value": "3", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[6].concentration / Sucrose | {"value": "30", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[7].concentration / Agar | {"value": "20", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://togomedium.org/medium/M1415
- https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=10

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
