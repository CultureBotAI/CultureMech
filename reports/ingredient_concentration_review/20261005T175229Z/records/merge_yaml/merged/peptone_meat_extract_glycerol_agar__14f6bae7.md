# Ingredient Concentration Review

- Record: data/merge_yaml/merged/peptone_meat_extract_glycerol_agar__14f6bae7.yaml
- ID: CultureMech:004622
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 03d067baa479d5d45c1d2b74ee5dc73becae2f004dfc973ad977d27c82c3658c
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/4
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/JCM_J518_PEPTONE-MEAT_EXTRACT-GLYCEROL_AGAR.yaml
- data/normalized_yaml/bacterial/KOMODO_250_Peptone_MEAT_EXTRACT_GLYCEROL_AGAR.yaml
- data/normalized_yaml/bacterial/TOGO_M2329_Peptone_Meat_Extract_Glycerol_Agar.yaml
- data/normalized_yaml/bacterial/TOGO_M519_Peptone-Meat_Extract-Glycerol_Agar.yaml
- data/normalized_yaml/bacterial/peptone_meat_extract_glycerol_agar.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Proteose peptone no. 3 | {"value": "5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Meat extract | {"value": "3", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Glycerol | {"value": "20", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / Agar | {"value": "20", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.


## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
