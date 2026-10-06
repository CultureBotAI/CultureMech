# Ingredient Concentration Review

- Record: data/merge_yaml/merged/alcanivorax_balericus_medium.yaml
- ID: CultureMech:004039
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 1d80ed5c2d0f75254a1feb0190cdefcb5fd57a4903768e91051705d515c0a3f2
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/4
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/KOMODO_1289_ALCANIVORAX_BALERICUS_medium.yaml
- data/normalized_yaml/bacterial/TOGO_M15_Nutrient_Agar_NO._2.yaml
- data/normalized_yaml/bacterial/TOGO_M405_Nutrient_Agar_With_50_Soil_Extract_And_5_NaCl.yaml
- data/normalized_yaml/bacterial/alcanivorax_balericus_medium.yaml
- data/normalized_yaml/bacterial/na_sphingobacterium_medium.yaml
- data/normalized_yaml/bacterial/nutrient_agar_no_2.yaml
- data/normalized_yaml/bacterial/nutrient_agar_with_50_soil_extract_and_5_nacl.yaml
- data/normalized_yaml/bacterial/volcanobacter_medium.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Peptone | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Beef extract | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / NaCl | {"value": "0.5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / Agar | {"value": "15", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.


## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
