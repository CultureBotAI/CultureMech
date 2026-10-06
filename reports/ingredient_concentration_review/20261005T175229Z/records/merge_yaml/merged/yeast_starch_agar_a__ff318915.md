# Ingredient Concentration Review

- Record: data/merge_yaml/merged/yeast_starch_agar_a__ff318915.yaml
- ID: CultureMech:003539
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: df8b47f97460f8c1a9cc4f6b7eb4a05ccec770311a8ac00d0931ca47c27a120a
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/3
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/1_10_yeast_starch_agar.yaml
- data/normalized_yaml/bacterial/1_5_yeast_starch_agar.yaml
- data/normalized_yaml/bacterial/TOGO_M34_Yeast-Starch_Agar_A.yaml
- data/normalized_yaml/bacterial/acidic_yeast_starch_agar_ph_5_0.yaml
- data/normalized_yaml/bacterial/half_strength_yeast_starch_agar.yaml
- data/normalized_yaml/bacterial/yeast_extract_starch_agar_nbrc_med_266.yaml
- data/normalized_yaml/bacterial/yeast_starch_agar_a.yaml
- data/normalized_yaml/fungal/1_10_yeast_starch_agar.yaml
- data/normalized_yaml/fungal/1_5_yeast_starch_agar.yaml
- data/normalized_yaml/fungal/JCM_J42_YEAST-STARCH_AGAR_A.yaml
- data/normalized_yaml/fungal/acidic_yeast_starch_agar_ph_5_0.yaml
- data/normalized_yaml/fungal/half_strength_yeast_starch_agar.yaml
- data/normalized_yaml/fungal/yeast_extract_starch_agar_nbrc_med_266.yaml
- data/normalized_yaml/fungal/yeast_starch_agar_a.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Yeast extract | {"value": "2", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Starch | {"value": "10", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Agar | {"value": "15", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.


## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
