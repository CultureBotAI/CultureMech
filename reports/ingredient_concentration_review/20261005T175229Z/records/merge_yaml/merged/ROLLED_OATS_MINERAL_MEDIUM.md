# Ingredient Concentration Review

- Record: data/merge_yaml/merged/ROLLED_OATS_MINERAL_MEDIUM.yaml
- ID: CultureMech:006657
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 6b1476085f219cb69d9298edb025d9adc38b40bd17bbd91c589677ad67b0d8c9
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/5
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/KOMODO_84_ROLLED_OATS_MINERAL_medium.yaml
- data/normalized_yaml/bacterial/medium_84_modified_for_dsm_40886.yaml
- data/normalized_yaml/bacterial/medium_84_modified_for_dsm_40887.yaml
- data/normalized_yaml/bacterial/medium_84_modified_for_dsm_40888.yaml
- data/normalized_yaml/bacterial/medium_84_modified_for_dsm_40889.yaml
- data/normalized_yaml/bacterial/medium_84_modified_for_dsm_41697.yaml
- data/normalized_yaml/bacterial/medium_84_modified_for_dsm_44681.yaml
- data/normalized_yaml/bacterial/rolled_oats_mineral_medium.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Rolled oats | {"value": "20", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Agar | {"value": "20", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / FeSO4 x 7 H2O | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence; PLAUSIBILITY_TRACE_SALT_AS_STOCK | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / MnCl2 x 4 H2O | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence; PLAUSIBILITY_TRACE_SALT_AS_STOCK | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / ZnSO4 x 7 H2O | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence; PLAUSIBILITY_TRACE_SALT_AS_STOCK | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.


## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
