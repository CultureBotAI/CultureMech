# Ingredient Concentration Review

- Record: data/merge_yaml/merged/cr1_diatom_medium.yaml
- ID: CultureMech:000152
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 1129ae15e0bedb5b19fdf01f04f2974e8a1f30cfc6bc5c6b3311fa70f6334ea9
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/3
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/algae/2x_soil_seawater_medium.yaml
- data/normalized_yaml/algae/CR1+_Diatom_Medium.yaml
- data/normalized_yaml/algae/Soilwater_GR-_Medium.yaml
- data/normalized_yaml/algae/cr1_s_diatom_medium.yaml
- data/normalized_yaml/algae/soil_extract_sodium_metasilicate_medium.yaml
- data/normalized_yaml/algae/soilwater_gr_medium.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / 1 | {"value": "variable", "unit": "G_PER_L"} | missing_attached_evidence; RANGE_OR_NONNUMERIC_REQUIRES_SOURCE | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / 2 | {"value": "variable", "unit": "G_PER_L"} | missing_attached_evidence; RANGE_OR_NONNUMERIC_REQUIRES_SOURCE | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / 3 | {"value": "variable", "unit": "G_PER_L"} | missing_attached_evidence; RANGE_OR_NONNUMERIC_REQUIRES_SOURCE | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://utex.org/products/cr1-plus-diatom-medium

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
