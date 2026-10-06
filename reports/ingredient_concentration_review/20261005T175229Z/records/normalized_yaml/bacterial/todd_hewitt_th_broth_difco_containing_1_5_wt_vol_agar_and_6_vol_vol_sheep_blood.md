# Ingredient Concentration Review

- Record: data/normalized_yaml/bacterial/todd_hewitt_th_broth_difco_containing_1_5_wt_vol_agar_and_6_vol_vol_sheep_blood.yaml
- ID: CultureMech:009445
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: dead33e444902e301b383f2c4e8de01be46086a8d95462c0582ed2896f0f1b26
- Layer: normalized
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/3
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/todd_hewitt_th_broth_difco_containing_1_5_wt_vol_agar_and_6_vol_vol_sheep_blood.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Sheep blood | {"value": "6", "unit": "PERCENT_V_V"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Agar | {"value": "1.5", "unit": "PERCENT_W_V"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Todd–Hewitt (TH) broth (Difco) | {"value": "1000", "unit": "ML_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- DOI:10.1016/j.micres.2013.09.007
- https://togomedium.org/medium/M2909

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
