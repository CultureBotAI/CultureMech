# Ingredient Concentration Review

- Record: data/normalized_yaml/bacterial/m9_phenanthrene.yaml
- ID: CultureMech:008631
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: a8199094b6b1d454a2aebee945a0670dcdd08de4e4a87deb4e64b37b2fea7abf
- Layer: normalized
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/21
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/m9_phenanthrene.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Agar solution | {"value": "900", "unit": "ML_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / 10xM9 solution | {"value": "100", "unit": "ML_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / MgSO4 solution | {"value": "2.1", "unit": "ML_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / CaCl2 solution | {"value": "1", "unit": "ML_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / Phenanthrene solution | {"value": "10", "unit": "ML_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[0].concentration / Agar solution | {"value": "900", "unit": "ML_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[0].composition[0].concentration / Agar | {"value": "15", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[0].composition[1].concentration / Distilled water | {"value": "900", "unit": "ML_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[1].concentration / 10xM9 solution | {"value": "100", "unit": "ML_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[1].composition[0].concentration / KH2PO4 | {"value": "30", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[1].composition[1].concentration / Na2HPO4 | {"value": "60", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[1].composition[2].concentration / NH4Cl | {"value": "10", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[1].composition[3].concentration / NaCl | {"value": "5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[1].composition[4].concentration / Distilled water | {"value": "1", "unit": "L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[2].concentration / MgSO4 solution | {"value": "2.1", "unit": "ML_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[2].composition[0].concentration / MgSO4 | {"value": "1", "unit": "MOLAR"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[3].concentration / CaCl2 solution | {"value": "1", "unit": "ML_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[3].composition[0].concentration / CaCl2 | {"value": "0.1", "unit": "MOLAR"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[4].concentration / Phenanthrene solution | {"value": "10", "unit": "ML_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[4].composition[0].concentration / Phenanthrene | {"value": "250", "unit": "MILLIMOLAR"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[4].composition[1].concentration / Dimethyl sulfoxide (DMSO) | {"value": "variable", "unit": "VARIABLE"} | missing_attached_evidence; VARIABLE_REQUIRES_SOURCE | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://togomedium.org/medium/M2041
- https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2041
- https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1339

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
