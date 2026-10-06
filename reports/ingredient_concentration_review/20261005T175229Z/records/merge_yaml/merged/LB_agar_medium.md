# Ingredient Concentration Review

- Record: data/merge_yaml/merged/LB_agar_medium.yaml
- ID: CultureMech:009664
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: a746a50b1936be4c64211e2ff2c3f3e5f73a86aafaa9ebb2d0019b16844eb150
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/4
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/1_3_lb_agar.yaml
- data/normalized_yaml/bacterial/2yt_medium.yaml
- data/normalized_yaml/bacterial/KOMODO_381_LB_Luria-Bertani_medium.yaml
- data/normalized_yaml/bacterial/TOGO_M1270_LB_Luria-Bertani_Agar_With_5_NaCl_pH_9.0.yaml
- data/normalized_yaml/bacterial/TOGO_M1334_LB_Luria-Bertani_Agar_With_5_NaCl.yaml
- data/normalized_yaml/bacterial/TOGO_M2476_LB_Luria-Bertani_Medium.yaml
- data/normalized_yaml/bacterial/TOGO_M2619_LB_Luria-Bertani_Medium.yaml
- data/normalized_yaml/bacterial/TOGO_M443_LB_Luria-Bertani_Agar.yaml
- data/normalized_yaml/bacterial/TOGO_M878_1_3_LB_Agar.yaml
- data/normalized_yaml/bacterial/half_concentrated_lb_luria_bertani_medium.yaml
- data/normalized_yaml/bacterial/lb_agar_medium.yaml
- data/normalized_yaml/bacterial/lb_luria_bertani_agar.yaml
- data/normalized_yaml/bacterial/lb_luria_bertani_agar_with_5_nacl.yaml
- data/normalized_yaml/bacterial/lb_luria_bertani_agar_with_5_nacl_ph_9_0.yaml
- data/normalized_yaml/bacterial/lb_luria_bertani_medium.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Tryptone | {"value": "3.3", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Yeast extract | {"value": "1.7", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / NaCl | {"value": "5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / Agar | {"value": "15", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://togomedium.org/medium/M3224
- https://www.laboratorynotes.com/preparation-of-luria-bertani-lb-miller-broth/

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
