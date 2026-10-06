# Ingredient Concentration Review

- Record: data/merge_yaml/merged/ALKALINE_NUTRIENT_AGAR.yaml
- ID: CultureMech:005008
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 1da797ef230ebdb314eb094466a87e8a126e68a1c2cd51bfd1e5bd6d6e4e02f4
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/5
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/JCM_J100_ALKALINE_NUTRIENT_AGAR.yaml
- data/normalized_yaml/bacterial/KOMODO_31_ALKALINE_NUTRIENT_AGAR.yaml
- data/normalized_yaml/bacterial/TOGO_M2420_Alkaline_Nutrient_Agar.yaml
- data/normalized_yaml/bacterial/TOGO_M92_Alkaline_Nutrient_Agar.yaml
- data/normalized_yaml/bacterial/alkaline_nutrient_agar.yaml
- data/normalized_yaml/bacterial/medium_31_modified_for_dsm_16130.yaml
- data/normalized_yaml/bacterial/medium_31_modified_for_dsm_23228.yaml
- data/normalized_yaml/bacterial/medium_31_modified_for_dsm_5271.yaml
- data/normalized_yaml/bacterial/medium_31_modified_for_dsm_6716.yaml
- data/normalized_yaml/bacterial/medium_31_modified_for_dsm_8714.yaml
- data/normalized_yaml/bacterial/medium_31_modified_for_dsm_8716.yaml
- data/normalized_yaml/bacterial/medium_31_modified_for_dsm_8717.yaml
- data/normalized_yaml/bacterial/medium_31_modified_for_dsm_8719.yaml
- data/normalized_yaml/bacterial/medium_31_modified_for_dsm_8720.yaml
- data/normalized_yaml/bacterial/medium_31_modified_for_dsm_8721.yaml
- data/normalized_yaml/bacterial/medium_31_modified_for_dsm_8722.yaml
- data/normalized_yaml/bacterial/medium_31_modified_for_dsm_8723.yaml
- data/normalized_yaml/bacterial/medium_31_modified_for_dsm_8724.yaml
- data/normalized_yaml/bacterial/medium_31_modified_for_dsm_8725.yaml
- data/normalized_yaml/bacterial/medium_31_modified_for_dsm_9473.yaml
- data/normalized_yaml/bacterial/medium_31_modified_for_dsm_9474.yaml
- data/normalized_yaml/bacterial/medium_31_modified_for_dsm_9475.yaml
- data/normalized_yaml/bacterial/medium_31_modified_for_dsm_9476.yaml
- data/normalized_yaml/bacterial/medium_31_modified_for_dsm_9477.yaml
- data/normalized_yaml/bacterial/medium_31_modified_for_dsm_9478.yaml
- data/normalized_yaml/bacterial/medium_31_modified_for_dsm_9479.yaml
- data/normalized_yaml/bacterial/medium_31_modified_for_dsm_9480.yaml
- data/normalized_yaml/bacterial/medium_31_modified_for_dsm_9481.yaml
- data/normalized_yaml/bacterial/medium_31_modified_for_dsm_9482.yaml
- data/normalized_yaml/bacterial/medium_31_modified_for_dsm_9706.yaml
- data/normalized_yaml/bacterial/medium_31_modified_for_dsm_9711.yaml
- data/normalized_yaml/bacterial/medium_31_modified_for_dsm_9712.yaml
- data/normalized_yaml/bacterial/medium_31_modified_for_dsm_9713.yaml
- data/normalized_yaml/bacterial/medium_31_modified_for_dsm_9714.yaml
- data/normalized_yaml/bacterial/medium_31_modified_for_dsm_9725.yaml
- data/normalized_yaml/bacterial/medium_31_modified_for_dsm_9726.yaml
- data/normalized_yaml/bacterial/medium_31_modified_for_dsm_9727.yaml
- data/normalized_yaml/bacterial/medium_31_modified_for_dsm_9728.yaml
- data/normalized_yaml/bacterial/medium_31_modified_for_dsm_9729.yaml
- data/normalized_yaml/bacterial/medium_31_modified_for_dsm_9730.yaml
- data/normalized_yaml/bacterial/medium_31_modified_for_dsm_9731.yaml
- data/normalized_yaml/bacterial/medium_31_modified_for_dsm_9763.yaml
- data/normalized_yaml/bacterial/medium_31_modified_for_dsm_9768.yaml
- data/normalized_yaml/bacterial/medium_31_modified_for_dsm_9778.yaml
- data/normalized_yaml/bacterial/medium_31_modified_for_dsm_9779.yaml
- data/normalized_yaml/bacterial/medium_31_modified_for_dsm_9780.yaml
- data/normalized_yaml/bacterial/medium_31_modified_for_dsm_9781.yaml
- data/normalized_yaml/bacterial/medium_31_modified_for_dsm_9782.yaml
- data/normalized_yaml/bacterial/medium_31_modified_for_dsm_9783.yaml
- data/normalized_yaml/bacterial/medium_31_modified_for_dsm_9784.yaml
- data/normalized_yaml/bacterial/medium_31_modified_for_dsm_9785.yaml
- data/normalized_yaml/bacterial/medium_31_modified_for_dsm_9813.yaml
- data/normalized_yaml/bacterial/medium_31_modified_for_dsm_9818.yaml
- data/normalized_yaml/bacterial/medium_31_modified_for_dsm_9822.yaml
- data/normalized_yaml/bacterial/medium_31_modified_for_dsm_9823.yaml
- data/normalized_yaml/bacterial/medium_31_modified_for_dsm_9881.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Peptone | {"value": "5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Meat extract | {"value": "3", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Agar | {"value": "15", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / NaHCO3 | {"value": "42", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / Na2CO3 anhydrous | {"value": "53", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.


## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
