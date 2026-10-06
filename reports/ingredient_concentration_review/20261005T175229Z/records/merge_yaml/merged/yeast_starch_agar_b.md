# Ingredient Concentration Review

- Record: data/merge_yaml/merged/yeast_starch_agar_b.yaml
- ID: CultureMech:006234
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: a74cf192f28013bb305409b90e39ab1d4dfe7076f25cfb4c97c386ffd85e2197
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/5
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/KOMODO_190_YpSs_medium.yaml
- data/normalized_yaml/bacterial/TOGO_M329_YpSs_Agar.yaml
- data/normalized_yaml/bacterial/TOGO_M53_Yeast-Starch_Agar_B.yaml
- data/normalized_yaml/bacterial/emersons_yeast_starch_agar.yaml
- data/normalized_yaml/bacterial/yeast_starch_agar_b.yaml
- data/normalized_yaml/bacterial/ypss_agar.yaml
- data/normalized_yaml/bacterial/ypss_medium.yaml
- data/normalized_yaml/fungal/JCM_J61_YEAST-STARCH_AGAR_B.yaml
- data/normalized_yaml/fungal/emersons_yeast_starch_agar.yaml
- data/normalized_yaml/fungal/yeast_starch_agar_b.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Yeast extract | {"value": "4", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Starch | {"value": "15", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / K2HPO4 | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / MgSO4 x 7 H2O | {"value": "0.5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / Agar | {"value": "15", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.


## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
