# Ingredient Concentration Review

- Record: data/merge_yaml/merged/r75s_nsw.yaml
- ID: CultureMech:000119
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: aaee1e2c1824bb8cff97406c8a9921c5b3c62372dc2f44cebe403b58d1fd0a40
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/1
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/algae/n75s.yaml
- data/normalized_yaml/algae/n75s_nsw.yaml
- data/normalized_yaml/algae/r75s.yaml
- data/normalized_yaml/algae/r75s_nsw.yaml
- data/normalized_yaml/bacterial/n75s.yaml
- data/normalized_yaml/bacterial/n75s_nsw.yaml
- data/normalized_yaml/bacterial/r75s.yaml
- data/normalized_yaml/bacterial/r75s_nsw.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Bring | {"value": "75", "unit": "PERCENT_W_V"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://www.ccap.ac.uk/wp-content/uploads/MR_R75S_NSW.pdf

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
