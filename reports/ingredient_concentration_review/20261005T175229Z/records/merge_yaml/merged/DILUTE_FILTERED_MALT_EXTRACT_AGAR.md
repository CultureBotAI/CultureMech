# Ingredient Concentration Review

- Record: data/merge_yaml/merged/DILUTE_FILTERED_MALT_EXTRACT_AGAR.yaml
- ID: CultureMech:004153
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: b641e2e6899efc292d526cd5eb270088a38f12a692c7c8eb55b7bc20b0143c5b
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/2
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/2_malt_agar.yaml
- data/normalized_yaml/bacterial/4_malt_agar.yaml
- data/normalized_yaml/bacterial/dilute_filtered_malt_extract_agar.yaml
- data/normalized_yaml/fungal/2_malt_agar.yaml
- data/normalized_yaml/fungal/4_malt_agar.yaml
- data/normalized_yaml/fungal/dilute_filtered_malt_extract_agar.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Malt extract | {"value": "50", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Agar | {"value": "150", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.


## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
