# Ingredient Concentration Review

- Record: data/merge_yaml/merged/anaerobic_seawater_swm_medium.yaml
- ID: CultureMech:015356
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 6b50d4e32adbfd3d4e8458d32ca630d702d0be2900c0fb9f51063627b8889d3f
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/29
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/for_dsm_11046.yaml
- data/normalized_yaml/bacterial/for_dsm_11261.yaml
- data/normalized_yaml/bacterial/for_dsm_11262.yaml
- data/normalized_yaml/bacterial/for_dsm_11263_and_dsm_11489.yaml
- data/normalized_yaml/bacterial/for_dsm_12881.yaml
- data/normalized_yaml/bacterial/for_dsm_13326.yaml
- data/normalized_yaml/bacterial/for_dsm_13327.yaml
- data/normalized_yaml/bacterial/for_dsm_13687.yaml
- data/normalized_yaml/bacterial/for_dsm_14424.yaml
- data/normalized_yaml/bacterial/for_dsm_14691.yaml
- data/normalized_yaml/bacterial/for_dsm_15206.yaml
- data/normalized_yaml/bacterial/for_dsm_15970.yaml
- data/normalized_yaml/bacterial/for_dsm_15978.yaml
- data/normalized_yaml/bacterial/for_dsm_19335.yaml
- data/normalized_yaml/bacterial/for_dsm_19636.yaml
- data/normalized_yaml/bacterial/for_dsm_21662.yaml
- data/normalized_yaml/bacterial/for_dsm_5651.yaml
- data/normalized_yaml/bacterial/for_dsm_5847.yaml
- data/normalized_yaml/bacterial/for_dsm_5848.yaml
- data/normalized_yaml/bacterial/for_dsm_5849.yaml
- data/normalized_yaml/bacterial/for_dsm_6233.yaml
- data/normalized_yaml/bacterial/for_dsm_6779.yaml
- data/normalized_yaml/bacterial/for_dsm_9705.yaml
- data/normalized_yaml/bacterial/fwm_medium.yaml
- data/normalized_yaml/bacterial/fwm_medium_modified.yaml
- data/normalized_yaml/bacterial/medium_503_modified_for_dsm_11045.yaml
- data/normalized_yaml/bacterial/medium_503_modified_for_dsm_11480.yaml
- data/normalized_yaml/bacterial/medium_503_modified_for_dsm_11493.yaml
- data/normalized_yaml/bacterial/medium_503_modified_for_dsm_12018.yaml
- data/normalized_yaml/bacterial/medium_503b_modified_for_dsm_14691.yaml
- data/normalized_yaml/bacterial/medium_503b_modified_for_dsm_14692.yaml
- data/normalized_yaml/bacterial/modified_vwm_medium.yaml
- data/normalized_yaml/bacterial/swm_medium.yaml
- data/normalized_yaml/bacterial/tmao3_tmpn3_medium.yaml
- data/normalized_yaml/specialized/anaerobic_freshwater_fwm_medium.yaml
- data/normalized_yaml/specialized/anaerobic_seawater_swm_medium.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / KH2PO4 | {"value": "0.212314", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / NH4Cl | {"value": "0.265393", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / NaCl | {"value": "1.06157", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / MgCl2 x 6 H2O | {"value": "0.424628", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / KCl | {"value": "0.530786", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[5].concentration / CaCl2 x 2 H2O | {"value": "0.159236", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[6].concentration / Sodium resazurin | {"value": "0.000530786", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[7].concentration / Na2CO3 | {"value": "50", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[8].concentration / D-Glucose | {"value": "250", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[9].concentration / Na2S x 9 H2O | {"value": "30", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[10].concentration / HCl | {"value": "2.5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[11].concentration / FeCl2 x 4 H2O | {"value": "1.5", "unit": "G_PER_L"} | missing_attached_evidence; PLAUSIBILITY_TRACE_SALT_AS_STOCK | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[12].concentration / ZnCl2 | {"value": "0.07", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[13].concentration / MnCl2 x 4 H2O | {"value": "0.1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[14].concentration / H3BO3 | {"value": "0.006", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[15].concentration / CoCl2 x 6 H2O | {"value": "0.19", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[16].concentration / CuCl2 x 2 H2O | {"value": "0.002", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[17].concentration / NiCl2 x 6 H2O | {"value": "0.024", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[18].concentration / Na2MoO4 x 2 H2O | {"value": "0.036", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[19].concentration / NaOH | {"value": "0.5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[20].concentration / Na2SeO3 x 5 H2O | {"value": "0.003", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[21].concentration / Na2WO4 x 2 H2O | {"value": "0.004", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[22].concentration / Vitamin B12 | {"value": "0.1", "unit": "G_PER_L"} | missing_attached_evidence; PLAUSIBILITY_INDICATOR_UNIT_SLIP | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[23].concentration / p-Aminobenzoic acid | {"value": "0.08", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[24].concentration / D-(+)-biotin | {"value": "0.02", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[25].concentration / Nicotinic acid | {"value": "0.2", "unit": "G_PER_L"} | missing_attached_evidence; PLAUSIBILITY_INDICATOR_UNIT_SLIP | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[26].concentration / Calcium pantothenate | {"value": "0.1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[27].concentration / Pyridoxine hydrochloride | {"value": "0.3", "unit": "G_PER_L"} | missing_attached_evidence; PLAUSIBILITY_INDICATOR_UNIT_SLIP | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[28].concentration / Thiamine-HCl x 2 H2O | {"value": "0.2", "unit": "G_PER_L"} | missing_attached_evidence; PLAUSIBILITY_INDICATOR_UNIT_SLIP | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium504.pdf

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
