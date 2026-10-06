# Ingredient Concentration Review

- Record: data/merge_yaml/merged/CORN_MEAL_AGAR.yaml
- ID: CultureMech:004218
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: c7fc255ccc425575a494b834d7a9fdeb46b1ee706ad254fa8bdb6c95b490e925
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/2
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/JCM_J1329_CORN_MEAL_AGAR.yaml
- data/normalized_yaml/bacterial/JCM_J150_CORN_MEAL_AGAR.yaml
- data/normalized_yaml/bacterial/KOMODO_191_CORN_MEAL_AGAR.yaml
- data/normalized_yaml/bacterial/TOGO_M141_Corn_Meal_Agar.yaml
- data/normalized_yaml/bacterial/TOGO_M3004_Corn_Meal_Agar.yaml
- data/normalized_yaml/bacterial/corn_meal_agar.yaml
- data/normalized_yaml/bacterial/for_dsm_25939.yaml
- data/normalized_yaml/bacterial/for_dsm_25945.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Corn meal | {"value": "50", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Agar | {"value": "10", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.


## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
