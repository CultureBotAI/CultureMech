# Ingredient Concentration Review

- Record: data/normalized_yaml/bacterial/JCM_J1347_FRESHWATER_THIOSULFATE_OXIDIZING_BACTERIA_MEDIUM.yaml
- ID: CultureMech:015883
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 4f65e8d0724a8314b4a0f017d5a254ed0f3bbd63f25f30749cf7082f363385b4
- Layer: normalized
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/2
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/JCM_J1347_FRESHWATER_THIOSULFATE_OXIDIZING_BACTERIA_MEDIUM.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Modified Wolfe's solution (see Medium No. 628 ) | {"value": "1000", "unit": "ML_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Trace minerals (see Medium No. 151 ) | {"value": "10.0", "unit": "ML_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1347

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
