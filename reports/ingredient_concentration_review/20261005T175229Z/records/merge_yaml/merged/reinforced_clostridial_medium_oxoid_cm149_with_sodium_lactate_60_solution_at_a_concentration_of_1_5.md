# Ingredient Concentration Review

- Record: data/merge_yaml/merged/reinforced_clostridial_medium_oxoid_cm149_with_sodium_lactate_60_solution_at_a_concentration_of_1_5.yaml
- ID: CultureMech:009180
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 8f984b56d7093feacdf8f3e89ee306af9b50caa24f7b39a69b0187d1a001a722
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/3
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/reinforced_clostridial_medium_oxoid_cm149_with_sodium_lactate_60_solution_at_a_concentration_of_1_5.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Distilled water | {"value": "1000", "unit": "G_PER_L"} | missing_attached_evidence; PLAUSIBILITY_WATER_AS_VOLUME | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Reinforced Clostridial medium (Oxoid CM149) | {"value": "38", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[0].concentration / Sodium lactate (60% solution) | {"value": "1.5", "unit": "PERCENT_W_V"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://togomedium.org/medium/M2613
- https://www.atcc.org/~/media/CCB197296D624B1DA0BBFA3C2EB8632B.ashx

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
