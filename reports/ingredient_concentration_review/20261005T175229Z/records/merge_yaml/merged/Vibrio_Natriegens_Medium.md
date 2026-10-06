# Ingredient Concentration Review

- Record: data/merge_yaml/merged/Vibrio_Natriegens_Medium.yaml
- ID: CultureMech:003869
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 2eb436d99bd8705775f1e632067e1742cbaf866e80592cb64f35a7eed2ab2284
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/4
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/1_100_nutrient_agar_no_2.yaml
- data/normalized_yaml/bacterial/1_10_nutrient_agar_no_2.yaml
- data/normalized_yaml/bacterial/JCM_J23_1_10_NUTRIENT_AGAR_NO._2.yaml
- data/normalized_yaml/bacterial/JCM_J24_1_100_NUTRIENT_AGAR_NO._2.yaml
- data/normalized_yaml/bacterial/KOMODO_101_NUTRIENT_AGAR_or_BROTH_WITH_NaCl.yaml
- data/normalized_yaml/bacterial/KOMODO_114_PARACOCCUS_HALODENITRIFICANS_medium.yaml
- data/normalized_yaml/bacterial/KOMODO_115_VIBRIO_NATRIEGENS_medium.yaml
- data/normalized_yaml/bacterial/KOMODO_952_1_10_NUTRIENT_AGAR_NO.2.yaml
- data/normalized_yaml/bacterial/KOMODO_953_1_100_NUTRIENT_AGAR_NO.2.yaml
- data/normalized_yaml/bacterial/TOGO_M16_1_10_Nutrient_Agar_NO._2.yaml
- data/normalized_yaml/bacterial/TOGO_M17_1_100_Nutrient_Agar_NO._2.yaml
- data/normalized_yaml/bacterial/TOGO_M2285_Vibrio_Natriegens_Medium.yaml
- data/normalized_yaml/bacterial/nutrient_agar_or_broth_with_nacl.yaml
- data/normalized_yaml/bacterial/paracoccus_halodenitrificans_medium.yaml
- data/normalized_yaml/bacterial/reactivation_with_liquid_medium_115.yaml
- data/normalized_yaml/bacterial/vibrio_natriegens_medium.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Peptone | {"value": "0.1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Meat extract | {"value": "0.1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / NaCl | {"value": "0.05", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / Agar | {"value": "20", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.


## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
