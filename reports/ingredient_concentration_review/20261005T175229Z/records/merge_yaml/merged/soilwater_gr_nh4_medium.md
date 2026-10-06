# Ingredient Concentration Review

- Record: data/merge_yaml/merged/soilwater_gr_nh4_medium.yaml
- ID: CultureMech:000228
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: ed2e846f89785f60c8bcbc6a08a98022ad42ab083a7ace52e8010105bf79969a
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/2
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/algae/1_4_erdschreibers_medium.yaml
- data/normalized_yaml/algae/20_allen_80_erdschreiber_1_4_medium.yaml
- data/normalized_yaml/algae/5_3_soil_seawater_agar_medium.yaml
- data/normalized_yaml/algae/Soilwater_GR-_NH4_Medium.yaml
- data/normalized_yaml/algae/bg_11_0_36_nacl_medium.yaml
- data/normalized_yaml/algae/bg_11_1_nacl_medium.yaml
- data/normalized_yaml/algae/bristol_nacl_medium.yaml
- data/normalized_yaml/algae/chus_medium.yaml
- data/normalized_yaml/algae/f_2_nh4_medium.yaml
- data/normalized_yaml/algae/soil_seawater_medium.yaml
- data/normalized_yaml/algae/soilwater_gr_nh4_medium.yaml
- data/normalized_yaml/algae/waris_soil_extract_medium.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / 1 | {"value": "variable", "unit": "G_PER_L"} | missing_attached_evidence; RANGE_OR_NONNUMERIC_REQUIRES_SOURCE | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / 2 | {"value": "variable", "unit": "G_PER_L"} | missing_attached_evidence; RANGE_OR_NONNUMERIC_REQUIRES_SOURCE | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://utex.org/products/soilwater-gr-minus-nh4-medium

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
