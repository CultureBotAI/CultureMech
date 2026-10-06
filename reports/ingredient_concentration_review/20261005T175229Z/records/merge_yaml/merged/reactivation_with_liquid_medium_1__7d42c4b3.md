# Ingredient Concentration Review

- Record: data/merge_yaml/merged/reactivation_with_liquid_medium_1__7d42c4b3.yaml
- ID: CultureMech:001298
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: cbfbd139a8aad0daf15e57152436c0d855767b7019723fc4e99b4ab6a0c58ae1
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/3
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/JCM_J74_NUTRIENT_AGAR.yaml
- data/normalized_yaml/bacterial/KOMODO_1_NUTRIENT_AGAR.yaml
- data/normalized_yaml/bacterial/NBRC_NUTRIENT_AGAR.yaml
- data/normalized_yaml/bacterial/TOGO_M2339_Nutrient_Agar.yaml
- data/normalized_yaml/bacterial/TOGO_M2340_Nutrient_Agar.yaml
- data/normalized_yaml/bacterial/TOGO_M2358_Reactivation_With_Liquid_Medium_1.yaml
- data/normalized_yaml/bacterial/TOGO_M2417_Nutrient_Agar.yaml
- data/normalized_yaml/bacterial/TOGO_M3116_Nutrient_Agar.yaml
- data/normalized_yaml/bacterial/TOGO_M3212_Nutrient_agar.yaml
- data/normalized_yaml/bacterial/TOGO_M65_Nutrient_Agar.yaml
- data/normalized_yaml/bacterial/nutrient_agar.yaml
- data/normalized_yaml/bacterial/reactivation_with_liquid_medium_1.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Peptone | {"value": "5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Meat extract | {"value": "3", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Agar | {"value": "15", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1a.pdf

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
