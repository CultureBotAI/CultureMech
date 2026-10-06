# Ingredient Concentration Review

- Record: data/merge_yaml/merged/modified_halobacteria_medium_3.yaml
- ID: CultureMech:002192
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 8352da6c5c5c6fc9730a69131e178496a70c675c48ab08bd32b4203379db00e4
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/9
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/archaea/TOGO_M1064_Modified_Halobacteria_Medium-2.yaml
- data/normalized_yaml/archaea/TOGO_M1065_Modified_Halobacteria_Medium-3.yaml
- data/normalized_yaml/archaea/TOGO_M1212_Halobacteria_Medium_pH_8.0.yaml
- data/normalized_yaml/archaea/TOGO_M576_Modified_Halobacteria_Medium.yaml
- data/normalized_yaml/archaea/TOGO_M817_Halobacterium_TMM_Mediium.yaml
- data/normalized_yaml/archaea/TOGO_M818_Halobacterium_TMM_Mediium.yaml
- data/normalized_yaml/archaea/TOGO_M959_Halobacteria_Medium_With_15_NaCl.yaml
- data/normalized_yaml/archaea/TOGO_M960_Halobacteria_Medium_With_15_NaCl.yaml
- data/normalized_yaml/archaea/halobacteria_medium_ph_8_0.yaml
- data/normalized_yaml/archaea/halobacteria_medium_with_15_nacl.yaml
- data/normalized_yaml/archaea/halobacterium_tmm_mediium.yaml
- data/normalized_yaml/archaea/modified_halobacteria_medium.yaml
- data/normalized_yaml/archaea/modified_halobacteria_medium_2.yaml
- data/normalized_yaml/archaea/modified_halobacteria_medium_3.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Casamino acids | {"value": "5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Yeast extract | {"value": "5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Na glutamate | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / Trisodium citrate | {"value": "3", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / MgSO4 x 7 H2O | {"value": "20", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[5].concentration / KCl | {"value": "2", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[6].concentration / NaCl | {"value": "200", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[7].concentration / FeCl2 x 4 H2O | {"value": "36", "unit": "MG_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[8].concentration / MnCl2 x 4 H2O | {"value": "0.36", "unit": "MG_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1008

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
