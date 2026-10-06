# Ingredient Concentration Review

- Record: data/normalized_yaml/bacterial/mediadive_1160_Main_sol_525.yaml
- ID: CultureMech:010656
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: b83482ff48b5e9460283866e349e46aea34e1ede52018da246a097069dffe9cf
- Layer: normalized
- Record kind: SOLUTION
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/16
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/mediadive_1160_Main_sol_525.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / See source for composition | {"value": "variable", "unit": "VARIABLE"} | missing_attached_evidence; VARIABLE_REQUIRES_SOURCE | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| composition[0].concentration / KCl | {"value": "0.336301", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| composition[1].concentration / MgCl2 x 6 H2O | {"value": "2.72008", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| composition[2].concentration / MgSO4 x 7 H2O | {"value": "3.41246", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| composition[3].concentration / NH4Cl | {"value": "0.24728", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| composition[4].concentration / K2HPO4 x 3 H2O | {"value": "0.138477", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| composition[5].concentration / CaCl2 x 2 H2O | {"value": "0.138477", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| composition[6].concentration / NaCl | {"value": "98.912", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| composition[7].concentration / Na-acetate | {"value": "0.98912", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| composition[8].concentration / Sodium resazurin | {"value": "0.00049456", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| composition[9].concentration / NaHCO3 | {"value": "3.95648", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| composition[10].concentration / Na2CO3 | {"value": "0.49456", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| composition[11].concentration / Trimethylamine-HCl | {"value": "4.9456", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| composition[12].concentration / L-Cysteine HCl x H2O | {"value": "0.49456", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| composition[13].concentration / Na2S x 9 H2O | {"value": "0.49456", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| composition[14].concentration / Distilled water | {"value": "989.1196834817014", "unit": "PERCENT_V_V"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.


## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
