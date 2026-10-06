# Ingredient Concentration Review

- Record: data/normalized_yaml/algae/volvox.yaml
- ID: CultureMech:000215
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 462ec5ada44f7bc112321914258ec64f84232494bea8edb96d30038fd0c4bb9e
- Layer: normalized
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/19
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/algae/volvox.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Na2glycerophosphate x 5 H2O | {"value": "60", "unit": "MG_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Glycyl-glycine | {"value": "500", "unit": "MG_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Deionized or distilled water | {"value": "964", "unit": "ML_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / Vitamin B12 | {"value": "0.005", "unit": "MG_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / Thiamine | {"value": "0.5", "unit": "MG_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[0].concentration / Ca(NO3)2 x 4 H2O stock solution | {"value": "10", "unit": "ML_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[0].composition[0].concentration / Ca(NO3)2 x 4 H2O | {"value": "118", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[1].concentration / MgSO4 x 7 H2O stock solution | {"value": "10", "unit": "ML_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[1].composition[0].concentration / MgSO4 x 7 H2O | {"value": "40", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[2].concentration / KCl stock solution | {"value": "10", "unit": "ML_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[2].composition[0].concentration / KCl | {"value": "50", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[3].concentration / Volvox micronutrient solution | {"value": "6", "unit": "ML_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[3].composition[0].concentration / Na2EDTA | {"value": "750", "unit": "MG_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[3].composition[1].concentration / FeCl3 x 6 H2O | {"value": "97", "unit": "MG_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[3].composition[2].concentration / MnCl2 x 4 H2O | {"value": "41", "unit": "MG_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[3].composition[3].concentration / ZnCl2 | {"value": "5", "unit": "MG_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[3].composition[4].concentration / CoCl2 x 6 H2O | {"value": "2", "unit": "MG_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[3].composition[5].concentration / Na2MoO4 x 2 H2O | {"value": "4", "unit": "MG_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[3].composition[6].concentration / Deionized or distilled water | {"value": "1", "unit": "L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- http://sagdb.uni-goettingen.de/culture_media/22
- https://sagdb.uni-goettingen.de/culture_media/22%20Volvox%20Medium.pdf

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
