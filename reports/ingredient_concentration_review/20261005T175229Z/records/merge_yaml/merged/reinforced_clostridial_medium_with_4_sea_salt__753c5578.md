# Ingredient Concentration Review

- Record: data/merge_yaml/merged/reinforced_clostridial_medium_with_4_sea_salt__753c5578.yaml
- ID: CultureMech:002832
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 4292209181cdcc147a84c37d479e572d6fff71e98a29a9c08ed23c494ed4b4bb
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/3
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/TOGO_M482_Reinforced_Clostridial_Medium_With_3_Sea_Salt.yaml
- data/normalized_yaml/bacterial/TOGO_M483_Reinforced_Clostridial_Medium_With_4_Sea_Salt.yaml
- data/normalized_yaml/bacterial/reinforced_clostridial_medium_with_3_sea_salt.yaml
- data/normalized_yaml/bacterial/reinforced_clostridial_medium_with_4_sea_salt.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Reinforced clostridial medium | {"value": "38", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Sea Salt | {"value": "30", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Agar | {"value": "15", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=482

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
