# Ingredient Concentration Review

- Record: data/normalized_yaml/bacterial/mediadive_4185_Main_sol_J439.yaml
- ID: CultureMech:013209
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 7b0c88f6b65cbeba94ff4e71a997541020b41f091a9a0623c8d5e0ddd84d8aad
- Layer: normalized
- Record kind: SOLUTION
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/14
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/mediadive_4185_Main_sol_J439.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / See source for composition | {"value": "variable", "unit": "VARIABLE"} | missing_attached_evidence; VARIABLE_REQUIRES_SOURCE | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| composition[0].concentration / NaCl | {"value": "0.95511", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| composition[1].concentration / MgCl2 x 6 H2O | {"value": "0.382044", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| composition[2].concentration / CaCl2 x 2 H2O | {"value": "0.095511", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| composition[3].concentration / NH4Cl | {"value": "0.238777", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| composition[4].concentration / KH2PO4 | {"value": "1.91022", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| composition[5].concentration / KCl | {"value": "0.477555", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| composition[6].concentration / Yeast extract | {"value": "0.477555", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| composition[7].concentration / Na2SO4 | {"value": "3.82044", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| composition[8].concentration / Resazurin | {"value": "0.00095511", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| composition[9].concentration / Distilled water | {"value": "955.1098376313277", "unit": "PERCENT_V_V"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| composition[10].concentration / Sodium lactate | {"value": "19.102196752626554", "unit": "PERCENT_V_V"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| composition[11].concentration / NaHCO3 | {"value": "19.102196752626554", "unit": "PERCENT_V_V"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| composition[12].concentration / Na2S x 9 H2O | {"value": "1.9102196752626552", "unit": "PERCENT_V_V"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.


## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
