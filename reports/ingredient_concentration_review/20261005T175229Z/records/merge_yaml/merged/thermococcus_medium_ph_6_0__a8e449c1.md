# Ingredient Concentration Review

- Record: data/merge_yaml/merged/thermococcus_medium_ph_6_0__a8e449c1.yaml
- ID: CultureMech:009724
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 534baa94f8d68699bf8ff69373ccb3378aca8646485fddb5a85494146ec32eff
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/2
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/archaea/TOGO_M345_Thermococcus_Medium_pH_6.0.yaml
- data/normalized_yaml/bacterial/salt_base_solution_medium_1189.yaml
- data/normalized_yaml/bacterial/salt_solution_medium_592.yaml
- data/normalized_yaml/bacterial/trace_element_solution_medium_882.yaml
- data/normalized_yaml/bacterial/wolfes_mineral_elixir_medium_792.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / H2SO4 | {"value": "variable", "unit": "VARIABLE"} | missing_attached_evidence; VARIABLE_REQUIRES_SOURCE | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[0].concentration / Thermococcus medium (see Medium [M273]) | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://togomedium.org/medium/M345
- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=350

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
