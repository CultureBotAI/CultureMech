# Ingredient Concentration Review

- Record: data/merge_yaml/merged/M9ZB_with_glucose.yaml
- ID: CultureMech:006992
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 3c8c3ed1cea1a7a9905318528522919f607e31b270683ac8b8bd5e9a7f23fce5
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/7
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/m9_farmer_et_al.yaml
- data/normalized_yaml/bacterial/m9_medium_kolisnychenko_et_al.yaml
- data/normalized_yaml/bacterial/m9_park_et_al.yaml
- data/normalized_yaml/bacterial/m9_purvis.yaml
- data/normalized_yaml/bacterial/m9_with_0_4_glucose_prachaiyo_et_al.yaml
- data/normalized_yaml/bacterial/m9_with_0_7_glucose_prachaiyo_et_al.yaml
- data/normalized_yaml/bacterial/m9_with_1_0_glucose_prachaiyo_et_al.yaml
- data/normalized_yaml/bacterial/m9zb_with_glucose.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / D-Glucose | {"value": "27.7531", "unit": "MILLIMOLAR"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Calcium chloride anhydrous | {"value": "0.1", "unit": "MILLIMOLAR"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Dibasic sodium phosphate | {"value": "42.2654", "unit": "MILLIMOLAR"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / Sodium chloride | {"value": "8.55578", "unit": "MILLIMOLAR"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / Potassium dihydrogen phosphate | {"value": "22.0449", "unit": "MILLIMOLAR"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[5].concentration / Magnesium sulfate | {"value": "1.0", "unit": "MILLIMOLAR"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[6].concentration / Ammonium chloride | {"value": "18.6947", "unit": "MILLIMOLAR"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://mediadb.systemsbiology.net/

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
