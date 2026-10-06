# Ingredient Concentration Review

- Record: data/merge_yaml/merged/BCYE_AGAR.yaml
- ID: CultureMech:002367
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: c97935ded0e4038da8fc740939038d67a62ed91bbab1f9459beb024614cfec80
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/2
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/1_10_r2a_agar.yaml
- data/normalized_yaml/bacterial/1_2_r2a_agar.yaml
- data/normalized_yaml/bacterial/JCM_J119_BCYE_AGAR.yaml
- data/normalized_yaml/bacterial/TOGO_M1288_Weak_Oatmeal_Agar.yaml
- data/normalized_yaml/bacterial/TOGO_M1547_Marine_Agar_2216.yaml
- data/normalized_yaml/bacterial/TOGO_M250_ME_Agar.yaml
- data/normalized_yaml/bacterial/TOGO_M455_Alkali-Reinforced_Clostridial_Agar.yaml
- data/normalized_yaml/bacterial/TOGO_M671_Modified_GAM_Agar.yaml
- data/normalized_yaml/bacterial/TOGO_M839_1_10_R2A_Agar.yaml
- data/normalized_yaml/bacterial/TOGO_M881_1_2_R2A_Agar.yaml
- data/normalized_yaml/bacterial/alkali_reinforced_clostridial_agar.yaml
- data/normalized_yaml/bacterial/bacto_marine_agar.yaml
- data/normalized_yaml/bacterial/marine_agar_2216.yaml
- data/normalized_yaml/bacterial/marine_agar_2216_ph_8_5.yaml
- data/normalized_yaml/bacterial/marine_agar_2216_ph_9_0.yaml
- data/normalized_yaml/bacterial/me_agar.yaml
- data/normalized_yaml/bacterial/modified_gam_agar.yaml
- data/normalized_yaml/bacterial/weak_oatmeal_agar.yaml
- data/normalized_yaml/specialized/bacto_marine_agar.yaml
- data/normalized_yaml/specialized/marine_agar_2216.yaml
- data/normalized_yaml/specialized/marine_agar_2216_ph_8_5.yaml
- data/normalized_yaml/specialized/marine_agar_2216_ph_9_0.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / R2A agar | {"value": "1.82", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Agar | {"value": "15", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=119

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
