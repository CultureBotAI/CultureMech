# Ingredient Concentration Review

- Record: data/normalized_yaml/specialized/pye.yaml
- ID: CultureMech:015685
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: bfed303be3cde8d9cd4016b71e3b48217239c08e7b19fec9485f80b8fcff8418
- Layer: normalized
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/4
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/specialized/pye.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Peptone | {"value": "2", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Yeast Extract | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Magnesium sulfate | {"value": "0.8", "unit": "MILLIMOLAR"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / Calcium chloride | {"value": "0.5", "unit": "MILLIMOLAR"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://github.com/CultureBotAI/CultureBotHT

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
