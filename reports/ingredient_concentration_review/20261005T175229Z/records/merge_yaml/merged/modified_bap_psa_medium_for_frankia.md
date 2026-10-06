# Ingredient Concentration Review

- Record: data/merge_yaml/merged/modified_bap_psa_medium_for_frankia.yaml
- ID: CultureMech:001143
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: c30d55cc7a3fd537c272f634a67e0ce388febcbe609d5f72f69e3858909d4dd0
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/20
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/modified_bap_psa_medium_for_frankia.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / KH2PO4 | {"value": "0.95", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / K2HPO4 | {"value": "0.6", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / NH4Cl | {"value": "0.27", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / Na-propionate | {"value": "0.48", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / Sodium succinate dibasic | {"value": "0.48", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[5].concentration / Pyruvic acid sodium salt | {"value": "0.48", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[6].concentration / Sodium acetate | {"value": "0.48", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[7].concentration / MgSO4 x 7 H2O | {"value": "0.025", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[8].concentration / CaCl2 x 2 H2O | {"value": "0.01", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[9].concentration / Thiamine HCl | {"value": "0.1", "unit": "G_PER_L"} | missing_attached_evidence; PLAUSIBILITY_INDICATOR_UNIT_SLIP | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[10].concentration / Nicotinic acid | {"value": "0.5", "unit": "G_PER_L"} | missing_attached_evidence; PLAUSIBILITY_INDICATOR_UNIT_SLIP | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[11].concentration / Pyridoxine hydrochloride | {"value": "0.5", "unit": "G_PER_L"} | missing_attached_evidence; PLAUSIBILITY_INDICATOR_UNIT_SLIP | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[12].concentration / Citric acid | {"value": "10", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[13].concentration / Eisencitrat | {"value": "10", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[14].concentration / CoSO4 x 7 H2O | {"value": "0.01", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[15].concentration / CuSO4 x 5 H2O | {"value": "0.8", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[16].concentration / H3BO3 | {"value": "28.6", "unit": "G_PER_L"} | missing_attached_evidence; PLAUSIBILITY_TRACE_SALT_AS_STOCK | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[17].concentration / MnCl2 x 4 H2O | {"value": "18.1", "unit": "G_PER_L"} | missing_attached_evidence; PLAUSIBILITY_TRACE_SALT_AS_STOCK | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[18].concentration / Na2MoO4 x 2 H2O | {"value": "0.25", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[19].concentration / ZnSO4 x 7 H2O | {"value": "2.2", "unit": "G_PER_L"} | missing_attached_evidence; PLAUSIBILITY_TRACE_SALT_AS_STOCK | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1660.pdf

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
