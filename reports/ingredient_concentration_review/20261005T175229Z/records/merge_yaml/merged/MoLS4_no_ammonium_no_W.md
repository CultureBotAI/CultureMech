# Ingredient Concentration Review

- Record: data/merge_yaml/merged/MoLS4_no_ammonium_no_W.yaml
- ID: CultureMech:015612
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: aa162758d694f95e6fbcb1ef3b5fb8631a628535b2b80959b1f948b68a4d8703
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/3
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/specialized/mols4_no_ammonium_no_w.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / MoLS4 | {"value": "1", "unit": "FOLD_DILUTION"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Ammonium chloride | {"value": "-", "unit": "G_PER_L"} | missing_attached_evidence; RANGE_OR_NONNUMERIC_REQUIRES_SOURCE | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Sodium tungstate dihydrate | {"value": "-", "unit": "G_PER_L"} | missing_attached_evidence; RANGE_OR_NONNUMERIC_REQUIRES_SOURCE | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://github.com/CultureBotAI/CultureBotHT

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
