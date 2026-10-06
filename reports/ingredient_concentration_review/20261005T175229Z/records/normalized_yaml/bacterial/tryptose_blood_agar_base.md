# Ingredient Concentration Review

- Record: data/normalized_yaml/bacterial/tryptose_blood_agar_base.yaml
- ID: CultureMech:009084
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: cb9e5c4f96491c7bab49d13b1c66d136f1209c05c664d5fc10bad9f593a36454
- Layer: normalized
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/1
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/tryptose_blood_agar_base.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Tryptose blood agar base (Difco Laboratories, Detroit, MI) | {"value": "variable", "unit": "VARIABLE"} | missing_attached_evidence; VARIABLE_REQUIRES_SOURCE | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://togomedium.org/medium/M2512

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
