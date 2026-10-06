# Ingredient Concentration Review

- Record: data/normalized_yaml/bacterial/10_wt_wt_skim_milk_supplemented_with_1_mm_sodium_formate.yaml
- ID: CultureMech:009451
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: ee6dbf237c54abdcfb480f60801e38d3b9ed2f6284d5a1734c82824360e00096
- Layer: normalized
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/2
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/10_wt_wt_skim_milk_supplemented_with_1_mm_sodium_formate.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Skim milk | {"value": "10", "unit": "PERCENT_W_W"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Sodium formate | {"value": "1", "unit": "MILLIMOLAR"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://togomedium.org/medium/M2916

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
