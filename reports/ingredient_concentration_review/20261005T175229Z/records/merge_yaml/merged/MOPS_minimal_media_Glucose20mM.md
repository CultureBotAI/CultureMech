# Ingredient Concentration Review

- Record: data/merge_yaml/merged/MOPS_minimal_media_Glucose20mM.yaml
- ID: CultureMech:015629
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 8ec85427dd06a42bd3597ca1b6e219834c9c877cbb404973afbc6c87fa440655
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/16
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/specialized/mops_minimal_media_glucose20mm.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / D-Glucose | {"value": "20", "unit": "MILLIMOLAR"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Ammonium chloride | {"value": "9.5", "unit": "MILLIMOLAR"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / 3-(N-morpholino)propanesulfonic acid | {"value": "40", "unit": "MILLIMOLAR"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / Tricine | {"value": "4", "unit": "MILLIMOLAR"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / Potassium phosphate dibasic | {"value": "1.32", "unit": "MILLIMOLAR"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[5].concentration / Iron (II) sulfate heptahydrate | {"value": "0.01", "unit": "MILLIMOLAR"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[6].concentration / Aluminum potassium sulfate dodecahydrate | {"value": "0.276", "unit": "MILLIMOLAR"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[7].concentration / Calcium chloride | {"value": "0.0005", "unit": "MILLIMOLAR"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[8].concentration / Magnesium chloride hexahydrate | {"value": "0.525", "unit": "MILLIMOLAR"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[9].concentration / Sodium Chloride | {"value": "50", "unit": "MILLIMOLAR"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[10].concentration / Ammonium heptamolybdate tetrahydrate | {"value": "3.00E-09", "unit": "MOLAR"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[11].concentration / Boric Acid | {"value": "4.00E-07", "unit": "MOLAR"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[12].concentration / Cobalt chloride hexahydrate | {"value": "3.00E-08", "unit": "MOLAR"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[13].concentration / Copper (II) sulfate pentahydrate | {"value": "1.00E-08", "unit": "MOLAR"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[14].concentration / Manganese (II) chloride tetrahydrate | {"value": "8.00E-08", "unit": "MOLAR"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[15].concentration / Zinc sulfate heptahydrate | {"value": "1.00E-08", "unit": "MOLAR"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://github.com/CultureBotAI/CultureBotHT

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
