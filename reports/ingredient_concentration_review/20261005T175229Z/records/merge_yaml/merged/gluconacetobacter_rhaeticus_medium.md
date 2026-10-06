# Ingredient Concentration Review

- Record: data/merge_yaml/merged/gluconacetobacter_rhaeticus_medium.yaml
- ID: CultureMech:003603
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 2051ad78b1f6b793d5c008f8914e5396c16fe16d00e9256f225f2df09e09536e
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/3
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/KOMODO_1044_GLUCONACETOBACTER_RHAETICUS_medium.yaml
- data/normalized_yaml/bacterial/KOMODO_850_ALTERNATIVE_ACETOBACTER_INTERMEDIUS_medium.yaml
- data/normalized_yaml/bacterial/acetobacter_musti_medium.yaml
- data/normalized_yaml/bacterial/alternative_acetobacter_intermedius_medium.yaml
- data/normalized_yaml/bacterial/gluconacetobacter_rhaeticus_medium.yaml
- data/normalized_yaml/bacterial/gy_medium.yaml
- data/normalized_yaml/bacterial/yed_acetobacter_medium.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Glucose | {"value": "50", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Yeast extract | {"value": "5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Agar | {"value": "15", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.


## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
