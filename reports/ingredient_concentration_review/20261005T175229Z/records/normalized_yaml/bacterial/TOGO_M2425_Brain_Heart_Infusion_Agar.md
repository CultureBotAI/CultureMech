# Ingredient Concentration Review

- Record: data/normalized_yaml/bacterial/TOGO_M2425_Brain_Heart_Infusion_Agar.yaml
- ID: CultureMech:009008
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: a95f60c039ba04f20565e60d909223a0c98b541407b9fabb69ea169a1915eac9
- Layer: normalized
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/2
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/TOGO_M2425_Brain_Heart_Infusion_Agar.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Brain Heart Infusion Agar (BD 211065) | {"value": "52", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / DI Water | {"value": "1000", "unit": "ML_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://togomedium.org/medium/M2425
- https://www.atcc.org/~/media/45E208A3191F4C7EA9B7E1063EB55303.ashx

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
