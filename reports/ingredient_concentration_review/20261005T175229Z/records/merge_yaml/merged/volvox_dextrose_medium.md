# Ingredient Concentration Review

- Record: data/merge_yaml/merged/volvox_dextrose_medium.yaml
- ID: CultureMech:000237
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 34b4857fa9f321fbed9104902ce246465c637d2c85d3d690fc698d1393719838
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/4
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/algae/1_1_dyiii_pea_gr_medium.yaml
- data/normalized_yaml/algae/1_2_soil_seawater_medium.yaml
- data/normalized_yaml/algae/1_3_soil_seawater_medium.yaml
- data/normalized_yaml/algae/1_4_soil_seawater_medium.yaml
- data/normalized_yaml/algae/1_5_soil_seawater_medium.yaml
- data/normalized_yaml/algae/modified_2x_chev_soil_medium.yaml
- data/normalized_yaml/algae/volvox_dextrose_medium.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / 1 | {"value": "variable", "unit": "G_PER_L"} | missing_attached_evidence; RANGE_OR_NONNUMERIC_REQUIRES_SOURCE | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / 2 | {"value": "variable", "unit": "G_PER_L"} | missing_attached_evidence; RANGE_OR_NONNUMERIC_REQUIRES_SOURCE | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / 3 | {"value": "variable", "unit": "G_PER_L"} | missing_attached_evidence; RANGE_OR_NONNUMERIC_REQUIRES_SOURCE | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / 4 | {"value": "variable", "unit": "G_PER_L"} | missing_attached_evidence; RANGE_OR_NONNUMERIC_REQUIRES_SOURCE | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://utex.org/products/volvox-dextrose-medium

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
