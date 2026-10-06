# Ingredient Concentration Review

- Record: data/merge_yaml/merged/rpmi_medium_supplemented_with_2_fetal_bovine_serum.yaml
- ID: CultureMech:009482
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: e57cdf3da1e0440bbe011d7e1f6ae964d610a7332eb964fe95e7ed97977e1265
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/2
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/rpmi_medium_supplemented_with_2_fetal_bovine_serum.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / fetal bovine serum | {"value": "2", "unit": "PERCENT_W_V"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / RPMI medium (Invitrogen, Carlsbad, CA) | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://togomedium.org/medium/M2958

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
