# Ingredient Concentration Review

- Record: data/merge_yaml/merged/LB_Medium.yaml
- ID: CultureMech:008901
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 00e8a039e9031c87aa21742be3519ca342469470a74dcd6f1d2df9e9efff9a82
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/4
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/algae/lb.yaml
- data/normalized_yaml/bacterial/2_x_yt_medium.yaml
- data/normalized_yaml/bacterial/TOGO_M1329_LB_Luria-Bertani_Medium_Lennox.yaml
- data/normalized_yaml/bacterial/TOGO_M1330_LB_Luria-Bertani_Medium_Lennox.yaml
- data/normalized_yaml/bacterial/TOGO_M2314_LB_medium.yaml
- data/normalized_yaml/bacterial/TOGO_M316_2_x_YT_Medium.yaml
- data/normalized_yaml/bacterial/TOGO_M3227_LB_broth.yaml
- data/normalized_yaml/bacterial/TOGO_M848_LB_Luria-Bertani_Broth_With_1_mM_DTT.yaml
- data/normalized_yaml/bacterial/lb_agar.yaml
- data/normalized_yaml/bacterial/lb_broth.yaml
- data/normalized_yaml/bacterial/lb_broth_medium.yaml
- data/normalized_yaml/bacterial/lb_luria_bertani_broth_with_1_mm_dtt.yaml
- data/normalized_yaml/bacterial/lb_luria_bertani_medium_lennox.yaml
- data/normalized_yaml/bacterial/lb_medium_difco.yaml
- data/normalized_yaml/bacterial/lb_medium_lennox.yaml
- data/normalized_yaml/bacterial/lb_with_addition_of_1_wt_vol_nacl.yaml
- data/normalized_yaml/fungal/tryptone_yeast_extract_medium.yaml
- data/normalized_yaml/fungal/tryptone_yeast_extract_medium_modified.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / NaCl | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Tryptone | {"value": "10.0", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Yeast extract | {"value": "5.0", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / Sodium chloride | {"value": "10.0", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- PMID:16628448
- https://togomedium.org/medium/M2314
- https://www.laboratorynotes.com/preparation-of-luria-bertani-lb-miller-broth/

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
